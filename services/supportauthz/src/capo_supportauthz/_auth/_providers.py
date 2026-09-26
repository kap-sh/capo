from __future__ import annotations

import configparser
import hashlib
import json
import os
import time
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Generic, TypeVar, cast

from zapros import AsyncClient, Client, ZaprosError

from capo_supportauthz._auth._identity import (
    Credentials,
    Identity,
)
from capo_supportauthz._services._aws_config import (
    _load_profile,
    active_profile,
    config_file,
)

# The SSO, assume-role and web-identity providers call other AWS services, so
# they need the `sso` extra: `pip install capo-supportauthz[sso]`. Without it the imports
# below stay `None` and only those providers fail — see `require_dependency`.
if TYPE_CHECKING:
    import capo_sso
    import capo_sso.errors
    import capo_sso.types.get_role_credentials_response
    import capo_sso_oidc
    import capo_sso_oidc.errors
    import capo_sso_oidc.types.create_token_response
    import capo_sts
    import capo_sts.types.credentials
else:
    try:
        import capo_sso
        import capo_sso.errors
    except ImportError:
        capo_sso = None
    try:
        import capo_sso_oidc
        import capo_sso_oidc.errors
    except ImportError:
        capo_sso_oidc = None
    try:
        import capo_sts
    except ImportError:
        capo_sts = None

# refresh an SSO token this long before it actually expires
SSO_TOKEN_REFRESH_WINDOW = timedelta(minutes=5)


class IdentityNotFound(Exception):
    """Raised when a provider cannot resolve an identity. Chain continues."""


class MissingDependencyError(Exception):
    """Raised when a provider needs the `sso` extra but it is not installed."""


class SSOError(Exception):
    """Raised when SSO is configured but unusable. Chain stops."""


class AssumeRoleError(Exception):
    """Raised when a `role_arn` profile is configured but unusable. Chain stops."""


def require_dependency(module: object | None, package: str) -> None:
    if module is None:
        raise MissingDependencyError(
            f"{package} is required for this credentials provider but is not "
            "installed; reinstall with the sso feature enabled: capo-supportauthz[sso]"
        )


IdentityT = TypeVar("IdentityT", bound="Identity")


class IdentityProvider(Generic[IdentityT]):
    @abstractmethod
    def resolve_identity(self) -> IdentityT:
        raise NotImplementedError

    async def aresolve_identity(self) -> IdentityT:
        # default: no network I/O, reuse the sync resolution
        return self.resolve_identity()


class ChainedProvider(IdentityProvider[IdentityT]):
    """Try each provider in order; first non-`IdentityNotFound` wins."""

    def __init__(self, *providers: IdentityProvider[IdentityT]) -> None:
        if not providers:
            raise ValueError("ChainedProvider requires at least one provider")
        self._providers = providers

    def resolve_identity(self) -> IdentityT:
        errors: list[str] = []
        for p in self._providers:
            try:
                return p.resolve_identity()
            except IdentityNotFound as e:
                errors.append(f"{type(p).__name__}: {e}")
        raise IdentityNotFound("no provider succeeded: " + "; ".join(errors))

    async def aresolve_identity(self) -> IdentityT:
        errors: list[str] = []
        for p in self._providers:
            try:
                return await p.aresolve_identity()
            except IdentityNotFound as e:
                errors.append(f"{type(p).__name__}: {e}")
        raise IdentityNotFound("no provider succeeded: " + "; ".join(errors))


class CachedProvider(IdentityProvider[IdentityT]):
    """Cache an identity until its `expiration` (minus skew) elapses."""

    _SKEW_SECONDS = 60

    def __init__(self, inner: IdentityProvider[IdentityT]) -> None:
        self._inner = inner
        self._cached: IdentityT | None = None

    def resolve_identity(self) -> IdentityT:
        if self._cached is not None and not self._expired(self._cached):
            return self._cached
        self._cached = self._inner.resolve_identity()
        return self._cached

    async def aresolve_identity(self) -> IdentityT:
        if self._cached is not None and not self._expired(self._cached):
            return self._cached
        self._cached = await self._inner.aresolve_identity()
        return self._cached

    @classmethod
    def _expired(cls, ident: Identity) -> bool:
        exp = ident.get("expiration")
        if exp is None:
            return False
        return (exp - datetime.now(timezone.utc)).total_seconds() <= cls._SKEW_SECONDS


class CredentialsProvider(IdentityProvider[Credentials]):
    """Base class for providers that resolve AWS `Credentials`."""

    @abstractmethod
    def resolve_identity(self) -> Credentials:
        raise NotImplementedError


class StaticAwsCredentialsProvider(CredentialsProvider):
    def __init__(self, credentials: Credentials) -> None:
        self._credentials = credentials

    def resolve_identity(self) -> Credentials:
        return self._credentials


class EnvCredentialsProvider(CredentialsProvider):
    """Read AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_SESSION_TOKEN."""

    def resolve_identity(self) -> Credentials:
        ak = os.environ.get("AWS_ACCESS_KEY_ID")
        sk = os.environ.get("AWS_SECRET_ACCESS_KEY")
        if not ak or not sk:
            raise IdentityNotFound("AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY unset")
        out: Credentials = {"access_key": ak, "secret_key": sk}
        token = os.environ.get("AWS_SESSION_TOKEN")
        if token:
            out["session_token"] = token
        return out


class ProfileCredentialsProvider(CredentialsProvider):
    """Read ~/.aws/credentials and ~/.aws/config for the active profile."""

    def __init__(
        self, credentials_file: Path | None = None, profile: str | None = None
    ) -> None:
        self._profile = profile or active_profile()
        self._cred_file = credentials_file or Path(
            os.environ.get("AWS_SHARED_CREDENTIALS_FILE")
            or Path.home() / ".aws" / "credentials"
        )

    def resolve_identity(self) -> Credentials:
        section = self._load_section()
        ak = section.get("aws_access_key_id")
        sk = section.get("aws_secret_access_key")
        if not ak or not sk:
            raise IdentityNotFound(
                f"profile {self._profile!r}: missing aws_access_key_id/aws_secret_access_key"
            )
        out: Credentials = {"access_key": ak, "secret_key": sk}
        token = section.get("aws_session_token")
        if token:
            out["session_token"] = token
        return out

    def _load_section(self) -> dict[str, str]:
        # config-file profile reuses the loader from _services/_aws_config
        merged, _ = _load_profile(self._profile)
        if self._cred_file.is_file():
            cfg = configparser.ConfigParser(interpolation=None)
            cfg.read(self._cred_file)
            if cfg.has_section(self._profile):
                merged.update(dict(cfg.items(self._profile)))
        if not merged:
            raise IdentityNotFound(
                f"profile {self._profile!r} not found in credentials/config files"
            )
        return merged


class EcsContainerCredentialsProvider(CredentialsProvider):
    """Resolve credentials from the ECS/EKS container credentials endpoint."""

    def __init__(self, client: Client | AsyncClient) -> None:
        self._client = client

    def resolve_identity(self) -> Credentials:
        if isinstance(self._client, AsyncClient):
            raise TypeError(
                "EcsContainerCredentialsProvider configured with AsyncClient; use aresolve_identity"
            )
        url, headers = self._request_args()
        resp = self._client.get(url, headers=headers)
        if resp.status < 200 or resp.status >= 300:
            raise IdentityNotFound(
                f"ECS credentials endpoint returned status {resp.status}"
            )
        return _credentials_from_json(resp.json)

    async def aresolve_identity(self) -> Credentials:
        if not isinstance(self._client, AsyncClient):
            raise TypeError(
                "EcsContainerCredentialsProvider configured with sync Client; use resolve_identity"
            )
        url, headers = self._request_args()
        resp = await self._client.get(url, headers=headers)
        if resp.status < 200 or resp.status >= 300:
            raise IdentityNotFound(
                f"ECS credentials endpoint returned status {resp.status}"
            )
        return _credentials_from_json(resp.json)

    def _request_args(self) -> tuple[str, dict[str, str]]:
        relative = os.environ.get("AWS_CONTAINER_CREDENTIALS_RELATIVE_URI")
        full = os.environ.get("AWS_CONTAINER_CREDENTIALS_FULL_URI")
        if relative:
            url = "http://169.254.170.2" + relative
        elif full:
            url = full
        else:
            raise IdentityNotFound("no ECS container credentials env var set")
        headers: dict[str, str] = {}
        token = os.environ.get("AWS_CONTAINER_AUTHORIZATION_TOKEN")
        token_file = os.environ.get("AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE")
        if token_file:
            token = Path(token_file).read_text().strip()
        if token:
            headers["Authorization"] = token
        return url, headers


class Ec2InstanceMetadataProvider(CredentialsProvider):
    """Resolve credentials from the EC2 Instance Metadata Service (IMDSv2)."""

    _BASE = "http://169.254.169.254"
    _TOKEN_PATH = "/latest/api/token"
    _CREDS_PATH = "/latest/meta-data/iam/security-credentials/"

    def __init__(self, client: Client | AsyncClient) -> None:
        self._client = client

    def resolve_identity(self) -> Credentials:
        if isinstance(self._client, AsyncClient):
            raise TypeError(
                "Ec2InstanceMetadataProvider configured with AsyncClient; use aresolve_identity"
            )
        if os.environ.get("AWS_EC2_METADATA_DISABLED", "").strip().lower() in (
            "true",
            "1",
        ):
            raise IdentityNotFound("IMDS disabled via AWS_EC2_METADATA_DISABLED")
        try:
            token_resp = self._client.put(
                self._BASE + self._TOKEN_PATH,
                headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
                body=b"",
            )
            auth = {"X-aws-ec2-metadata-token": token_resp.text}
            role_resp = self._client.get(self._BASE + self._CREDS_PATH, headers=auth)
            role = role_resp.text.strip()
            creds_resp = self._client.get(
                self._BASE + self._CREDS_PATH + role, headers=auth
            )
        except ZaprosError as e:
            raise IdentityNotFound(f"IMDS request failed: {e}")
        if creds_resp.status < 200 or creds_resp.status >= 300:
            raise IdentityNotFound(f"IMDS returned status {creds_resp.status}")
        return _credentials_from_json(creds_resp.json)

    async def aresolve_identity(self) -> Credentials:
        if not isinstance(self._client, AsyncClient):
            raise TypeError(
                "Ec2InstanceMetadataProvider configured with sync Client; use resolve_identity"
            )
        if os.environ.get("AWS_EC2_METADATA_DISABLED", "").strip().lower() in (
            "true",
            "1",
        ):
            raise IdentityNotFound("IMDS disabled via AWS_EC2_METADATA_DISABLED")
        try:
            token_resp = await self._client.put(
                self._BASE + self._TOKEN_PATH,
                headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
                body=b"",
            )
            auth = {"X-aws-ec2-metadata-token": token_resp.text}
            role_resp = await self._client.get(
                self._BASE + self._CREDS_PATH, headers=auth
            )
            role = role_resp.text.strip()
            creds_resp = await self._client.get(
                self._BASE + self._CREDS_PATH + role, headers=auth
            )
        except ZaprosError as e:
            raise IdentityNotFound(f"IMDS request failed: {e}")
        if creds_resp.status < 200 or creds_resp.status >= 300:
            raise IdentityNotFound(f"IMDS returned status {creds_resp.status}")
        return _credentials_from_json(creds_resp.json)


@dataclass(frozen=True)
class SsoConfig:
    start_url: str
    region: str
    account_id: str
    role_name: str
    session_name: str | None


class SsoCredentialsProvider(CredentialsProvider):
    """Resolve credentials from AWS IAM Identity Center (SSO).

    Reads the profile's ``sso_*`` settings, loads the access token that
    ``aws sso login`` cached under ``~/.aws/sso/cache`` (refreshing it through
    SSO-OIDC when it is about to expire) and exchanges it for short-term
    credentials through the SSO ``GetRoleCredentials`` API.
    """

    def __init__(
        self, client: Client | AsyncClient, profile: str | None = None
    ) -> None:
        self._client = client
        self._profile = profile

    def resolve_identity(self) -> Credentials:
        if isinstance(self._client, AsyncClient):
            raise TypeError(
                "SsoCredentialsProvider configured with AsyncClient; use aresolve_identity"
            )
        # resolve the config first so an unconfigured profile just skips SSO
        config = load_sso_config(self._profile)
        require_dependency(capo_sso, "capo-sso")
        token = load_sso_token(config, self._client)
        sso = capo_sso.SSOClient(http_handler=self._client.handler)
        try:
            response = sso.get_role_credentials(
                config.role_name,
                config.account_id,
                token,
                config_overrides={
                    "region": config.region,
                    "credentials_provider": None,
                },
            )
        except capo_sso.errors.UnauthorizedException as e:
            raise SSOError(f"SSO token rejected; run `aws sso login`: {e}")
        return credentials_from_role_credentials(response)

    async def aresolve_identity(self) -> Credentials:
        if not isinstance(self._client, AsyncClient):
            raise TypeError(
                "SsoCredentialsProvider configured with sync Client; use resolve_identity"
            )
        # resolve the config first so an unconfigured profile just skips SSO
        config = load_sso_config(self._profile)
        require_dependency(capo_sso, "capo-sso")
        token = await aload_sso_token(config, self._client)
        sso = capo_sso.AsyncSSOClient(http_handler=self._client.handler)
        try:
            response = await sso.get_role_credentials(
                config.role_name,
                config.account_id,
                token,
                config_overrides={
                    "region": config.region,
                    "credentials_provider": None,
                },
            )
        except capo_sso.errors.UnauthorizedException as e:
            raise SSOError(f"SSO token rejected; run `aws sso login`: {e}")
        return credentials_from_role_credentials(response)


def load_config_section(name: str) -> dict[str, str]:
    cfg_file = config_file()
    if not cfg_file.is_file():
        return {}
    cfg = configparser.ConfigParser(interpolation=None)
    cfg.read(cfg_file)
    return dict(cfg.items(name)) if cfg.has_section(name) else {}


def load_sso_config(profile_name: str | None = None) -> SsoConfig:
    profile, _ = _load_profile(profile_name)
    session_name = profile.get("sso_session")
    if session_name is None and not any(k.startswith("sso_") for k in profile):
        raise IdentityNotFound("profile has no sso_* settings")
    if session_name is not None:
        # `sso_session` moves the portal settings into an [sso-session NAME] section
        session = load_config_section(f"sso-session {session_name}")
        start_url = session.get("sso_start_url")
        region = session.get("sso_region")
    else:
        start_url = profile.get("sso_start_url")
        region = profile.get("sso_region")
    account_id = profile.get("sso_account_id")
    role_name = profile.get("sso_role_name")
    missing = [
        name
        for name, value in (
            ("sso_start_url", start_url),
            ("sso_region", region),
            ("sso_account_id", account_id),
            ("sso_role_name", role_name),
        )
        if not value
    ]
    if missing:
        raise SSOError("incomplete sso configuration: missing " + ", ".join(missing))
    assert start_url and region and account_id and role_name  # narrowed by `missing`
    return SsoConfig(
        start_url=start_url,
        region=region,
        account_id=account_id,
        role_name=role_name,
        session_name=session_name,
    )


def read_sso_token_cache(config: SsoConfig) -> tuple[Path, dict[str, object]]:
    # cache file is sha1 of the session name (new format) or the start url (legacy)
    key = config.session_name or config.start_url
    digest = hashlib.sha1(key.encode("utf-8")).hexdigest()
    path = Path.home() / ".aws" / "sso" / "cache" / f"{digest}.json"
    if not path.is_file():
        raise SSOError(f"no cached SSO token at {path}; run `aws sso login`")
    data = json.loads(path.read_text())
    if not isinstance(data.get("accessToken"), str) or not isinstance(
        data.get("expiresAt"), str
    ):
        raise SSOError(f"SSO token cache {path} has no accessToken/expiresAt")
    return path, data


def unexpired_sso_token(data: dict[str, object], *, skew: timedelta) -> str | None:
    """The cached token if it is still good for at least ``skew``, else None."""
    expires_at = parse_sso_expiry(str(data["expiresAt"]))
    if expires_at - datetime.now(timezone.utc) <= skew:
        return None
    return str(data["accessToken"])


def sso_refresh_args(data: dict[str, object]) -> tuple[str, str, str] | None:
    """Client registration + refresh token, if this entry can be refreshed.

    Only tokens cached for an ``sso_session`` carry a client registration; the
    legacy ``sso_start_url`` format has nothing to refresh with.
    """
    client_id = data.get("clientId")
    client_secret = data.get("clientSecret")
    refresh_token = data.get("refreshToken")
    if (
        not isinstance(client_id, str)
        or not isinstance(client_secret, str)
        or not isinstance(refresh_token, str)
    ):
        return None
    registration_expires_at = data.get("registrationExpiresAt")
    if isinstance(registration_expires_at, str):
        if parse_sso_expiry(registration_expires_at) <= datetime.now(timezone.utc):
            return None
    return client_id, client_secret, refresh_token


def load_sso_token(config: SsoConfig, client: Client) -> str:
    path, data = read_sso_token_cache(config)
    fresh = unexpired_sso_token(data, skew=SSO_TOKEN_REFRESH_WINDOW)
    if fresh is not None:
        return fresh
    refresh_args = sso_refresh_args(data)
    if refresh_args is not None:
        require_dependency(capo_sso_oidc, "capo-sso-oidc")
        oidc = capo_sso_oidc.SSOOIDCClient(http_handler=client.handler)
        try:
            response = oidc.create_token(
                refresh_args[0],
                refresh_args[1],
                "refresh_token",
                refresh_token=refresh_args[2],
                config_overrides={
                    "region": config.region,
                    "credentials_provider": None,
                },
            )
        except (capo_sso_oidc.errors.SSOOIDCError, ZaprosError):
            return sso_token_or_error(data, path)
        return store_refreshed_sso_token(path, data, response)
    return sso_token_or_error(data, path)


async def aload_sso_token(config: SsoConfig, client: AsyncClient) -> str:
    path, data = read_sso_token_cache(config)
    fresh = unexpired_sso_token(data, skew=SSO_TOKEN_REFRESH_WINDOW)
    if fresh is not None:
        return fresh
    refresh_args = sso_refresh_args(data)
    if refresh_args is not None:
        require_dependency(capo_sso_oidc, "capo-sso-oidc")
        oidc = capo_sso_oidc.AsyncSSOOIDCClient(http_handler=client.handler)
        try:
            response = await oidc.create_token(
                refresh_args[0],
                refresh_args[1],
                "refresh_token",
                refresh_token=refresh_args[2],
                config_overrides={
                    "region": config.region,
                    "credentials_provider": None,
                },
            )
        except (capo_sso_oidc.errors.SSOOIDCError, ZaprosError):
            return sso_token_or_error(data, path)
        return store_refreshed_sso_token(path, data, response)
    return sso_token_or_error(data, path)


def sso_token_or_error(data: dict[str, object], path: Path) -> str:
    """Fall back to the cached token when refreshing was impossible or failed."""
    token = unexpired_sso_token(data, skew=timedelta(0))
    if token is None:
        raise SSOError(
            f"cached SSO token in {path} expired at {data['expiresAt']}; "
            "run `aws sso login`"
        )
    return token


def store_refreshed_sso_token(
    path: Path,
    data: dict[str, object],
    response: capo_sso_oidc.types.create_token_response.CreateTokenResponse,
) -> str:
    access_token = response.get("access_token")
    if not access_token:
        raise SSOError("CreateToken response has no accessToken")
    expires_at = datetime.now(timezone.utc) + timedelta(
        seconds=response.get("expires_in", 0)
    )
    updated = dict(data)
    updated["accessToken"] = access_token
    updated["expiresAt"] = expires_at.strftime("%Y-%m-%dT%H:%M:%SZ")
    refresh_token = response.get("refresh_token")
    if refresh_token:
        updated["refreshToken"] = refresh_token
    path.write_text(json.dumps(updated))
    path.chmod(0o600)
    return access_token


def parse_sso_expiry(value: str) -> datetime:
    # the CLI writes either an ISO offset, a trailing 'Z', or a trailing 'UTC'
    parsed = datetime.fromisoformat(value.removesuffix("UTC").removesuffix("Z"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def credentials_from_role_credentials(
    response: capo_sso.types.get_role_credentials_response.GetRoleCredentialsResponse,
) -> Credentials:
    role = response.get("role_credentials") or {}
    ak = role.get("access_key_id")
    sk = role.get("secret_access_key")
    if not ak or not sk:
        raise SSOError("GetRoleCredentials response missing access key / secret key")
    out: Credentials = {"access_key": ak, "secret_key": sk}
    token = role.get("session_token")
    if token:
        out["session_token"] = token
    expiration = role.get("expiration")
    if expiration:
        # SSO reports the expiry in epoch milliseconds
        out["expiration"] = datetime.fromtimestamp(expiration / 1000, timezone.utc)
    return out


@dataclass(frozen=True)
class AssumeRoleConfig:
    role_arn: str
    session_name: str
    region: str
    external_id: str | None
    duration_seconds: int | None


class AssumeRoleCredentialsProvider(CredentialsProvider):
    """Assume the profile's ``role_arn`` through STS ``AssumeRole``.

    The credentials used to make the call come from the profile's
    ``source_profile`` (which may itself be an SSO profile, or another
    ``role_arn`` profile for role chaining) or from ``credential_source``.
    """

    def __init__(
        self,
        client: Client | AsyncClient,
        profile: str | None = None,
        _visited: frozenset[str] = frozenset(),
    ) -> None:
        self._client = client
        self._profile = profile
        self._visited = _visited

    def resolve_identity(self) -> Credentials:
        if isinstance(self._client, AsyncClient):
            raise TypeError(
                "AssumeRoleCredentialsProvider configured with AsyncClient; use aresolve_identity"
            )
        # resolve the config first so a profile without role_arn just skips
        section, _ = _load_profile(self._profile)
        config = assume_role_config(section)
        require_dependency(capo_sts, "capo-sts")
        source = self._source_provider(section)
        sts = capo_sts.STSClient(
            http_handler=self._client.handler,
            region=config.region,
            credentials_provider=cast("capo_sts.CredentialsProvider", source),
        )
        response = sts.assume_role(
            config.role_arn,
            config.session_name,
            external_id=config.external_id,
            duration_seconds=config.duration_seconds,
        )
        return credentials_from_sts(response.get("credentials"))

    async def aresolve_identity(self) -> Credentials:
        if not isinstance(self._client, AsyncClient):
            raise TypeError(
                "AssumeRoleCredentialsProvider configured with sync Client; use resolve_identity"
            )
        # resolve the config first so a profile without role_arn just skips
        section, _ = _load_profile(self._profile)
        config = assume_role_config(section)
        require_dependency(capo_sts, "capo-sts")
        source = self._source_provider(section)
        sts = capo_sts.AsyncSTSClient(
            http_handler=self._client.handler,
            region=config.region,
            credentials_provider=cast("capo_sts.CredentialsProvider", source),
        )
        response = await sts.assume_role(
            config.role_arn,
            config.session_name,
            external_id=config.external_id,
            duration_seconds=config.duration_seconds,
        )
        return credentials_from_sts(response.get("credentials"))

    def _source_provider(
        self, section: dict[str, str]
    ) -> IdentityProvider[Credentials]:
        source_profile = section.get("source_profile")
        credential_source = section.get("credential_source")
        if source_profile and credential_source:
            raise AssumeRoleError(
                "source_profile and credential_source are mutually exclusive"
            )
        if credential_source:
            match credential_source:
                case "Environment":
                    return EnvCredentialsProvider()
                case "Ec2InstanceMetadata":
                    return Ec2InstanceMetadataProvider(self._client)
                case "EcsContainer":
                    return EcsContainerCredentialsProvider(self._client)
                case _:
                    raise AssumeRoleError(
                        f"unsupported credential_source {credential_source!r}"
                    )
        if source_profile in self._visited:
            raise AssumeRoleError(
                f"circular source_profile reference through {source_profile!r}"
            )
        assert source_profile is not None  # assume_role_config rejects the empty case
        return ChainedProvider(
            AssumeRoleCredentialsProvider(
                self._client, source_profile, self._visited | {source_profile}
            ),
            SsoCredentialsProvider(self._client, source_profile),
            ProfileCredentialsProvider(profile=source_profile),
        )


class WebIdentityCredentialsProvider(CredentialsProvider):
    """Exchange an OIDC token for credentials via ``AssumeRoleWithWebIdentity``.

    Reads ``AWS_WEB_IDENTITY_TOKEN_FILE``/``AWS_ROLE_ARN`` or the profile's
    ``web_identity_token_file``/``role_arn`` — this is how EKS service accounts
    (IRSA) obtain credentials.
    """

    def __init__(
        self, client: Client | AsyncClient, profile: str | None = None
    ) -> None:
        self._client = client
        self._profile = profile

    def resolve_identity(self) -> Credentials:
        if isinstance(self._client, AsyncClient):
            raise TypeError(
                "WebIdentityCredentialsProvider configured with AsyncClient; use aresolve_identity"
            )
        config, token = self._config()
        require_dependency(capo_sts, "capo-sts")
        sts = capo_sts.STSClient(
            http_handler=self._client.handler, region=config.region
        )
        response = sts.assume_role_with_web_identity(
            config.role_arn,
            config.session_name,
            token,
            duration_seconds=config.duration_seconds,
            config_overrides={"credentials_provider": None},
        )
        return credentials_from_sts(response.get("credentials"))

    async def aresolve_identity(self) -> Credentials:
        if not isinstance(self._client, AsyncClient):
            raise TypeError(
                "WebIdentityCredentialsProvider configured with sync Client; use resolve_identity"
            )
        config, token = self._config()
        require_dependency(capo_sts, "capo-sts")
        sts = capo_sts.AsyncSTSClient(
            http_handler=self._client.handler, region=config.region
        )
        response = await sts.assume_role_with_web_identity(
            config.role_arn,
            config.session_name,
            token,
            duration_seconds=config.duration_seconds,
            config_overrides={"credentials_provider": None},
        )
        return credentials_from_sts(response.get("credentials"))

    def _config(self) -> tuple[AssumeRoleConfig, str]:
        section, _ = _load_profile(self._profile)
        token_file = os.environ.get("AWS_WEB_IDENTITY_TOKEN_FILE")
        role_arn = os.environ.get("AWS_ROLE_ARN")
        session_name = os.environ.get("AWS_ROLE_SESSION_NAME")
        if not token_file or not role_arn:
            # the env pair is all-or-nothing; otherwise fall back to the profile
            token_file = section.get("web_identity_token_file")
            role_arn = section.get("role_arn")
            session_name = section.get("role_session_name")
        if not token_file or not role_arn:
            raise IdentityNotFound("no web identity token file / role arn configured")
        path = Path(token_file).expanduser()
        if not path.is_file():
            raise AssumeRoleError(f"web identity token file {path} does not exist")
        config = AssumeRoleConfig(
            role_arn=role_arn,
            session_name=session_name or default_session_name(),
            region=sts_region(section),
            external_id=None,
            duration_seconds=int_or_none(section.get("duration_seconds")),
        )
        return config, path.read_text().strip()


def assume_role_config(section: dict[str, str]) -> AssumeRoleConfig:
    role_arn = section.get("role_arn")
    if not role_arn:
        raise IdentityNotFound("profile has no role_arn")
    if section.get("web_identity_token_file"):
        # handled by WebIdentityCredentialsProvider, not AssumeRole
        raise IdentityNotFound("profile uses web_identity_token_file")
    if not section.get("source_profile") and not section.get("credential_source"):
        raise IdentityNotFound(
            "role_arn profile has no source_profile/credential_source"
        )
    if section.get("mfa_serial"):
        raise AssumeRoleError("mfa_serial profiles are not supported")
    return AssumeRoleConfig(
        role_arn=role_arn,
        session_name=section.get("role_session_name") or default_session_name(),
        region=sts_region(section),
        external_id=section.get("external_id"),
        duration_seconds=int_or_none(section.get("duration_seconds")),
    )


def default_session_name() -> str:
    return f"capo-session-{int(time.time())}"


def sts_region(section: dict[str, str]) -> str:
    return os.environ.get("AWS_REGION") or section.get("region") or "us-east-1"


def int_or_none(value: str | None) -> int | None:
    return int(value) if value else None


def credentials_from_sts(
    credentials: capo_sts.types.credentials.Credentials | None,
) -> Credentials:
    if credentials is None:
        raise AssumeRoleError("STS response contained no credentials")
    return {
        "access_key": credentials["access_key_id"],
        "secret_key": credentials["secret_access_key"],
        "session_token": credentials["session_token"],
        "expiration": credentials["expiration"],
    }


def _parse_iso8601(value: str) -> datetime:
    # tolerate trailing 'Z'
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _credentials_from_json(data: dict[str, object]) -> Credentials:
    ak = data.get("AccessKeyId")
    sk = data.get("SecretAccessKey")
    if not isinstance(ak, str) or not isinstance(sk, str):
        raise IdentityNotFound(
            "credentials response missing AccessKeyId/SecretAccessKey"
        )
    out: Credentials = {"access_key": ak, "secret_key": sk}
    token = data.get("Token")
    if isinstance(token, str):
        out["session_token"] = token
    exp = data.get("Expiration")
    if isinstance(exp, str):
        out["expiration"] = _parse_iso8601(exp)
    return out


def default_aws_credentials_chain(
    client: Client | AsyncClient,
) -> IdentityProvider[Credentials]:
    return CachedProvider(
        ChainedProvider(
            EnvCredentialsProvider(),
            AssumeRoleCredentialsProvider(client),
            WebIdentityCredentialsProvider(client),
            SsoCredentialsProvider(client),
            ProfileCredentialsProvider(),
            EcsContainerCredentialsProvider(client),
            Ec2InstanceMetadataProvider(client),
        )
    )
