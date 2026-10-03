"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteInventoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.inventory_deletion_summary
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.uuid


class DeleteInventoryResult(TypedDict, closed=True):
    deletion_id: NotRequired["capo_ssm.types.uuid.UUID"]
    """<p>Every <code>DeleteInventory</code> operation is assigned a unique ID. This option returns a unique ID. You can use this ID to query the status of a delete operation. This option is useful for ensuring that a delete operation has completed before you begin other operations. </p>"""
    type_name: NotRequired[
        "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    ]
    """<p>The name of the inventory data type specified in the request.</p>"""
    deletion_summary: NotRequired[
        "capo_ssm.types.inventory_deletion_summary.InventoryDeletionSummary"
    ]
    """<p>A summary of the delete operation. For more information about this summary, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-custom.html#delete-custom-inventory-summary">Deleting custom inventory</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInventoryResult) -> dict:
    out: dict = {}
    if "deletion_id" in value:
        out["DeletionId"] = value["deletion_id"]
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "deletion_summary" in value:
        import capo_ssm.types.inventory_deletion_summary

        out["DeletionSummary"] = (
            capo_ssm.types.inventory_deletion_summary.serialize_aws_json_1_1(
                value["deletion_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInventoryResult:
    out: DeleteInventoryResult = {}  # type: ignore[typeddict-item]
    if data.get("DeletionId") is not None:
        out["deletion_id"] = data["DeletionId"]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("DeletionSummary") is not None:
        import capo_ssm.types.inventory_deletion_summary

        out["deletion_summary"] = (
            capo_ssm.types.inventory_deletion_summary.deserialize_aws_json_1_1(
                data["DeletionSummary"]
            )
        )
    return out
