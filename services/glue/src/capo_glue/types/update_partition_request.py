"""Generated from Smithy shape ``com.amazonaws.glue#UpdatePartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.bounded_partition_value_list
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.partition_input


class UpdatePartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partition to be updated resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database in which the table in question resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table in which the partition to be updated is located.</p>"""
    partition_value_list: (
        "capo_glue.types.bounded_partition_value_list.BoundedPartitionValueList"
    )
    """<p>List of partition key values that define the partition to update.</p>"""
    partition_input: "capo_glue.types.partition_input.PartitionInput"
    """<p>The new partition object to update the partition to.</p> <p>The <code>Values</code> property can't be changed. If you want to change the partition key values for a partition, delete and recreate the partition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.bounded_partition_value_list

    out["PartitionValueList"] = (
        capo_glue.types.bounded_partition_value_list.serialize_aws_json_1_1(
            value["partition_value_list"]
        )
    )
    import capo_glue.types.partition_input

    out["PartitionInput"] = capo_glue.types.partition_input.serialize_aws_json_1_1(
        value["partition_input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePartitionRequest:
    out: UpdatePartitionRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("PartitionValueList") is not None:
        import capo_glue.types.bounded_partition_value_list

        out["partition_value_list"] = (
            capo_glue.types.bounded_partition_value_list.deserialize_aws_json_1_1(
                data["PartitionValueList"]
            )
        )
    else:
        out["partition_value_list"] = []
    if data.get("PartitionInput") is not None:
        import capo_glue.types.partition_input

        out["partition_input"] = (
            capo_glue.types.partition_input.deserialize_aws_json_1_1(
                data["PartitionInput"]
            )
        )
    else:
        raise DeserializationError("UpdatePartitionRequest.partition_input required")
    return out
