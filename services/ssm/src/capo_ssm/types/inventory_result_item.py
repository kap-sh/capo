"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item_capture_time
    import capo_ssm.types.inventory_item_content_hash
    import capo_ssm.types.inventory_item_entry_list
    import capo_ssm.types.inventory_item_schema_version
    import capo_ssm.types.inventory_item_type_name


class InventoryResultItem(TypedDict, closed=True):
    type_name: "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    """<p>The name of the inventory result item type.</p>"""
    schema_version: (
        "capo_ssm.types.inventory_item_schema_version.InventoryItemSchemaVersion"
    )
    """<p>The schema version for the inventory result item/</p>"""
    capture_time: NotRequired[
        "capo_ssm.types.inventory_item_capture_time.InventoryItemCaptureTime"
    ]
    """<p>The time inventory item data was captured.</p>"""
    content_hash: NotRequired[
        "capo_ssm.types.inventory_item_content_hash.InventoryItemContentHash"
    ]
    """<p>MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API doesn't update the inventory item type contents if the MD5 hash hasn't changed since last update. </p>"""
    content: "capo_ssm.types.inventory_item_entry_list.InventoryItemEntryList"
    """<p>Contains all the inventory data of the item type. Results include attribute names and values. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryResultItem) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    out["SchemaVersion"] = value["schema_version"]
    if "capture_time" in value:
        out["CaptureTime"] = value["capture_time"]
    if "content_hash" in value:
        out["ContentHash"] = value["content_hash"]
    import capo_ssm.types.inventory_item_entry_list

    out["Content"] = capo_ssm.types.inventory_item_entry_list.serialize_aws_json_1_1(
        value["content"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryResultItem:
    out: InventoryResultItem = {}  # type: ignore[typeddict-item]
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
    if data.get("ContentHash") is not None:
        out["content_hash"] = data["ContentHash"]
    if data.get("Content") is not None:
        import capo_ssm.types.inventory_item_entry_list

        out["content"] = (
            capo_ssm.types.inventory_item_entry_list.deserialize_aws_json_1_1(
                data["Content"]
            )
        )
    else:
        out["content"] = []
    return out
