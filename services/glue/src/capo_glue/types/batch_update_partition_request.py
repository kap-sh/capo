"""Generated from Smithy shape ``com.amazonaws.glue#BatchUpdatePartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.batch_update_partition_request_entry_list
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string


class BatchUpdatePartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the catalog in which the partition is to be updated. Currently, this should be the Amazon Web Services account ID.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the metadata database in which the partition is to be updated.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the metadata table in which the partition is to be updated.</p>"""
    entries: "capo_glue.types.batch_update_partition_request_entry_list.BatchUpdatePartitionRequestEntryList"
    """<p>A list of up to 100 <code>BatchUpdatePartitionRequestEntry</code> objects to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdatePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.batch_update_partition_request_entry_list

    out["Entries"] = (
        capo_glue.types.batch_update_partition_request_entry_list.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdatePartitionRequest:
    out: BatchUpdatePartitionRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Entries") is not None:
        import capo_glue.types.batch_update_partition_request_entry_list

        out["entries"] = (
            capo_glue.types.batch_update_partition_request_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    return out
