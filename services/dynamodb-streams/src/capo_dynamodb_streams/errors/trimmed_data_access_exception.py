"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#TrimmedDataAccessException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb_streams.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.error_message


class TrimmedDataAccessException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb_streams.types.error_message.ErrorMessage"]
    """<p>"The data you are trying to access has been trimmed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TrimmedDataAccessException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TrimmedDataAccessException_:
    out: TrimmedDataAccessException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TrimmedDataAccessException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodbstreams#TrimmedDataAccessException``."""

    code: str | None = "TrimmedDataAccessException"

    def __init__(self, data: TrimmedDataAccessException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TrimmedDataAccessException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "TrimmedDataAccessException":
        return cls(deserialize_aws_json_1_0(data), message)
