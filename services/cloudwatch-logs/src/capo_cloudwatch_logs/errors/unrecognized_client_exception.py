"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UnrecognizedClientException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.message


class UnrecognizedClientException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnrecognizedClientException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnrecognizedClientException_:
    out: UnrecognizedClientException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnrecognizedClientException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#UnrecognizedClientException``."""

    code: str | None = "UnrecognizedClientException"

    def __init__(
        self,
        data: UnrecognizedClientException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnrecognizedClientException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnrecognizedClientException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
