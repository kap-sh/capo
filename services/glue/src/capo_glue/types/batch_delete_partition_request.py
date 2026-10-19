"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeletePartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.batch_delete_partition_value_list
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string


class BatchDeletePartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database in which the table in question resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table that contains the partitions to be deleted.</p>"""
    partitions_to_delete: "capo_glue.types.batch_delete_partition_value_list.BatchDeletePartitionValueList"
    """<p>A list of <code>PartitionInput</code> structures that define the partitions to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeletePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.batch_delete_partition_value_list

    out["PartitionsToDelete"] = (
        capo_glue.types.batch_delete_partition_value_list.serialize_aws_json_1_1(
            value["partitions_to_delete"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeletePartitionRequest:
    out: BatchDeletePartitionRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("PartitionsToDelete") is not None:
        import capo_glue.types.batch_delete_partition_value_list

        out["partitions_to_delete"] = (
            capo_glue.types.batch_delete_partition_value_list.deserialize_aws_json_1_1(
                data["PartitionsToDelete"]
            )
        )
    else:
        out["partitions_to_delete"] = []
    return out
