"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteResourceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.resource_id
    import capo_config_service.types.resource_type_string


class DeleteResourceConfigRequest(TypedDict, closed=True):
    resource_type: "capo_config_service.types.resource_type_string.ResourceTypeString"
    """<p>The type of the resource.</p>"""
    resource_id: "capo_config_service.types.resource_id.ResourceId"
    """<p>Unique identifier of the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourceConfigRequest) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourceConfigRequest:
    out: DeleteResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    return out
