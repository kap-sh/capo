"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionSizeLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.error_message


class ItemCollectionSizeLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]
    """<p>The total size of an item collection has exceeded the maximum limit of 10 gigabytes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemCollectionSizeLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ItemCollectionSizeLimitExceededException_:
    out: ItemCollectionSizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ItemCollectionSizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ItemCollectionSizeLimitExceededException``."""

    code: str | None = "ItemCollectionSizeLimitExceededException"

    def __init__(
        self,
        data: ItemCollectionSizeLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ItemCollectionSizeLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ItemCollectionSizeLimitExceededException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
