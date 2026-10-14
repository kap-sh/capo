"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConditionalCheckFailedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_map
    import capo_dynamodb.types.error_message


class ConditionalCheckFailedException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]
    """<p>The conditional request failed.</p>"""
    item: NotRequired["capo_dynamodb.types.attribute_map.AttributeMap"]
    """<p>Item which caused the <code>ConditionalCheckFailedException</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionalCheckFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "item" in value:
        import capo_dynamodb.types.attribute_map

        out["Item"] = capo_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConditionalCheckFailedException_:
    out: ConditionalCheckFailedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("Item") is not None:
        import capo_dynamodb.types.attribute_map

        out["item"] = capo_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Item"]
        )
    return out


class ConditionalCheckFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ConditionalCheckFailedException``."""

    code: str | None = "ConditionalCheckFailedException"

    def __init__(
        self,
        data: ConditionalCheckFailedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConditionalCheckFailedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConditionalCheckFailedException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
