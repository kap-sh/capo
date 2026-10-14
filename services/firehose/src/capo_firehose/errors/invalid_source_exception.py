"""Generated from Smithy shape ``com.amazonaws.firehose#InvalidSourceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import ServiceError

if TYPE_CHECKING:
    import capo_firehose.types.error_code
    import capo_firehose.types.error_message


class InvalidSourceException_(TypedDict, closed=True):
    code: NotRequired["capo_firehose.types.error_code.ErrorCode"]
    message: NotRequired["capo_firehose.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidSourceException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidSourceException_:
    out: InvalidSourceException_ = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidSourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.firehose#InvalidSourceException``."""

    code: str | None = "InvalidSourceException"

    def __init__(
        self,
        data: InvalidSourceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSourceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidSourceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
