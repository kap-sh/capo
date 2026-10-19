"""Generated from Smithy shape ``com.amazonaws.glue#DeletePartitionIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string


class DeletePartitionIndexRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The catalog ID where the table resides.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>Specifies the name of a database from which you want to delete a partition index.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>Specifies the name of a table from which you want to delete a partition index.</p>"""
    index_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the partition index to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePartitionIndexRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["IndexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePartitionIndexRequest:
    out: DeletePartitionIndexRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    return out
