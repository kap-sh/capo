"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeleteObjectsOnCancelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.transaction_id_string
    import capo_lakeformation.types.virtual_object_list


class DeleteObjectsOnCancelRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The Glue data catalog that contains the governed table. Defaults to the current account ID.</p>"""
    database_name: "capo_lakeformation.types.name_string.NameString"
    """<p>The database that contains the governed table.</p>"""
    table_name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the governed table.</p>"""
    transaction_id: "capo_lakeformation.types.transaction_id_string.TransactionIdString"
    """<p>ID of the transaction that the writes occur in.</p>"""
    objects: "capo_lakeformation.types.virtual_object_list.VirtualObjectList"
    """<p>A list of VirtualObject structures, which indicates the Amazon S3 objects to be deleted if the transaction cancels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteObjectsOnCancelRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["TransactionId"] = value["transaction_id"]
    import capo_lakeformation.types.virtual_object_list

    out["Objects"] = capo_lakeformation.types.virtual_object_list.serialize_json(
        value["objects"]
    )
    return out


def deserialize_json(data: dict) -> DeleteObjectsOnCancelRequest:
    out: DeleteObjectsOnCancelRequest = {}  # type: ignore[typeddict-item]
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
    else:
        out["transaction_id"] = ""
    if data.get("Objects") is not None:
        import capo_lakeformation.types.virtual_object_list

        out["objects"] = capo_lakeformation.types.virtual_object_list.deserialize_json(
            data["Objects"]
        )
    else:
        out["objects"] = []
    return out
