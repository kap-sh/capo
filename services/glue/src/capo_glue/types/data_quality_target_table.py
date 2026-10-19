"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityTargetTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string


class DataQualityTargetTable(TypedDict, closed=True):
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the Glue table.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database where the Glue table exists.</p>"""
    catalog_id: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The catalog id where the Glue table exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityTargetTable) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    out["DatabaseName"] = value["database_name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityTargetTable:
    out: DataQualityTargetTable = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    return out
