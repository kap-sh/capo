from __future__ import annotations

import configparser
import functools
import os
from dataclasses import dataclass
from pathlib import Path
from typing import TypeVar

from capo_account_access._services._pipeline import (
    AsyncInterceptor,
    AsyncNextFn,
    AsyncOperationRequest,
    AsyncOperationResponse,
    Interceptor,
    NextFn,
    OperationRequest,
    OperationResponse,
)

ENDPOINT_ENV_VAR = "AWS_ENDPOINT_URL_ACCOUNT_ACCESS"
SERVICE_ID = "account_access"
TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


@dataclass(frozen=True)
class AwsSettings:
    region: str | None
    endpoint: str | None
    use_fips: bool
    use_dual_stack: bool
    max_attempts: int


def _env_bool(name: str) -> bool | None:
    val = os.environ.get(name)
    if val is None:
        return None
    return val.strip().lower() in ("true", "1")


def _profile_bool(section: dict[str, str], key: str) -> bool | None:
    val = section.get(key)
    if val is None:
        return None
    return val.strip().lower() in ("true", "1")


def config_file() -> Path:
    raw_cfg = os.environ.get("AWS_CONFIG_FILE")
    return Path(raw_cfg).expanduser() if raw_cfg else Path.home() / ".aws" / "config"


def active_profile() -> str:
    return (
        os.environ.get("AWS_PROFILE")
        or os.environ.get("AWS_DEFAULT_PROFILE")
        or "default"
    )


def _load_profile(
    profile: str | None = None,
) -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    profile = profile or active_profile()
    cfg_file = config_file()
    merged: dict[str, str] = {}
    services: dict[str, dict[str, str]] = {}
    if cfg_file.is_file():
        cfg = configparser.ConfigParser(interpolation=None)
        cfg.read(cfg_file)
        key = "default" if profile == "default" else f"profile {profile}"
        if cfg.has_section(key):
            merged.update(dict(cfg.items(key)))
        services_name = merged.get("services")
        if services_name and cfg.has_section(f"services {services_name}"):
            raw = dict(cfg.items(f"services {services_name}"))
            for svc, block in raw.items():
                parsed: dict[str, str] = {}
                for line in block.splitlines():
                    stripped = line.strip()
                    if "=" in stripped:
                        k, _, val = stripped.partition("=")
                        parsed[k.strip()] = val.strip()
                services[svc] = parsed
    return merged, services


@functools.cache
def load_aws_settings() -> AwsSettings:
    profile, services = _load_profile()
    region = os.environ.get("AWS_REGION") or profile.get("region")
    endpoint = (
        os.environ.get(ENDPOINT_ENV_VAR)
        or os.environ.get("AWS_ENDPOINT_URL")
        or services.get(SERVICE_ID, {}).get("endpoint_url")
        or profile.get("endpoint_url")
    )
    use_fips: bool | None = _env_bool("AWS_USE_FIPS_ENDPOINT")
    if use_fips is None:
        use_fips = _profile_bool(profile, "use_fips_endpoint")
    if use_fips is None:
        use_fips = False
    use_dual_stack: bool | None = _env_bool("AWS_USE_DUALSTACK_ENDPOINT")
    if use_dual_stack is None:
        use_dual_stack = _profile_bool(profile, "use_dualstack_endpoint")
    if use_dual_stack is None:
        use_dual_stack = False
    max_attempts_raw = os.environ.get("AWS_MAX_ATTEMPTS") or profile.get("max_attempts")
    max_attempts = int(max_attempts_raw) if max_attempts_raw else 3
    return AwsSettings(
        region=region,
        endpoint=endpoint,
        use_fips=use_fips,
        use_dual_stack=use_dual_stack,
        max_attempts=max_attempts,
    )


def aws_config() -> Interceptor[TInput, TOutput]:
    def interceptor(
        request: OperationRequest[TInput], next: NextFn[TInput, TOutput]
    ) -> OperationResponse[TOutput]:
        settings = load_aws_settings()
        options = request.options
        if options.region is None:
            options.region = settings.region
        if options.endpoint is None:
            options.endpoint = settings.endpoint
        if options.use_fips is None:
            options.use_fips = settings.use_fips
        if options.retry_max_attempts is None:
            options.retry_max_attempts = settings.max_attempts
        return next(request)

    return interceptor


def aaws_config() -> AsyncInterceptor[TInput, TOutput]:
    async def interceptor(
        request: AsyncOperationRequest[TInput], next: AsyncNextFn[TInput, TOutput]
    ) -> AsyncOperationResponse[TOutput]:
        settings = load_aws_settings()
        options = request.options
        if options.region is None:
            options.region = settings.region
        if options.endpoint is None:
            options.endpoint = settings.endpoint
        if options.use_fips is None:
            options.use_fips = settings.use_fips
        if options.retry_max_attempts is None:
            options.retry_max_attempts = settings.max_attempts
        return await next(request)

    return interceptor
