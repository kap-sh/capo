"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_id
    import capo_ssm.types.ops_item_related_item_association_resource_uri
    import capo_ssm.types.string


class OpsItemRelatedItemAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]
    resource_uri: NotRequired[
        "capo_ssm.types.ops_item_related_item_association_resource_uri.OpsItemRelatedItemAssociationResourceUri"
    ]
    ops_item_id: NotRequired["capo_ssm.types.ops_item_id.OpsItemId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_uri" in value:
        out["ResourceUri"] = value["resource_uri"]
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemRelatedItemAlreadyExistsException_:
    out: OpsItemRelatedItemAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceUri") is not None:
        out["resource_uri"] = data["ResourceUri"]
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    return out


class OpsItemRelatedItemAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemAlreadyExistsException``."""

    code: str | None = "OpsItemRelatedItemAlreadyExistsException"

    def __init__(
        self,
        data: OpsItemRelatedItemAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsItemRelatedItemAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OpsItemRelatedItemAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
