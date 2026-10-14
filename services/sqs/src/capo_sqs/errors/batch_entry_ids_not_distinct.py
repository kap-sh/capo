"""Generated from Smithy shape ``com.amazonaws.sqs#BatchEntryIdsNotDistinct``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import ServiceError

if TYPE_CHECKING:
    import capo_sqs.types.exception_message


class BatchEntryIdsNotDistinct_(TypedDict, closed=True):
    message: NotRequired["capo_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchEntryIdsNotDistinct_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchEntryIdsNotDistinct_:
    out: BatchEntryIdsNotDistinct_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class BatchEntryIdsNotDistinct(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#BatchEntryIdsNotDistinct``."""

    code: str | None = "BatchEntryIdsNotDistinct"

    def __init__(
        self,
        data: BatchEntryIdsNotDistinct_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BatchEntryIdsNotDistinct",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BatchEntryIdsNotDistinct":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
