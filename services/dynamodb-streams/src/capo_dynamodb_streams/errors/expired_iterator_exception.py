"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#ExpiredIteratorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dynamodb_streams.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.error_message


class ExpiredIteratorException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb_streams.types.error_message.ErrorMessage"]
    """<p>The provided iterator exceeds the maximum age allowed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpiredIteratorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpiredIteratorException_:
    out: ExpiredIteratorException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ExpiredIteratorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodbstreams#ExpiredIteratorException``."""

    code: str | None = "ExpiredIteratorException"

    def __init__(
        self,
        data: ExpiredIteratorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExpiredIteratorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ExpiredIteratorException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
