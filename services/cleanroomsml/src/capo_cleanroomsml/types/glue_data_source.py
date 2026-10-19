"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GlueDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.glue_database_name
    import capo_cleanroomsml.types.glue_table_name


class GlueDataSource(TypedDict, closed=True):
    table_name: "capo_cleanroomsml.types.glue_table_name.GlueTableName"
    """<p>The Glue table that contains the training data.</p>"""
    database_name: "capo_cleanroomsml.types.glue_database_name.GlueDatabaseName"
    """<p>The Glue database that contains the training data.</p>"""
    catalog_id: NotRequired["capo_cleanroomsml.types.account_id.AccountId"]
    """<p>The Glue catalog that contains the training data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueDataSource) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    out["databaseName"] = value["database_name"]
    if "catalog_id" in value:
        out["catalogId"] = value["catalog_id"]
    return out


def deserialize_json(data: dict) -> GlueDataSource:
    out: GlueDataSource = {}  # type: ignore[typeddict-item]
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        out["database_name"] = ""
    if data.get("catalogId") is not None:
        out["catalog_id"] = data["catalogId"]
    return out
