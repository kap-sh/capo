"""Generated from Smithy shape ``com.amazonaws.datasync#InvalidRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import ServiceError

if TYPE_CHECKING:
    import capo_datasync.types.string


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_datasync.types.string.string"]
    error_code: NotRequired["capo_datasync.types.string.string"]
    datasync_error_code: NotRequired["capo_datasync.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "datasync_error_code" in value:
        out["datasyncErrorCode"] = value["datasync_error_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("datasyncErrorCode") is not None:
        out["datasync_error_code"] = data["datasyncErrorCode"]
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.datasync#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(
        self,
        data: InvalidRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidRequestException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
