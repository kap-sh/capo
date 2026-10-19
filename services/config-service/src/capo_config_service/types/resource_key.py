"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.resource_id
    import capo_config_service.types.resource_type


class ResourceKey(TypedDict, closed=True):
    resource_type: "capo_config_service.types.resource_type.ResourceType"
    """<p>The resource type.</p>"""
    resource_id: "capo_config_service.types.resource_id.ResourceId"
    """<p>The ID of the resource (for example., sg-xxxxxx). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceKey) -> dict:
    out: dict = {}
    import capo_config_service.types.resource_type

    out["resourceType"] = (
        capo_config_service.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    out["resourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceKey:
    out: ResourceKey = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_config_service.types.resource_type

        out["resource_type"] = (
            capo_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_config_service.types.resource_type.ResourceType", ""
        )
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    return out
