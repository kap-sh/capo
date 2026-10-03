"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryDeletionStatusItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.inventory_deletion_last_status_message
    import capo_ssm.types.inventory_deletion_last_status_update_time
    import capo_ssm.types.inventory_deletion_start_time
    import capo_ssm.types.inventory_deletion_status
    import capo_ssm.types.inventory_deletion_summary
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.uuid


class InventoryDeletionStatusItem(TypedDict, closed=True):
    deletion_id: NotRequired["capo_ssm.types.uuid.UUID"]
    """<p>The deletion ID returned by the <code>DeleteInventory</code> operation.</p>"""
    type_name: NotRequired[
        "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    ]
    """<p>The name of the inventory data type.</p>"""
    deletion_start_time: NotRequired[
        "capo_ssm.types.inventory_deletion_start_time.InventoryDeletionStartTime"
    ]
    """<p>The UTC timestamp when the delete operation started.</p>"""
    last_status: NotRequired[
        "capo_ssm.types.inventory_deletion_status.InventoryDeletionStatus"
    ]
    """<p>The status of the operation. Possible values are InProgress and Complete.</p>"""
    last_status_message: NotRequired[
        "capo_ssm.types.inventory_deletion_last_status_message.InventoryDeletionLastStatusMessage"
    ]
    """<p>Information about the status.</p>"""
    deletion_summary: NotRequired[
        "capo_ssm.types.inventory_deletion_summary.InventoryDeletionSummary"
    ]
    """<p>Information about the delete operation. For more information about this summary, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-custom.html#delete-custom-inventory">Understanding the delete inventory summary</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    last_status_update_time: NotRequired[
        "capo_ssm.types.inventory_deletion_last_status_update_time.InventoryDeletionLastStatusUpdateTime"
    ]
    """<p>The UTC timestamp of when the last status report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryDeletionStatusItem) -> dict:
    out: dict = {}
    if "deletion_id" in value:
        out["DeletionId"] = value["deletion_id"]
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "deletion_start_time" in value:
        import capo_ssm.types.inventory_deletion_start_time

        out["DeletionStartTime"] = (
            capo_ssm.types.inventory_deletion_start_time.serialize_aws_json_1_1(
                value["deletion_start_time"]
            )
        )
    if "last_status" in value:
        import capo_ssm.types.inventory_deletion_status

        out["LastStatus"] = (
            capo_ssm.types.inventory_deletion_status.serialize_aws_json_1_1(
                value["last_status"]
            )
        )
    if "last_status_message" in value:
        out["LastStatusMessage"] = value["last_status_message"]
    if "deletion_summary" in value:
        import capo_ssm.types.inventory_deletion_summary

        out["DeletionSummary"] = (
            capo_ssm.types.inventory_deletion_summary.serialize_aws_json_1_1(
                value["deletion_summary"]
            )
        )
    if "last_status_update_time" in value:
        import capo_ssm.types.inventory_deletion_last_status_update_time

        out["LastStatusUpdateTime"] = (
            capo_ssm.types.inventory_deletion_last_status_update_time.serialize_aws_json_1_1(
                value["last_status_update_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryDeletionStatusItem:
    out: InventoryDeletionStatusItem = {}  # type: ignore[typeddict-item]
    if data.get("DeletionId") is not None:
        out["deletion_id"] = data["DeletionId"]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("DeletionStartTime") is not None:
        import capo_ssm.types.inventory_deletion_start_time

        out["deletion_start_time"] = (
            capo_ssm.types.inventory_deletion_start_time.deserialize_aws_json_1_1(
                data["DeletionStartTime"]
            )
        )
    if data.get("LastStatus") is not None:
        import capo_ssm.types.inventory_deletion_status

        out["last_status"] = (
            capo_ssm.types.inventory_deletion_status.deserialize_aws_json_1_1(
                data["LastStatus"]
            )
        )
    if data.get("LastStatusMessage") is not None:
        out["last_status_message"] = data["LastStatusMessage"]
    if data.get("DeletionSummary") is not None:
        import capo_ssm.types.inventory_deletion_summary

        out["deletion_summary"] = (
            capo_ssm.types.inventory_deletion_summary.deserialize_aws_json_1_1(
                data["DeletionSummary"]
            )
        )
    if data.get("LastStatusUpdateTime") is not None:
        import capo_ssm.types.inventory_deletion_last_status_update_time

        out["last_status_update_time"] = (
            capo_ssm.types.inventory_deletion_last_status_update_time.deserialize_aws_json_1_1(
                data["LastStatusUpdateTime"]
            )
        )
    return out
