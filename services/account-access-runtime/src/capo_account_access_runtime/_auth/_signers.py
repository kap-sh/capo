from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from zapros import Request

from capo_account_access_runtime._auth._identity import BearerToken, Identity
from capo_account_access_runtime._auth._providers import IdentityProvider

IdentityT = TypeVar("IdentityT", bound="Identity")


class Signer(ABC, Generic[IdentityT]):
    """Per-request request signer. Holds an IdentityProvider plus static config."""

    def __init__(self, provider: IdentityProvider[IdentityT]) -> None:
        self.provider = provider

    @abstractmethod
    async def asign(self, req: Request) -> Request: ...
    @abstractmethod
    def sign(self, req: Request) -> Request: ...


class HttpBearerSigner(Signer[BearerToken]):
    """smithy.api#httpBearerAuth — RFC 6750 ``Authorization: Bearer <token>``."""

    async def asign(self, req: Request) -> Request:
        t = await self.provider.aresolve_identity()
        headers = req.headers.copy()
        headers["Authorization"] = f"Bearer {t['token']}"
        return Request(
            req.url, req.method, headers, body=req.body or b"", context=req.context
        )

    def sign(self, req: Request) -> Request:
        t = self.provider.resolve_identity()
        headers = req.headers.copy()
        headers["Authorization"] = f"Bearer {t['token']}"
        return Request(
            req.url, req.method, headers, body=req.body or b"", context=req.context
        )
