from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from zapros import Request

from capo_glue._auth._identity import Credentials, Identity
from capo_glue._auth._providers import IdentityProvider
from capo_glue._auth._sigv4 import S3_SIGNING_NAMES, SigV4AuthContext, sign_sigv4

IdentityT = TypeVar("IdentityT", bound="Identity")


class Signer(ABC, Generic[IdentityT]):
    """Per-request request signer. Holds an IdentityProvider plus static config."""

    def __init__(self, provider: IdentityProvider[IdentityT]) -> None:
        self.provider = provider

    @abstractmethod
    async def asign(self, req: Request) -> Request: ...
    @abstractmethod
    def sign(self, req: Request) -> Request: ...


class SigV4Signer(Signer[Credentials]):
    """aws.auth#sigv4 — AWS Signature Version 4.

    The full auth scheme (``name`` variant, ``signingName``, ``signingRegion``,
    encoding/normalization flags) is provided by the caller — either from the
    endpoint rule-set's ``authSchemes`` property or built by the generated
    ``get_signer`` from operation defaults. ``unsigned_payload`` mirrors the
    operation's ``aws.auth#unsignedPayload`` trait: the body is sent but left
    out of the signature. ``event_stream`` marks a request event stream: the
    request is signed with the ``STREAMING-AWS4-HMAC-SHA256-EVENTS`` payload
    marker and every event with a signature chained from it.
    """

    def __init__(
        self,
        provider: IdentityProvider[Credentials],
        *,
        auth_scheme: dict[str, Any],
        unsigned_payload: bool = False,
        event_stream: bool = False,
    ) -> None:
        super().__init__(provider)
        self._auth_scheme = auth_scheme
        self._unsigned_payload = unsigned_payload
        self._event_stream = event_stream

    async def asign(self, req: Request) -> Request:
        creds = await self.provider.aresolve_identity()
        ctx: SigV4AuthContext = {
            "type": "sig_v4",
            "access_key_id": creds["access_key"],
            "secret_access_key": creds["secret_key"],
            "session_token": creds.get("session_token"),
            "signing_region": self._auth_scheme["signingRegion"],
            "signing_name": self._auth_scheme["signingName"],
            "disable_double_encoding": self._auth_scheme.get(
                "disableDoubleEncoding", False
            ),
            "disable_normalize_path": self._auth_scheme.get(
                "disableNormalizePath", False
            ),
        }
        unsigned_payload = self._unsigned_payload
        if (
            not unsigned_payload
            and not self._event_stream
            and req.body is not None
            and not isinstance(req.body, bytes)
        ):
            if self._auth_scheme["signingName"] in S3_SIGNING_NAMES:
                # S3 accepts UNSIGNED-PAYLOAD for any operation; streamed bodies rely on it.
                unsigned_payload = True
            else:
                raise NotImplementedError(
                    "Currently we don't support signed chunked payloads, so buffer the body and "
                    "pass bytes as a workaround; chunked signed implementation coming soon"
                )
        return sign_sigv4(
            req, ctx, unsigned_payload=unsigned_payload, event_stream=self._event_stream
        )

    def sign(self, req: Request) -> Request:
        creds = self.provider.resolve_identity()
        ctx: SigV4AuthContext = {
            "type": "sig_v4",
            "access_key_id": creds["access_key"],
            "secret_access_key": creds["secret_key"],
            "session_token": creds.get("session_token"),
            "signing_region": self._auth_scheme["signingRegion"],
            "signing_name": self._auth_scheme["signingName"],
            "disable_double_encoding": self._auth_scheme.get(
                "disableDoubleEncoding", False
            ),
            "disable_normalize_path": self._auth_scheme.get(
                "disableNormalizePath", False
            ),
        }
        unsigned_payload = self._unsigned_payload
        if (
            not unsigned_payload
            and not self._event_stream
            and req.body is not None
            and not isinstance(req.body, bytes)
        ):
            if self._auth_scheme["signingName"] in S3_SIGNING_NAMES:
                # S3 accepts UNSIGNED-PAYLOAD for any operation; streamed bodies rely on it.
                unsigned_payload = True
            else:
                raise NotImplementedError(
                    "Currently we don't support signed chunked payloads, so buffer the body and "
                    "pass bytes as a workaround; chunked signed implementation coming soon"
                )
        return sign_sigv4(
            req, ctx, unsigned_payload=unsigned_payload, event_stream=self._event_stream
        )
