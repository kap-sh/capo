"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InternalServerError``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime_http2.errors import ServiceError


class InternalServerError_(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>Error message.</p>"""
    error_code: NotRequired["str"]
    """<p>Error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(
        self,
        data: InternalServerError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerError":
        return cls(deserialize_json(data), message, response=response)
