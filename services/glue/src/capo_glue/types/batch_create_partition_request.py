"""Generated from Smithy shape ``com.amazonaws.glue#BatchCreatePartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.partition_input_list


class BatchCreatePartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the catalog in which the partition is to be created. Currently, this should be the Amazon Web Services account ID.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the metadata database in which the partition is to be created.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the metadata table in which the partition is to be created.</p>"""
    partition_input_list: "capo_glue.types.partition_input_list.PartitionInputList"
    """<p>A list of <code>PartitionInput</code> structures that define the partitions to be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreatePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.partition_input_list

    out["PartitionInputList"] = (
        capo_glue.types.partition_input_list.serialize_aws_json_1_1(
            value["partition_input_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCreatePartitionRequest:
    out: BatchCreatePartitionRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("PartitionInputList") is not None:
        import capo_glue.types.partition_input_list

        out["partition_input_list"] = (
            capo_glue.types.partition_input_list.deserialize_aws_json_1_1(
                data["PartitionInputList"]
            )
        )
    else:
        out["partition_input_list"] = []
    return out
