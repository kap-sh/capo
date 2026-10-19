"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateTableObjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.transaction_id_string
    import capo_lakeformation.types.write_operation_list


class UpdateTableObjectsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The catalog containing the governed table to update. Defaults to the caller’s account ID.</p>"""
    database_name: "capo_lakeformation.types.name_string.NameString"
    """<p>The database containing the governed table to update.</p>"""
    table_name: "capo_lakeformation.types.name_string.NameString"
    """<p>The governed table to update.</p>"""
    transaction_id: NotRequired[
        "capo_lakeformation.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction at which to do the write.</p>"""
    write_operations: "capo_lakeformation.types.write_operation_list.WriteOperationList"
    """<p>A list of <code>WriteOperation</code> objects that define an object to add to or delete from the manifest for a governed table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableObjectsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    import capo_lakeformation.types.write_operation_list

    out["WriteOperations"] = (
        capo_lakeformation.types.write_operation_list.serialize_json(
            value["write_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTableObjectsRequest:
    out: UpdateTableObjectsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    if data.get("WriteOperations") is not None:
        import capo_lakeformation.types.write_operation_list

        out["write_operations"] = (
            capo_lakeformation.types.write_operation_list.deserialize_json(
                data["WriteOperations"]
            )
        )
    else:
        out["write_operations"] = []
    return out
