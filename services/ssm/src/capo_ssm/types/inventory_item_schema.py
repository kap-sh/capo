"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItemSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item_attribute_list
    import capo_ssm.types.inventory_item_schema_version
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.inventory_type_display_name


class InventoryItemSchema(TypedDict, closed=True):
    type_name: "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    """<p>The name of the inventory type. Default inventory item type names start with Amazon Web Services. Custom inventory type names will start with Custom. Default inventory item types include the following: <code>AWS:AWSComponent</code>, <code>AWS:Application</code>, <code>AWS:InstanceInformation</code>, <code>AWS:Network</code>, and <code>AWS:WindowsUpdate</code>.</p>"""
    version: NotRequired[
        "capo_ssm.types.inventory_item_schema_version.InventoryItemSchemaVersion"
    ]
    """<p>The schema version for the inventory item.</p>"""
    attributes: (
        "capo_ssm.types.inventory_item_attribute_list.InventoryItemAttributeList"
    )
    """<p>The schema attributes for inventory. This contains data type and attribute name.</p>"""
    display_name: NotRequired[
        "capo_ssm.types.inventory_type_display_name.InventoryTypeDisplayName"
    ]
    """<p>The alias name of the inventory type. The alias name is used for display purposes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItemSchema) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    if "version" in value:
        out["Version"] = value["version"]
    import capo_ssm.types.inventory_item_attribute_list

    out["Attributes"] = (
        capo_ssm.types.inventory_item_attribute_list.serialize_aws_json_1_1(
            value["attributes"]
        )
    )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryItemSchema:
    out: InventoryItemSchema = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    else:
        out["type_name"] = ""
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("Attributes") is not None:
        import capo_ssm.types.inventory_item_attribute_list

        out["attributes"] = (
            capo_ssm.types.inventory_item_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    else:
        out["attributes"] = []
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    return out
