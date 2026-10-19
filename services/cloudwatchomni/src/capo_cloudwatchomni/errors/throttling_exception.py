"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ThrottlingException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import ServiceError


class ThrottlingException_(TypedDict, closed=True):
    message: "str"
    retry_after_seconds: NotRequired["int"]
    """The number of seconds to wait before retrying the request. Not always present."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "retry_after_seconds" in value:
        out["retryAfterSeconds"] = value["retry_after_seconds"]
    return out


def deserialize_cbor(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("retryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["retryAfterSeconds"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchomni#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_cbor(data), message, response=response)
