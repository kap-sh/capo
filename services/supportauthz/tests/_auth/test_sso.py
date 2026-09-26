from __future__ import annotations

import asyncio
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest
from capo_supportauthz._auth._providers import (
    ChainedProvider,
    IdentityNotFound,
    SsoCredentialsProvider,
    SSOError,
    default_aws_credentials_chain,
    load_sso_config,
    load_sso_token,
    parse_sso_expiry,
)
from zapros import AsyncClient, Client, Response
from zapros.mock import Mock, MockMiddleware, MockRouter, path

_ROLE_CREDS_JSON = json.dumps(
    {
        "roleCredentials": {
            "accessKeyId": "AKSSO",
            "secretAccessKey": "ssosecret",
            "sessionToken": "ssotoken",
            "expiration": 1893456000000,  # 2030-01-01T00:00:00Z in epoch millis
        }
    }
)
_CLEARED_ENV = (
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_SESSION_TOKEN",
    "AWS_PROFILE",
    "AWS_DEFAULT_PROFILE",
    "AWS_REGION",
)


@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    for var in _CLEARED_ENV:
        monkeypatch.delenv(var, raising=False)
    # both the config file and the token cache (~/.aws/sso/cache) get redirected
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("AWS_CONFIG_FILE", str(tmp_path / "config"))


def _write_config(tmp_path: Path, body: str) -> None:
    (tmp_path / "config").write_text(body)


def _token_path(tmp_path: Path, key: str) -> Path:
    cache = tmp_path / ".aws" / "sso" / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    return cache / f"{hashlib.sha1(key.encode('utf-8')).hexdigest()}.json"


def _write_token(
    tmp_path: Path, key: str, token: str, expires_at: str, **extra: str
) -> Path:
    target = _token_path(tmp_path, key)
    target.write_text(
        json.dumps({"accessToken": token, "expiresAt": expires_at, **extra})
    )
    return target


def _legacy_profile(tmp_path: Path) -> None:
    _write_config(
        tmp_path,
        "[default]\n"
        "sso_start_url = https://example.awsapps.com/start\n"
        "sso_region = us-east-1\n"
        "sso_account_id = 123456789012\n"
        "sso_role_name = ReadOnly\n",
    )


def _session_profile(tmp_path: Path) -> None:
    _write_config(
        tmp_path,
        "[default]\n"
        "sso_session = my-session\n"
        "sso_account_id = 123456789012\n"
        "sso_role_name = ReadOnly\n"
        "\n"
        "[sso-session my-session]\n"
        "sso_start_url = https://example.awsapps.com/start\n"
        "sso_region = eu-west-1\n",
    )


def _mock_router(*mocks: Mock) -> MockMiddleware:
    router = MockRouter()
    for m in mocks:
        router.add(m)
    return MockMiddleware(router=router)


def test_load_sso_config_legacy(tmp_path: Path) -> None:
    _legacy_profile(tmp_path)
    config = load_sso_config()
    assert config.start_url == "https://example.awsapps.com/start"
    assert config.region == "us-east-1"
    assert config.account_id == "123456789012"
    assert config.role_name == "ReadOnly"
    assert config.session_name is None


def test_load_sso_config_session(tmp_path: Path) -> None:
    _session_profile(tmp_path)
    config = load_sso_config()
    assert config.start_url == "https://example.awsapps.com/start"
    assert config.region == "eu-west-1"
    assert config.session_name == "my-session"


def test_load_sso_config_absent(tmp_path: Path) -> None:
    _write_config(tmp_path, "[default]\nregion = us-east-1\n")
    with pytest.raises(IdentityNotFound):
        load_sso_config()


def test_load_sso_config_incomplete(tmp_path: Path) -> None:
    _write_config(
        tmp_path, "[default]\nsso_start_url = https://example.awsapps.com/start\n"
    )
    with pytest.raises(SSOError, match="sso_region"):
        load_sso_config()


def test_load_sso_token_legacy_cache_key(tmp_path: Path) -> None:
    _legacy_profile(tmp_path)
    _write_token(
        tmp_path,
        "https://example.awsapps.com/start",
        "cached-token",
        "2030-01-01T00:00:00Z",
    )
    assert load_sso_token(load_sso_config(), Client()) == "cached-token"


def test_load_sso_token_session_cache_key(tmp_path: Path) -> None:
    _session_profile(tmp_path)
    _write_token(tmp_path, "my-session", "session-token", "2030-01-01T00:00:00UTC")
    assert load_sso_token(load_sso_config(), Client()) == "session-token"


def test_load_sso_token_missing(tmp_path: Path) -> None:
    _legacy_profile(tmp_path)
    with pytest.raises(SSOError, match="aws sso login"):
        load_sso_token(load_sso_config(), Client())


def test_load_sso_token_expired(tmp_path: Path) -> None:
    _legacy_profile(tmp_path)
    _write_token(
        tmp_path, "https://example.awsapps.com/start", "old", "2020-01-01T00:00:00Z"
    )
    with pytest.raises(SSOError, match="expired"):
        load_sso_token(load_sso_config(), Client())


def test_resolve_identity(tmp_path: Path) -> None:
    _legacy_profile(tmp_path)
    _write_token(
        tmp_path,
        "https://example.awsapps.com/start",
        "cached-token",
        "2030-01-01T00:00:00Z",
    )
    mock = Mock.given(path("/federation/credentials")).respond(
        Response(200, text=_ROLE_CREDS_JSON)
    )
    creds = SsoCredentialsProvider(Client(_mock_router(mock))).resolve_identity()
    assert creds["access_key"] == "AKSSO"
    assert creds["secret_key"] == "ssosecret"
    assert creds["session_token"] == "ssotoken"
    assert creds["expiration"].year == 2030

    request = mock.calls[0]
    assert request.headers["x-amz-sso_bearer_token"] == "cached-token"
    # GetRoleCredentials is bearer-authenticated; it must not be SigV4-signed
    assert "authorization" not in request.headers
    assert request.url.host == "portal.sso.us-east-1.amazonaws.com"
    assert request.url.search_params["account_id"] == "123456789012"
    assert request.url.search_params["role_name"] == "ReadOnly"


def test_resolve_identity_async(tmp_path: Path) -> None:
    _session_profile(tmp_path)
    _write_token(tmp_path, "my-session", "session-token", "2030-01-01T00:00:00Z")
    mock = Mock.given(path("/federation/credentials")).respond(
        Response(200, text=_ROLE_CREDS_JSON)
    )

    async def run():
        client = AsyncClient(_mock_router(mock))
        return await SsoCredentialsProvider(client).aresolve_identity()

    creds = asyncio.run(run())
    assert creds["access_key"] == "AKSSO"
    assert mock.calls[0].url.host == "portal.sso.eu-west-1.amazonaws.com"


def test_unauthorized_token_raises_sso_error(tmp_path: Path) -> None:
    _legacy_profile(tmp_path)
    _write_token(
        tmp_path, "https://example.awsapps.com/start", "stale", "2030-01-01T00:00:00Z"
    )
    mock = Mock.given(path("/federation/credentials")).respond(
        Response(
            401,
            text=json.dumps({"message": "session expired"}),
            headers={"x-amzn-errortype": "UnauthorizedException"},
        )
    )
    with pytest.raises(SSOError, match="aws sso login"):
        SsoCredentialsProvider(Client(_mock_router(mock))).resolve_identity()


def test_sync_method_with_async_client_raises() -> None:
    with pytest.raises(TypeError):
        SsoCredentialsProvider(AsyncClient()).resolve_identity()


def test_async_method_with_sync_client_raises() -> None:
    with pytest.raises(TypeError):
        asyncio.run(SsoCredentialsProvider(Client()).aresolve_identity())


def test_refresh_expiring_token(tmp_path: Path) -> None:
    _session_profile(tmp_path)
    target = _write_token(
        tmp_path,
        "my-session",
        "about-to-expire",
        # inside the 5 minute refresh window
        (datetime.now(timezone.utc) + timedelta(minutes=2)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        clientId="client-id",
        clientSecret="client-secret",
        refreshToken="refresh-token",
        registrationExpiresAt="2030-01-01T00:00:00Z",
    )
    oidc = Mock.given(path("/token")).respond(
        Response(
            200,
            text=json.dumps(
                {
                    "accessToken": "refreshed-token",
                    "expiresIn": 3600,
                    "refreshToken": "next-refresh-token",
                }
            ),
        )
    )
    client = Client(_mock_router(oidc))
    assert load_sso_token(load_sso_config(), client) == "refreshed-token"

    request = oidc.calls[0]
    assert request.url.host == "oidc.eu-west-1.amazonaws.com"
    assert "authorization" not in request.headers
    assert json.loads(request.body) == {
        "clientId": "client-id",
        "clientSecret": "client-secret",
        "grantType": "refresh_token",
        "refreshToken": "refresh-token",
    }
    # the refreshed token and rotated refresh token are written back to the cache
    stored = json.loads(target.read_text())
    assert stored["accessToken"] == "refreshed-token"
    assert stored["refreshToken"] == "next-refresh-token"
    assert parse_sso_expiry(stored["expiresAt"]) > datetime.now(timezone.utc)


def test_refresh_failure_falls_back_to_valid_token(tmp_path: Path) -> None:
    _session_profile(tmp_path)
    _write_token(
        tmp_path,
        "my-session",
        "still-valid",
        (datetime.now(timezone.utc) + timedelta(minutes=2)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        clientId="client-id",
        clientSecret="client-secret",
        refreshToken="refresh-token",
    )
    oidc = Mock.given(path("/token")).respond(
        Response(
            400,
            text=json.dumps({"error": "invalid_grant"}),
            headers={"x-amzn-errortype": "InvalidGrantException"},
        )
    )
    client = Client(_mock_router(oidc))
    assert load_sso_token(load_sso_config(), client) == "still-valid"


def test_expired_registration_is_not_refreshed(tmp_path: Path) -> None:
    _session_profile(tmp_path)
    _write_token(
        tmp_path,
        "my-session",
        "old",
        "2020-01-01T00:00:00Z",
        clientId="client-id",
        clientSecret="client-secret",
        refreshToken="refresh-token",
        registrationExpiresAt="2020-01-01T00:00:00Z",
    )
    oidc = Mock.given(path("/token")).respond(Response(200, text="{}"))
    with pytest.raises(SSOError, match="expired"):
        load_sso_token(load_sso_config(), Client(_mock_router(oidc)))
    oidc.assert_not_called()


def test_legacy_token_is_never_refreshed(tmp_path: Path) -> None:
    _legacy_profile(tmp_path)
    _write_token(
        tmp_path, "https://example.awsapps.com/start", "old", "2020-01-01T00:00:00Z"
    )
    oidc = Mock.given(path("/token")).respond(Response(200, text="{}"))
    with pytest.raises(SSOError, match="aws sso login"):
        load_sso_token(load_sso_config(), Client(_mock_router(oidc)))
    oidc.assert_not_called()


def test_chain_order_matches_aws() -> None:
    chain = default_aws_credentials_chain(Client())
    inner = chain._inner
    assert isinstance(inner, ChainedProvider)
    assert [type(p).__name__ for p in inner._providers] == [
        "EnvCredentialsProvider",
        "AssumeRoleCredentialsProvider",
        "WebIdentityCredentialsProvider",
        "SsoCredentialsProvider",
        "ProfileCredentialsProvider",
        "EcsContainerCredentialsProvider",
        "Ec2InstanceMetadataProvider",
    ]
