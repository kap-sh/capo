"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#PolicyTooLargeException``."""

import zapros
from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import ServiceError


class PolicyTooLargeException_(TypedDict, closed=True):
    message: "str"
    """A description of the error."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyTooLargeException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> PolicyTooLargeException_:
    out: PolicyTooLargeException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class PolicyTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchomni#PolicyTooLargeException``."""

    code: str | None = "PolicyTooLargeException"

    def __init__(
        self,
        data: PolicyTooLargeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyTooLargeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PolicyTooLargeException":
        return cls(deserialize_cbor(data), message, response=response)
