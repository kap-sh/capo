"""Generated from Smithy shape ``com.amazonaws.sqs#TooManyEntriesInBatchRequest``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import ServiceError

if TYPE_CHECKING:
    import capo_sqs.types.exception_message


class TooManyEntriesInBatchRequest_(TypedDict, closed=True):
    message: NotRequired["capo_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TooManyEntriesInBatchRequest_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TooManyEntriesInBatchRequest_:
    out: TooManyEntriesInBatchRequest_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TooManyEntriesInBatchRequest(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#TooManyEntriesInBatchRequest``."""

    code: str | None = "TooManyEntriesInBatchRequest"

    def __init__(
        self,
        data: TooManyEntriesInBatchRequest_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyEntriesInBatchRequest",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyEntriesInBatchRequest":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
