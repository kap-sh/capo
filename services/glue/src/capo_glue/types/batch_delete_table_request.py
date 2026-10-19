"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeleteTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.batch_delete_table_name_list
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.transaction_id_string


class BatchDeleteTableRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database in which the tables to delete reside. For Hive compatibility, this name is entirely lowercase.</p>"""
    tables_to_delete: (
        "capo_glue.types.batch_delete_table_name_list.BatchDeleteTableNameList"
    )
    """<p>A list of the table to delete.</p>"""
    transaction_id: NotRequired[
        "capo_glue.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to delete the table contents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    import capo_glue.types.batch_delete_table_name_list

    out["TablesToDelete"] = (
        capo_glue.types.batch_delete_table_name_list.serialize_aws_json_1_1(
            value["tables_to_delete"]
        )
    )
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteTableRequest:
    out: BatchDeleteTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TablesToDelete") is not None:
        import capo_glue.types.batch_delete_table_name_list

        out["tables_to_delete"] = (
            capo_glue.types.batch_delete_table_name_list.deserialize_aws_json_1_1(
                data["TablesToDelete"]
            )
        )
    else:
        out["tables_to_delete"] = []
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    return out
