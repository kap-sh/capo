"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteInventoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.dry_run
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.inventory_schema_delete_option
    import capo_ssm.types.uuid


class DeleteInventoryRequest(TypedDict, closed=True):
    type_name: "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    """<p>The name of the custom inventory type for which you want to delete either all previously collected data or the inventory type itself. </p>"""
    schema_delete_option: NotRequired[
        "capo_ssm.types.inventory_schema_delete_option.InventorySchemaDeleteOption"
    ]
    """<p>Use the <code>SchemaDeleteOption</code> to delete a custom inventory type (schema). If you don't choose this option, the system only deletes existing inventory data associated with the custom inventory type. Choose one of the following options:</p> <p>DisableSchema: If you choose this option, the system ignores all inventory data for the specified version, and any earlier versions. To enable this schema again, you must call the <code>PutInventory</code> operation for a version greater than the disabled version.</p> <p>DeleteSchema: This option deletes the specified custom type from the Inventory service. You can recreate the schema later, if you want.</p>"""
    dry_run: NotRequired["capo_ssm.types.dry_run.DryRun"]
    """<p>Use this option to view a summary of the deletion request without deleting any data or the data type. This option is useful when you only want to understand what will be deleted. Once you validate that the data to be deleted is what you intend to delete, you can run the same command without specifying the <code>DryRun</code> option.</p>"""
    client_token: NotRequired["capo_ssm.types.uuid.UUID"]
    """<p>User-provided idempotency token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInventoryRequest) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    if "schema_delete_option" in value:
        import capo_ssm.types.inventory_schema_delete_option

        out["SchemaDeleteOption"] = (
            capo_ssm.types.inventory_schema_delete_option.serialize_aws_json_1_1(
                value["schema_delete_option"]
            )
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInventoryRequest:
    out: DeleteInventoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    else:
        out["type_name"] = ""
    if data.get("SchemaDeleteOption") is not None:
        import capo_ssm.types.inventory_schema_delete_option

        out["schema_delete_option"] = (
            capo_ssm.types.inventory_schema_delete_option.deserialize_aws_json_1_1(
                data["SchemaDeleteOption"]
            )
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
