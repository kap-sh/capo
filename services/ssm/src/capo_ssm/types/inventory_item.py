"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item_capture_time
    import capo_ssm.types.inventory_item_content_context
    import capo_ssm.types.inventory_item_content_hash
    import capo_ssm.types.inventory_item_entry_list
    import capo_ssm.types.inventory_item_schema_version
    import capo_ssm.types.inventory_item_type_name


class InventoryItem(TypedDict, closed=True):
    type_name: "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    """<p>The name of the inventory type. Default inventory item type names start with <code>AWS</code>. Custom inventory type names will start with Custom. Default inventory item types include the following: <code>AWS:AWSComponent</code>, <code>AWS:Application</code>, <code>AWS:InstanceInformation</code>, <code>AWS:Network</code>, and <code>AWS:WindowsUpdate</code>.</p>"""
    schema_version: (
        "capo_ssm.types.inventory_item_schema_version.InventoryItemSchemaVersion"
    )
    """<p>The schema version for the inventory item.</p>"""
    capture_time: "capo_ssm.types.inventory_item_capture_time.InventoryItemCaptureTime"
    """<p>The time the inventory information was collected.</p>"""
    content_hash: NotRequired[
        "capo_ssm.types.inventory_item_content_hash.InventoryItemContentHash"
    ]
    """<p>MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API doesn't update the inventory item type contents if the MD5 hash hasn't changed since last update. </p>"""
    content: NotRequired[
        "capo_ssm.types.inventory_item_entry_list.InventoryItemEntryList"
    ]
    """<p>The inventory data of the inventory type.</p>"""
    context: NotRequired[
        "capo_ssm.types.inventory_item_content_context.InventoryItemContentContext"
    ]
    """<p>A map of associated properties for a specified inventory type. For example, with this attribute, you can specify the <code>ExecutionId</code>, <code>ExecutionType</code>, <code>ComplianceType</code> properties of the <code>AWS:ComplianceItem</code> type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItem) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    out["SchemaVersion"] = value["schema_version"]
    out["CaptureTime"] = value["capture_time"]
    if "content_hash" in value:
        out["ContentHash"] = value["content_hash"]
    if "content" in value:
        import capo_ssm.types.inventory_item_entry_list

        out["Content"] = (
            capo_ssm.types.inventory_item_entry_list.serialize_aws_json_1_1(
                value["content"]
            )
        )
    if "context" in value:
        import capo_ssm.types.inventory_item_content_context

        out["Context"] = (
            capo_ssm.types.inventory_item_content_context.serialize_aws_json_1_1(
                value["context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryItem:
    out: InventoryItem = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    else:
        out["type_name"] = ""
    if data.get("SchemaVersion") is not None:
        out["schema_version"] = data["SchemaVersion"]
    else:
        out["schema_version"] = ""
    if data.get("CaptureTime") is not None:
        out["capture_time"] = data["CaptureTime"]
    else:
        out["capture_time"] = ""
    if data.get("ContentHash") is not None:
        out["content_hash"] = data["ContentHash"]
    if data.get("Content") is not None:
        import capo_ssm.types.inventory_item_entry_list

        out["content"] = (
            capo_ssm.types.inventory_item_entry_list.deserialize_aws_json_1_1(
                data["Content"]
            )
        )
    if data.get("Context") is not None:
        import capo_ssm.types.inventory_item_content_context

        out["context"] = (
            capo_ssm.types.inventory_item_content_context.deserialize_aws_json_1_1(
                data["Context"]
            )
        )
    return out
