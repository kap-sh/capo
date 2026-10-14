"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InvalidSequenceTokenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.message
    import capo_cloudwatch_logs.types.sequence_token


class InvalidSequenceTokenException_(TypedDict, closed=True):
    expected_sequence_token: NotRequired[
        "capo_cloudwatch_logs.types.sequence_token.SequenceToken"
    ]
    message: NotRequired["capo_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidSequenceTokenException_) -> dict:
    out: dict = {}
    if "expected_sequence_token" in value:
        out["expectedSequenceToken"] = value["expected_sequence_token"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidSequenceTokenException_:
    out: InvalidSequenceTokenException_ = {}  # type: ignore[typeddict-item]
    if data.get("expectedSequenceToken") is not None:
        out["expected_sequence_token"] = data["expectedSequenceToken"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidSequenceTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#InvalidSequenceTokenException``."""

    code: str | None = "InvalidSequenceTokenException"

    def __init__(
        self,
        data: InvalidSequenceTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSequenceTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidSequenceTokenException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
