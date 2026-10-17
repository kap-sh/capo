from __future__ import annotations

import asyncio
import json
import shlex
import sys
from pathlib import Path

import pytest
from capo_securitylake._auth._providers import (
    CachedProvider,
    CredentialProcessError,
    Ec2InstanceMetadataProvider,
    EcsContainerCredentialsProvider,
    EnvCredentialsProvider,
    IdentityNotFound,
    ProcessCredentialsProvider,
    StaticAwsCredentialsProvider,
    _credentials_from_json,
    default_aws_credentials_chain,
)
from zapros import AsyncClient, Client, Response
from zapros.mock import Mock, MockMiddleware, MockRouter, path

_CREDS_JSON = json.dumps(
    {
        "AccessKeyId": "AKIA",
        "SecretAccessKey": "secret",
        "Token": "tok",
        "Expiration": "2030-01-01T00:00:00Z",
    }
)
_CLEARED_ENV = (
    "AWS_CONTAINER_CREDENTIALS_RELATIVE_URI",
    "AWS_CONTAINER_CREDENTIALS_FULL_URI",
    "AWS_CONTAINER_AUTHORIZATION_TOKEN",
    "AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE",
    "AWS_EC2_METADATA_DISABLED",
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_SESSION_TOKEN",
)


@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for var in _CLEARED_ENV:
        monkeypatch.delenv(var, raising=False)


def _mock_client(*mocks: Mock) -> Client:
    router = MockRouter()
    for m in mocks:
        router.add(m)
    return Client(MockMiddleware(router=router))


def _mock_async_client(*mocks: Mock) -> AsyncClient:
    router = MockRouter()
    for m in mocks:
        router.add(m)
    return AsyncClient(MockMiddleware(router=router))


def _process_profile(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    stdout: str,
    exit_code: int = 0,
    config_keys: str = "",
    credentials: str = "",
) -> None:
    script = tmp_path / "creds.py"
    script.write_text(
        f"import sys\nsys.stdout.write({stdout!r})\nsys.exit({exit_code})\n"
    )
    command = f"{shlex.quote(sys.executable)} {shlex.quote(str(script))}"
    config = tmp_path / "config"
    config.write_text(f"[profile proc]\ncredential_process = {command}\n{config_keys}")
    (tmp_path / "credentials").write_text(credentials)
    monkeypatch.setenv("AWS_CONFIG_FILE", str(config))
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", str(tmp_path / "credentials"))
    monkeypatch.setenv("AWS_PROFILE", "proc")


def test_static_provider() -> None:
    creds = {"access_key": "AK", "secret_key": "SK"}
    assert StaticAwsCredentialsProvider(creds).resolve_identity() == creds


def test_env_provider(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "AKENV")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "secretenv")
    monkeypatch.setenv("AWS_SESSION_TOKEN", "tokenv")
    creds = EnvCredentialsProvider().resolve_identity()
    assert creds["access_key"] == "AKENV"
    assert creds["secret_key"] == "secretenv"
    assert creds["session_token"] == "tokenv"


def test_env_provider_missing() -> None:
    with pytest.raises(IdentityNotFound):
        EnvCredentialsProvider().resolve_identity()


def test_credentials_from_json_full() -> None:
    out = _credentials_from_json(json.loads(_CREDS_JSON))
    assert out["access_key"] == "AKIA"
    assert out["secret_key"] == "secret"
    assert out["session_token"] == "tok"
    assert out["expiration"].year == 2030


def test_credentials_from_json_missing() -> None:
    with pytest.raises(IdentityNotFound):
        _credentials_from_json({"AccessKeyId": "AKIA"})


def test_ecs_relative_uri(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_CONTAINER_CREDENTIALS_RELATIVE_URI", "/creds")
    url, headers = EcsContainerCredentialsProvider(Client())._request_args()
    assert url == "http://169.254.170.2/creds"
    assert headers == {}


def test_ecs_full_uri_with_token(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_CONTAINER_CREDENTIALS_FULL_URI", "http://example/creds")
    monkeypatch.setenv("AWS_CONTAINER_AUTHORIZATION_TOKEN", "Bearer abc")
    url, headers = EcsContainerCredentialsProvider(Client())._request_args()
    assert url == "http://example/creds"
    assert headers["Authorization"] == "Bearer abc"


def test_ecs_token_from_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("AWS_CONTAINER_CREDENTIALS_FULL_URI", "http://example/creds")
    tok = tmp_path / "tok"
    tok.write_text("filetoken\n")
    monkeypatch.setenv("AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE", str(tok))
    _, headers = EcsContainerCredentialsProvider(Client())._request_args()
    assert headers["Authorization"] == "filetoken"


def test_ecs_no_env_raises() -> None:
    with pytest.raises(IdentityNotFound):
        EcsContainerCredentialsProvider(Client())._request_args()


def test_ecs_resolve_identity(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_CONTAINER_CREDENTIALS_FULL_URI", "http://example/creds")
    client = _mock_client(
        Mock.given(path("/creds")).respond(Response(200, text=_CREDS_JSON))
    )
    creds = EcsContainerCredentialsProvider(client).resolve_identity()
    assert creds["access_key"] == "AKIA"
    assert creds["session_token"] == "tok"


def test_ecs_resolve_identity_async(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_CONTAINER_CREDENTIALS_FULL_URI", "http://example/creds")

    async def run():
        client = _mock_async_client(
            Mock.given(path("/creds")).respond(Response(200, text=_CREDS_JSON))
        )
        return await EcsContainerCredentialsProvider(client).aresolve_identity()

    creds = asyncio.run(run())
    assert creds["access_key"] == "AKIA"


def test_imds_resolve_identity() -> None:
    client = _mock_client(
        Mock.given(path("/latest/api/token")).respond(Response(200, text="tok")),
        Mock.given(path("/latest/meta-data/iam/security-credentials/")).respond(
            Response(200, text="role")
        ),
        Mock.given(path("/latest/meta-data/iam/security-credentials/role")).respond(
            Response(200, text=_CREDS_JSON)
        ),
    )
    creds = Ec2InstanceMetadataProvider(client).resolve_identity()
    assert creds["access_key"] == "AKIA"


def test_imds_disabled(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_EC2_METADATA_DISABLED", "true")
    with pytest.raises(IdentityNotFound):
        Ec2InstanceMetadataProvider(Client()).resolve_identity()


def test_ecs_sync_method_with_async_client_raises() -> None:
    with pytest.raises(TypeError):
        EcsContainerCredentialsProvider(AsyncClient()).resolve_identity()


def test_imds_sync_method_with_async_client_raises() -> None:
    with pytest.raises(TypeError):
        Ec2InstanceMetadataProvider(AsyncClient()).resolve_identity()


def test_ecs_async_method_with_sync_client_raises() -> None:
    with pytest.raises(TypeError):
        asyncio.run(EcsContainerCredentialsProvider(Client()).aresolve_identity())


def test_chain_order_env_first(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "AKENV")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "secretenv")
    chain = default_aws_credentials_chain(Client())
    assert isinstance(chain, CachedProvider)
    assert chain.resolve_identity()["access_key"] == "AKENV"


def test_process_provider(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    printed = json.dumps(
        {
            "Version": 1,
            "AccessKeyId": "AKPROC",
            "SecretAccessKey": "secretproc",
            "SessionToken": "tokproc",
        }
    )
    _process_profile(tmp_path, monkeypatch, stdout=printed)
    creds = ProcessCredentialsProvider().resolve_identity()
    assert creds == {
        "access_key": "AKPROC",
        "secret_key": "secretproc",
        "session_token": "tokproc",
    }
    assert (
        default_aws_credentials_chain(Client()).resolve_identity()["access_key"]
        == "AKPROC"
    )


def test_process_provider_failure_stops_the_chain(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _process_profile(tmp_path, monkeypatch, stdout="", exit_code=1)
    with pytest.raises(CredentialProcessError):
        default_aws_credentials_chain(Client()).resolve_identity()


def test_credential_process_comes_before_config_file_keys(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _process_profile(
        tmp_path,
        monkeypatch,
        stdout=json.dumps(
            {"Version": 1, "AccessKeyId": "AKPROC", "SecretAccessKey": "secretproc"}
        ),
        config_keys="aws_access_key_id = AKCONFIG\naws_secret_access_key = secretconfig\n",
    )
    assert (
        default_aws_credentials_chain(Client()).resolve_identity()["access_key"]
        == "AKPROC"
    )


def test_credentials_file_keys_come_before_credential_process(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _process_profile(
        tmp_path,
        monkeypatch,
        stdout=json.dumps(
            {"Version": 1, "AccessKeyId": "AKPROC", "SecretAccessKey": "secretproc"}
        ),
        credentials="[proc]\naws_access_key_id = AKFILE\naws_secret_access_key = secretfile\n",
    )
    assert (
        default_aws_credentials_chain(Client()).resolve_identity()["access_key"]
        == "AKFILE"
    )
