"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#InternalException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import ServiceError


class InternalException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InternalException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> InternalException_:
    out: InternalException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eventbridgev2#InternalException``."""

    code: str | None = "InternalException"

    def __init__(
        self,
        data: InternalException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalException":
        return cls(deserialize_cbor(data), message, response=response)
