"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#AccessDeniedException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import ServiceError


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eventbridgev2#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(
        self,
        data: AccessDeniedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccessDeniedException":
        return cls(deserialize_cbor(data), message, response=response)
