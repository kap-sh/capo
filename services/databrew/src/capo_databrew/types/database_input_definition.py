"""Generated from Smithy shape ``com.amazonaws.databrew#DatabaseInputDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.database_table_name
    import capo_databrew.types.glue_connection_name
    import capo_databrew.types.query_string
    import capo_databrew.types.s3_location


class DatabaseInputDefinition(TypedDict, closed=True):
    glue_connection_name: "capo_databrew.types.glue_connection_name.GlueConnectionName"
    """<p>The Glue Connection that stores the connection information for the target database.</p>"""
    database_table_name: NotRequired[
        "capo_databrew.types.database_table_name.DatabaseTableName"
    ]
    """<p>The table within the target database.</p>"""
    temp_directory: NotRequired["capo_databrew.types.s3_location.S3Location"]
    query_string: NotRequired["capo_databrew.types.query_string.QueryString"]
    """<p>Custom SQL to run against the provided Glue connection. This SQL will be used as the input for DataBrew projects and jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseInputDefinition) -> dict:
    out: dict = {}
    out["GlueConnectionName"] = value["glue_connection_name"]
    if "database_table_name" in value:
        out["DatabaseTableName"] = value["database_table_name"]
    if "temp_directory" in value:
        import capo_databrew.types.s3_location

        out["TempDirectory"] = capo_databrew.types.s3_location.serialize_json(
            value["temp_directory"]
        )
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    return out


def deserialize_json(data: dict) -> DatabaseInputDefinition:
    out: DatabaseInputDefinition = {}  # type: ignore[typeddict-item]
    if data.get("GlueConnectionName") is not None:
        out["glue_connection_name"] = data["GlueConnectionName"]
    else:
        out["glue_connection_name"] = ""
    if data.get("DatabaseTableName") is not None:
        out["database_table_name"] = data["DatabaseTableName"]
    if data.get("TempDirectory") is not None:
        import capo_databrew.types.s3_location

        out["temp_directory"] = capo_databrew.types.s3_location.deserialize_json(
            data["TempDirectory"]
        )
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    return out
