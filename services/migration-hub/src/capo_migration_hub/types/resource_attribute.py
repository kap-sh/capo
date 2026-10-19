"""Generated from Smithy shape ``com.amazonaws.migrationhub#ResourceAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.resource_attribute_type
    import capo_migration_hub.types.resource_attribute_value


class ResourceAttribute(TypedDict, closed=True):
    type: "capo_migration_hub.types.resource_attribute_type.ResourceAttributeType"
    """<p>Type of resource.</p>"""
    value: "capo_migration_hub.types.resource_attribute_value.ResourceAttributeValue"
    """<p>Value of the resource type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAttribute) -> dict:
    out: dict = {}
    import capo_migration_hub.types.resource_attribute_type

    out["Type"] = (
        capo_migration_hub.types.resource_attribute_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceAttribute:
    out: ResourceAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_migration_hub.types.resource_attribute_type

        out["type"] = (
            capo_migration_hub.types.resource_attribute_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_migration_hub.types.resource_attribute_type.ResourceAttributeType", ""
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
