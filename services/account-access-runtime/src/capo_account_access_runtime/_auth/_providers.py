from __future__ import annotations

import json
from abc import abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import Generic, TypeVar

from capo_account_access_runtime._auth._identity import (
    BearerToken,
    Identity,
)


class IdentityNotFound(Exception):
    """Raised when a provider cannot resolve an identity. Chain continues."""


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


class BearerTokenProvider(IdentityProvider[BearerToken]):
    """Base class for providers that resolve a `BearerToken`."""

    @abstractmethod
    def resolve_identity(self) -> BearerToken:
        raise NotImplementedError


class StaticBearerTokenProvider(BearerTokenProvider):
    def __init__(self, token: str) -> None:
        self._token: BearerToken = {"token": token}

    def resolve_identity(self) -> BearerToken:
        return self._token


class SsoTokenCacheProvider(BearerTokenProvider):
    """Read a token cached by `aws sso login` from ~/.aws/sso/cache/."""

    def __init__(
        self, cache_dir: Path | None = None, session_name: str | None = None
    ) -> None:
        self._cache_dir = cache_dir or (Path.home() / ".aws" / "sso" / "cache")
        self._session_name = session_name

    def resolve_identity(self) -> BearerToken:
        if not self._cache_dir.is_dir():
            raise IdentityNotFound(f"SSO cache dir missing: {self._cache_dir}")

        entry = self._select_entry()
        if entry is None:
            raise IdentityNotFound("no usable SSO cache entry")

        token = entry.get("accessToken")
        if not isinstance(token, str) or not token:
            raise IdentityNotFound("SSO cache entry has no accessToken")

        out: BearerToken = {"token": token}
        exp = entry.get("expiresAt")
        if isinstance(exp, str):
            out["expiration"] = _parse_iso8601(exp)
        return out

    def _select_entry(self) -> dict[str, object] | None:
        candidates: list[tuple[float, dict[str, object]]] = []
        for path in self._cache_dir.glob("*.json"):
            try:
                data: dict[str, object] = json.loads(path.read_text())
            except (OSError, json.JSONDecodeError):
                continue
            if self._session_name and data.get("sessionName") != self._session_name:
                continue
            if "accessToken" not in data:
                continue
            candidates.append((path.stat().st_mtime, data))
        if not candidates:
            return None
        return max(candidates, key=lambda x: x[0])[1]


def _parse_iso8601(value: str) -> datetime:
    # tolerate trailing 'Z'
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def default_bearer_token_provider() -> IdentityProvider[BearerToken]:
    return CachedProvider(SsoTokenCacheProvider())
