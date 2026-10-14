"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ValidationException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError, ServiceError


class ValidationException_(TypedDict, closed=True):
    message: "str"
    error_code: NotRequired["str"]
    """The error code associated with the validation failure."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_cbor(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchomni#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(
        self,
        data: ValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_cbor(data), message, response=response)
