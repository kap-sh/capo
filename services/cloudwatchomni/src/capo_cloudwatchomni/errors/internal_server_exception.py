"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#InternalServerException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import ServiceError


class InternalServerException_(TypedDict, closed=True):
    message: "str"
    error_code: NotRequired["str"]
    """The error code associated with the internal error."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_cbor(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchomni#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_cbor(data), message, response=response)
