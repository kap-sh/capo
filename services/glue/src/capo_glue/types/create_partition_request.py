"""Generated from Smithy shape ``com.amazonaws.glue#CreatePartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.partition_input


class CreatePartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The Amazon Web Services account ID of the catalog in which the partition is to be created.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the metadata database in which the partition is to be created.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the metadata table in which the partition is to be created.</p>"""
    partition_input: "capo_glue.types.partition_input.PartitionInput"
    """<p>A <code>PartitionInput</code> structure defining the partition to be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.partition_input

    out["PartitionInput"] = capo_glue.types.partition_input.serialize_aws_json_1_1(
        value["partition_input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartitionRequest:
    out: CreatePartitionRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("PartitionInput") is not None:
        import capo_glue.types.partition_input

        out["partition_input"] = (
            capo_glue.types.partition_input.deserialize_aws_json_1_1(
                data["PartitionInput"]
            )
        )
    else:
        raise DeserializationError("CreatePartitionRequest.partition_input required")
    return out
