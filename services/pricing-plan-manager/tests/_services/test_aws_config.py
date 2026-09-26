from __future__ import annotations

import os
from pathlib import Path

import pytest
from capo_pricing_plan_manager._services._aws_config import (
    _env_bool,
    _load_profile,
    _profile_bool,
    load_aws_settings,
)


@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    for var in (
        "AWS_PROFILE",
        "AWS_DEFAULT_PROFILE",
        "AWS_CONFIG_FILE",
        "AWS_REGION",
        "AWS_ENDPOINT_URL",
        "AWS_ENDPOINT_URL_PRICING_PLAN_MANAGER",
        "AWS_USE_FIPS_ENDPOINT",
        "AWS_USE_DUALSTACK_ENDPOINT",
        "AWS_MAX_ATTEMPTS",
    ):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", str(tmp_path / "no_such_config"))
    load_aws_settings.cache_clear()


def write_config(tmp_path: Path, body: str, *, profile: str = "default") -> None:
    cfg = tmp_path / "config"
    cfg.write_text(body)
    os.environ["AWS_CONFIG_FILE"] = str(cfg)
    os.environ["AWS_PROFILE"] = profile
    load_aws_settings.cache_clear()


@pytest.mark.parametrize(
    "value, expected",
    [
        ("true", True),
        ("TRUE", True),
        ("1", True),
        ("  True  ", True),
        ("false", False),
        ("0", False),
        ("nonsense", False),
    ],
)
def test_env_bool_set(
    monkeypatch: pytest.MonkeyPatch, value: str, expected: bool
) -> None:
    monkeypatch.setenv("SOME_FLAG", value)
    assert _env_bool("SOME_FLAG") is expected


def test_env_bool_missing() -> None:
    assert _env_bool("DEFINITELY_UNSET_FLAG") is None


@pytest.mark.parametrize(
    "value, expected", [("true", True), ("1", True), ("false", False), ("no", False)]
)
def test_profile_bool_set(value: str, expected: bool) -> None:
    assert _profile_bool({"k": value}, "k") is expected


def test_profile_bool_missing() -> None:
    assert _profile_bool({}, "k") is None


def test_defaults_when_nothing_set() -> None:
    s = load_aws_settings()
    assert s.region is None
    assert s.endpoint is None
    assert s.use_fips is False
    assert s.use_dual_stack is False
    assert s.max_attempts == 3


def test_region_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_REGION", "us-west-2")
    assert load_aws_settings().region == "us-west-2"


def test_region_from_profile(tmp_path: Path) -> None:
    write_config(tmp_path, "[default]\nregion = eu-central-1\n")
    assert load_aws_settings().region == "eu-central-1"


def test_region_env_beats_profile(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    write_config(tmp_path, "[default]\nregion = eu-central-1\n")
    monkeypatch.setenv("AWS_REGION", "us-west-2")
    assert load_aws_settings().region == "us-west-2"


def test_named_profile_section(tmp_path: Path) -> None:
    write_config(
        tmp_path,
        "[default]\nregion = us-east-1\n\n[profile dev]\nregion = ap-south-1\n",
        profile="dev",
    )
    assert load_aws_settings().region == "ap-south-1"


def test_endpoint_service_env_beats_global_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_ENDPOINT_URL", "https://global.example")
    monkeypatch.setenv("AWS_ENDPOINT_URL_PRICING_PLAN_MANAGER", "https://svc.example")
    assert load_aws_settings().endpoint == "https://svc.example"


def test_endpoint_global_env_when_no_service_env(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("AWS_ENDPOINT_URL", "https://global.example")
    assert load_aws_settings().endpoint == "https://global.example"


def test_endpoint_from_services_block(tmp_path: Path) -> None:
    write_config(
        tmp_path,
        "[default]\nservices = local\n\n[services local]\npricing_plan_manager =\n  endpoint_url = https://localstack:4566\n",
    )
    assert load_aws_settings().endpoint == "https://localstack:4566"


def test_endpoint_from_profile(tmp_path: Path) -> None:
    write_config(tmp_path, "[default]\nendpoint_url = https://profile.example\n")
    assert load_aws_settings().endpoint == "https://profile.example"


def test_use_fips_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_USE_FIPS_ENDPOINT", "true")
    assert load_aws_settings().use_fips is True


def test_use_fips_from_profile(tmp_path: Path) -> None:
    write_config(tmp_path, "[default]\nuse_fips_endpoint = true\n")
    assert load_aws_settings().use_fips is True


def test_use_fips_env_beats_profile(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    write_config(tmp_path, "[default]\nuse_fips_endpoint = true\n")
    monkeypatch.setenv("AWS_USE_FIPS_ENDPOINT", "false")
    assert load_aws_settings().use_fips is False


def test_use_dual_stack_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_USE_DUALSTACK_ENDPOINT", "1")
    assert load_aws_settings().use_dual_stack is True


def test_max_attempts_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_MAX_ATTEMPTS", "7")
    assert load_aws_settings().max_attempts == 7


def test_max_attempts_from_profile(tmp_path: Path) -> None:
    write_config(tmp_path, "[default]\nmax_attempts = 5\n")
    assert load_aws_settings().max_attempts == 5


def test_max_attempts_env_beats_profile(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    write_config(tmp_path, "[default]\nmax_attempts = 5\n")
    monkeypatch.setenv("AWS_MAX_ATTEMPTS", "9")
    assert load_aws_settings().max_attempts == 9


def test_region_from_env_endpoint_from_profile(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    write_config(tmp_path, "[default]\nendpoint_url = https://profile.example\n")
    monkeypatch.setenv("AWS_REGION", "us-west-2")
    s = load_aws_settings()
    assert s.region == "us-west-2"
    assert s.endpoint == "https://profile.example"


def test_region_from_profile_max_attempts_from_env(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    write_config(tmp_path, "[default]\nregion = eu-central-1\nmax_attempts = 5\n")
    monkeypatch.setenv("AWS_MAX_ATTEMPTS", "9")
    s = load_aws_settings()
    assert s.region == "eu-central-1"
    assert s.max_attempts == 9


def test_fips_from_env_dualstack_from_profile(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    write_config(tmp_path, "[default]\nuse_dualstack_endpoint = true\n")
    monkeypatch.setenv("AWS_USE_FIPS_ENDPOINT", "true")
    s = load_aws_settings()
    assert s.use_fips is True
    assert s.use_dual_stack is True


def test_load_profile_parses_services_block(tmp_path: Path) -> None:
    write_config(
        tmp_path,
        "[default]\nregion = us-east-1\nservices = local\n\n[services local]\npricing_plan_manager =\n  endpoint_url = https://localstack:4566\n",
    )
    merged, services = _load_profile()
    assert merged["region"] == "us-east-1"
    assert services["pricing_plan_manager"]["endpoint_url"] == "https://localstack:4566"


def test_load_profile_missing_file_returns_empty() -> None:
    merged, services = _load_profile()
    assert merged == {}
    assert services == {}
