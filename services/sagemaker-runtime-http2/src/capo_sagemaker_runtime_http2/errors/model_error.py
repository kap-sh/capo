"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ModelError``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime_http2.errors import ServiceError


class ModelError_(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>Error message.</p>"""
    original_status_code: NotRequired["int"]
    """<p>HTTP status code returned by model.</p>"""
    original_message: NotRequired["str"]
    """<p>Original error message from the model.</p>"""
    log_stream_arn: NotRequired["str"]
    """<p>CloudWatch log stream ARN.</p>"""
    error_code: NotRequired["str"]
    """<p>Error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "original_status_code" in value:
        out["OriginalStatusCode"] = value["original_status_code"]
    if "original_message" in value:
        out["OriginalMessage"] = value["original_message"]
    if "log_stream_arn" in value:
        out["LogStreamArn"] = value["log_stream_arn"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> ModelError_:
    out: ModelError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("OriginalStatusCode") is not None:
        out["original_status_code"] = data["OriginalStatusCode"]
    if data.get("OriginalMessage") is not None:
        out["original_message"] = data["OriginalMessage"]
    if data.get("LogStreamArn") is not None:
        out["log_stream_arn"] = data["LogStreamArn"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    return out


class ModelError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ModelError``."""

    code: str | None = "ModelError"

    def __init__(
        self,
        data: ModelError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ModelError":
        return cls(deserialize_json(data), message, response=response)
