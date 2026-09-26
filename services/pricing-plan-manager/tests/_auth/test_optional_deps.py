"""The sso extra is optional: providers that need it must fail loudly only when
the feature is actually configured, and stay out of the way otherwise."""

from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
from capo_pricing_plan_manager._auth import _providers
from capo_pricing_plan_manager._auth._providers import (
    AssumeRoleCredentialsProvider,
    IdentityNotFound,
    MissingDependencyError,
    SsoCredentialsProvider,
    WebIdentityCredentialsProvider,
    default_aws_credentials_chain,
)
from zapros import AsyncClient, Client

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
    "AWS_CONTAINER_CREDENTIALS_RELATIVE_URI",
    "AWS_CONTAINER_CREDENTIALS_FULL_URI",
)
_SSO_PROFILE = (
    "[default]\n"
    "sso_start_url = https://example.awsapps.com/start\n"
    "sso_region = us-east-1\n"
    "sso_account_id = 123456789012\n"
    "sso_role_name = ReadOnly\n"
)
_ROLE_PROFILE = (
    "[default]\n"
    "role_arn = arn:aws:iam::123456789012:role/Target\n"
    "source_profile = base\n"
    "\n"
    "[profile base]\n"
    "aws_access_key_id = AKBASE\n"
    "aws_secret_access_key = basesecret\n"
)


@pytest.fixture(autouse=True)
def uninstalled(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Pretend the sso extra was never installed."""
    for var in _CLEARED_ENV:
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("AWS_CONFIG_FILE", str(tmp_path / "config"))
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", str(tmp_path / "credentials"))
    monkeypatch.setenv("AWS_EC2_METADATA_DISABLED", "true")
    for name in ("capo_sso", "capo_sso_oidc", "capo_sts"):
        monkeypatch.setattr(_providers, name, None)


def _write_config(tmp_path: Path, body: str) -> None:
    (tmp_path / "config").write_text(body)


def test_sso_configured_reports_missing_extra(tmp_path: Path) -> None:
    _write_config(tmp_path, _SSO_PROFILE)
    with pytest.raises(
        MissingDependencyError, match=r"capo-pricing-plan-manager\[sso\]"
    ) as excinfo:
        SsoCredentialsProvider(Client()).resolve_identity()
    assert "capo-sso" in str(excinfo.value)


def test_sso_configured_reports_missing_extra_async(tmp_path: Path) -> None:
    _write_config(tmp_path, _SSO_PROFILE)
    with pytest.raises(
        MissingDependencyError, match=r"capo-pricing-plan-manager\[sso\]"
    ):
        asyncio.run(SsoCredentialsProvider(AsyncClient()).aresolve_identity())


def test_assume_role_configured_reports_missing_extra(tmp_path: Path) -> None:
    _write_config(tmp_path, _ROLE_PROFILE)
    with pytest.raises(
        MissingDependencyError, match=r"capo-pricing-plan-manager\[sso\]"
    ) as excinfo:
        AssumeRoleCredentialsProvider(Client()).resolve_identity()
    assert "capo-sts" in str(excinfo.value)


def test_web_identity_configured_reports_missing_extra(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    token_file = tmp_path / "token"
    token_file.write_text("oidc-token")
    monkeypatch.setenv("AWS_WEB_IDENTITY_TOKEN_FILE", str(token_file))
    monkeypatch.setenv("AWS_ROLE_ARN", "arn:aws:iam::123456789012:role/Irsa")
    with pytest.raises(
        MissingDependencyError, match=r"capo-pricing-plan-manager\[sso\]"
    ):
        WebIdentityCredentialsProvider(Client()).resolve_identity()


def test_unconfigured_providers_skip_without_extra(tmp_path: Path) -> None:
    """No sso/role config means these providers defer, extra installed or not."""
    _write_config(tmp_path, "[default]\nregion = us-east-1\n")
    client = Client()
    providers = (
        SsoCredentialsProvider(client),
        AssumeRoleCredentialsProvider(client),
        WebIdentityCredentialsProvider(client),
    )
    for provider in providers:
        with pytest.raises(IdentityNotFound):
            provider.resolve_identity()


def test_default_chain_still_works_without_extra(tmp_path: Path) -> None:
    """The base install must resolve static profile credentials as before."""
    _write_config(tmp_path, "[default]\nregion = us-east-1\n")
    (tmp_path / "credentials").write_text(
        "[default]\naws_access_key_id = AKPROFILE\naws_secret_access_key = secret\n"
    )
    creds = default_aws_credentials_chain(Client()).resolve_identity()
    assert creds["access_key"] == "AKPROFILE"
