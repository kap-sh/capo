"""Generated from Smithy shape ``com.amazonaws.ssm#ItemContentMismatchException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.string


class ItemContentMismatchException_(TypedDict, closed=True):
    type_name: NotRequired[
        "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    ]
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ItemContentMismatchException_) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ItemContentMismatchException_:
    out: ItemContentMismatchException_ = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ItemContentMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ItemContentMismatchException``."""

    code: str | None = "ItemContentMismatchException"

    def __init__(
        self,
        data: ItemContentMismatchException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ItemContentMismatchException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ItemContentMismatchException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
