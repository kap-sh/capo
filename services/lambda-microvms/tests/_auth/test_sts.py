from __future__ import annotations

import asyncio
import json
from pathlib import Path
from urllib.parse import parse_qs

import pytest
from capo_lambda_microvms._auth._providers import (
    AssumeRoleCredentialsProvider,
    AssumeRoleError,
    IdentityNotFound,
    WebIdentityCredentialsProvider,
)
from zapros import AsyncClient, Client, Response
from zapros.mock import Mock, MockMiddleware, MockRouter, host, path

_CLEARED_ENV = (
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_SESSION_TOKEN",
    "AWS_PROFILE",
    "AWS_DEFAULT_PROFILE",
    "AWS_REGION",
    "AWS_WEB_IDENTITY_TOKEN_FILE",
    "AWS_ROLE_ARN",
    "AWS_ROLE_SESSION_NAME",
)


def _sts_xml(action: str) -> str:
    return (
        f"<{action}Response><{action}Result><Credentials>"
        "<AccessKeyId>AKROLE</AccessKeyId>"
        "<SecretAccessKey>rolesecret</SecretAccessKey>"
        "<SessionToken>roletoken</SessionToken>"
        "<Expiration>2030-01-01T00:00:00Z</Expiration>"
        f"</Credentials></{action}Result></{action}Response>"
    )


@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    for var in _CLEARED_ENV:
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("AWS_CONFIG_FILE", str(tmp_path / "config"))
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", str(tmp_path / "credentials"))


def _write_config(tmp_path: Path, body: str) -> None:
    (tmp_path / "config").write_text(body)


def _mock_router(*mocks: Mock) -> MockMiddleware:
    router = MockRouter()
    for m in mocks:
        router.add(m)
    return MockMiddleware(router=router)


def _sts_mock(action: str = "AssumeRole") -> Mock:
    return Mock.given(host("sts.us-east-1.amazonaws.com")).respond(
        Response(200, text=_sts_xml(action))
    )


def _form(mock: Mock, index: int = 0) -> dict[str, str]:
    body = mock.calls[index].body
    assert isinstance(body, bytes)
    return {k: v[0] for k, v in parse_qs(body.decode(), strict_parsing=True).items()}


def test_assume_role_with_source_profile(tmp_path: Path) -> None:
    _write_config(
        tmp_path,
        "[default]\n"
        "role_arn = arn:aws:iam::123456789012:role/Target\n"
        "source_profile = base\n"
        "role_session_name = my-session\n"
        "external_id = ext-123\n"
        "region = us-east-1\n"
        "\n"
        "[profile base]\n"
        "aws_access_key_id = AKBASE\n"
        "aws_secret_access_key = basesecret\n",
    )
    sts = _sts_mock()
    creds = AssumeRoleCredentialsProvider(Client(_mock_router(sts))).resolve_identity()
    assert creds["access_key"] == "AKROLE"
    assert creds["secret_key"] == "rolesecret"
    assert creds["session_token"] == "roletoken"
    assert creds["expiration"].year == 2030

    form = _form(sts)
    assert form["Action"] == "AssumeRole"
    assert form["RoleArn"] == "arn:aws:iam::123456789012:role/Target"
    assert form["RoleSessionName"] == "my-session"
    assert form["ExternalId"] == "ext-123"
    # the call itself is signed with the source profile's credentials
    assert "Credential=AKBASE/" in sts.calls[0].headers["authorization"]


def test_assume_role_chaining(tmp_path: Path) -> None:
    _write_config(
        tmp_path,
        "[default]\n"
        "role_arn = arn:aws:iam::123456789012:role/Second\n"
        "source_profile = middle\n"
        "\n"
        "[profile middle]\n"
        "role_arn = arn:aws:iam::123456789012:role/First\n"
        "source_profile = base\n"
        "\n"
        "[profile base]\n"
        "aws_access_key_id = AKBASE\n"
        "aws_secret_access_key = basesecret\n",
    )
    sts = _sts_mock()
    creds = AssumeRoleCredentialsProvider(Client(_mock_router(sts))).resolve_identity()
    assert creds["access_key"] == "AKROLE"
    # inner role assumed first, then the outer one
    assert sts.call_count == 2
    assert _form(sts, 0)["RoleArn"] == "arn:aws:iam::123456789012:role/First"
    assert _form(sts, 1)["RoleArn"] == "arn:aws:iam::123456789012:role/Second"


def test_assume_role_circular_source_profile(tmp_path: Path) -> None:
    _write_config(
        tmp_path,
        "[default]\n"
        "role_arn = arn:aws:iam::123456789012:role/A\n"
        "source_profile = loop\n"
        "\n"
        "[profile loop]\n"
        "role_arn = arn:aws:iam::123456789012:role/B\n"
        "source_profile = loop\n",
    )
    with pytest.raises(AssumeRoleError, match="circular"):
        AssumeRoleCredentialsProvider(Client()).resolve_identity()


def test_assume_role_credential_source_environment(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "AKENV")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "envsecret")
    _write_config(
        tmp_path,
        "[default]\n"
        "role_arn = arn:aws:iam::123456789012:role/Target\n"
        "credential_source = Environment\n",
    )
    sts = _sts_mock()
    creds = AssumeRoleCredentialsProvider(Client(_mock_router(sts))).resolve_identity()
    assert creds["access_key"] == "AKROLE"
    assert "Credential=AKENV/" in sts.calls[0].headers["authorization"]


def test_assume_role_source_from_sso_profile(tmp_path: Path) -> None:
    """An SSO profile can be the source_profile for an assumed role."""
    _write_config(
        tmp_path,
        "[default]\n"
        "role_arn = arn:aws:iam::123456789012:role/Target\n"
        "source_profile = sso-base\n"
        "\n"
        "[profile sso-base]\n"
        "sso_start_url = https://example.awsapps.com/start\n"
        "sso_region = us-east-1\n"
        "sso_account_id = 123456789012\n"
        "sso_role_name = ReadOnly\n",
    )
    import hashlib

    cache = tmp_path / ".aws" / "sso" / "cache"
    cache.mkdir(parents=True)
    digest = hashlib.sha1(b"https://example.awsapps.com/start").hexdigest()
    (cache / f"{digest}.json").write_text(
        json.dumps({"accessToken": "sso-token", "expiresAt": "2030-01-01T00:00:00Z"})
    )
    sso = Mock.given(
        path("/federation/credentials")
    ).respond(
        Response(
            200,
            text=json.dumps(
                {
                    "roleCredentials": {
                        "accessKeyId": "AKSSO",
                        "secretAccessKey": "ssosecret",
                        "sessionToken": "ssotoken",
                        "expiration": 1893456000000,  # 2030-01-01T00:00:00Z in epoch millis
                    }
                }
            ),
        )
    )
    sts = _sts_mock()
    creds = AssumeRoleCredentialsProvider(
        Client(_mock_router(sso, sts))
    ).resolve_identity()
    assert creds["access_key"] == "AKROLE"
    # the AssumeRole call is signed with the credentials SSO handed back
    assert "Credential=AKSSO/" in sts.calls[0].headers["authorization"]


def test_assume_role_without_source_is_skipped(tmp_path: Path) -> None:
    _write_config(
        tmp_path, "[default]\nrole_arn = arn:aws:iam::123456789012:role/Target\n"
    )
    with pytest.raises(IdentityNotFound):
        AssumeRoleCredentialsProvider(Client()).resolve_identity()


def test_assume_role_mfa_serial_unsupported(tmp_path: Path) -> None:
    _write_config(
        tmp_path,
        "[default]\n"
        "role_arn = arn:aws:iam::123456789012:role/Target\n"
        "source_profile = base\n"
        "mfa_serial = arn:aws:iam::123456789012:mfa/user\n",
    )
    with pytest.raises(AssumeRoleError, match="mfa_serial"):
        AssumeRoleCredentialsProvider(Client()).resolve_identity()


def test_assume_role_no_role_arn(tmp_path: Path) -> None:
    _write_config(tmp_path, "[default]\nregion = us-east-1\n")
    with pytest.raises(IdentityNotFound, match="role_arn"):
        AssumeRoleCredentialsProvider(Client()).resolve_identity()


def test_web_identity_from_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    token_file = tmp_path / "token"
    token_file.write_text("oidc-token\n")
    monkeypatch.setenv("AWS_WEB_IDENTITY_TOKEN_FILE", str(token_file))
    monkeypatch.setenv("AWS_ROLE_ARN", "arn:aws:iam::123456789012:role/Irsa")
    monkeypatch.setenv("AWS_ROLE_SESSION_NAME", "pod-session")
    sts = _sts_mock("AssumeRoleWithWebIdentity")
    creds = WebIdentityCredentialsProvider(Client(_mock_router(sts))).resolve_identity()
    assert creds["access_key"] == "AKROLE"

    form = _form(sts)
    assert form["Action"] == "AssumeRoleWithWebIdentity"
    assert form["RoleArn"] == "arn:aws:iam::123456789012:role/Irsa"
    assert form["RoleSessionName"] == "pod-session"
    assert form["WebIdentityToken"] == "oidc-token"
    # AssumeRoleWithWebIdentity takes no credentials, so it must go out unsigned
    assert "authorization" not in sts.calls[0].headers


def test_web_identity_from_profile(tmp_path: Path) -> None:
    token_file = tmp_path / "token"
    token_file.write_text("profile-oidc-token")
    _write_config(
        tmp_path,
        "[default]\n"
        f"web_identity_token_file = {token_file}\n"
        "role_arn = arn:aws:iam::123456789012:role/Irsa\n",
    )
    sts = _sts_mock("AssumeRoleWithWebIdentity")
    creds = WebIdentityCredentialsProvider(Client(_mock_router(sts))).resolve_identity()
    assert creds["access_key"] == "AKROLE"
    assert _form(sts)["WebIdentityToken"] == "profile-oidc-token"


def test_web_identity_async(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    token_file = tmp_path / "token"
    token_file.write_text("oidc-token")
    monkeypatch.setenv("AWS_WEB_IDENTITY_TOKEN_FILE", str(token_file))
    monkeypatch.setenv("AWS_ROLE_ARN", "arn:aws:iam::123456789012:role/Irsa")
    sts = _sts_mock("AssumeRoleWithWebIdentity")

    async def run():
        return await WebIdentityCredentialsProvider(
            AsyncClient(_mock_router(sts))
        ).aresolve_identity()

    assert asyncio.run(run())["access_key"] == "AKROLE"


def test_web_identity_not_configured(tmp_path: Path) -> None:
    _write_config(tmp_path, "[default]\nregion = us-east-1\n")
    with pytest.raises(IdentityNotFound):
        WebIdentityCredentialsProvider(Client()).resolve_identity()


def test_web_identity_missing_token_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("AWS_WEB_IDENTITY_TOKEN_FILE", str(tmp_path / "absent"))
    monkeypatch.setenv("AWS_ROLE_ARN", "arn:aws:iam::123456789012:role/Irsa")
    with pytest.raises(AssumeRoleError, match="does not exist"):
        WebIdentityCredentialsProvider(Client()).resolve_identity()


def test_sync_method_with_async_client_raises() -> None:
    with pytest.raises(TypeError):
        AssumeRoleCredentialsProvider(AsyncClient()).resolve_identity()
    with pytest.raises(TypeError):
        WebIdentityCredentialsProvider(AsyncClient()).resolve_identity()


def test_async_method_with_sync_client_raises() -> None:
    with pytest.raises(TypeError):
        asyncio.run(AssumeRoleCredentialsProvider(Client()).aresolve_identity())
    with pytest.raises(TypeError):
        asyncio.run(WebIdentityCredentialsProvider(Client()).aresolve_identity())
