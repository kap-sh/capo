"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InputValidationError``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime_http2.errors import ServiceError


class InputValidationError_(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>Error message.</p>"""
    error_code: NotRequired["str"]
    """<p>Error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputValidationError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> InputValidationError_:
    out: InputValidationError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    return out


class InputValidationError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InputValidationError``."""

    code: str | None = "InputValidationError"

    def __init__(
        self,
        data: InputValidationError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InputValidationError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InputValidationError":
        return cls(deserialize_json(data), message, response=response)
