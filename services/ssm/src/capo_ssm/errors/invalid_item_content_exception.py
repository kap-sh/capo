"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidItemContentException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.string


class InvalidItemContentException_(TypedDict, closed=True):
    type_name: NotRequired[
        "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    ]
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidItemContentException_) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidItemContentException_:
    out: InvalidItemContentException_ = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidItemContentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidItemContentException``."""

    code: str | None = "InvalidItemContentException"

    def __init__(
        self,
        data: InvalidItemContentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidItemContentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidItemContentException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
