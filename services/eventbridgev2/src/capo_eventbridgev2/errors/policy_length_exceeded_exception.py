"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PolicyLengthExceededException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import ServiceError


class PolicyLengthExceededException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyLengthExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> PolicyLengthExceededException_:
    out: PolicyLengthExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class PolicyLengthExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eventbridgev2#PolicyLengthExceededException``."""

    code: str | None = "PolicyLengthExceededException"

    def __init__(
        self,
        data: PolicyLengthExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyLengthExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PolicyLengthExceededException":
        return cls(deserialize_cbor(data), message, response=response)
