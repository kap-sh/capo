"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceCount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.long
    import capo_config_service.types.resource_type


class ResourceCount(TypedDict, closed=True):
    resource_type: NotRequired["capo_config_service.types.resource_type.ResourceType"]
    """<p>The resource type (for example, <code>"AWS::EC2::Instance"</code>).</p>"""
    count: "capo_config_service.types.long.Long"
    """<p>The number of resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCount) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_config_service.types.resource_type

        out["resourceType"] = (
            capo_config_service.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    out["count"] = value.get("count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceCount:
    out: ResourceCount = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_config_service.types.resource_type

        out["resource_type"] = (
            capo_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
