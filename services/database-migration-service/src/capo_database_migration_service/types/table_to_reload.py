"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TableToReload``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class TableToReload(TypedDict, closed=True):
    schema_name: "capo_database_migration_service.types.string.String"
    """<p>The schema name of the table to be reloaded.</p>"""
    table_name: "capo_database_migration_service.types.string.String"
    """<p>The table name of the table to be reloaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableToReload) -> dict:
    out: dict = {}
    out["SchemaName"] = value["schema_name"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableToReload:
    out: TableToReload = {}  # type: ignore[typeddict-item]
    if data.get("SchemaName") is not None:
        out["schema_name"] = data["SchemaName"]
    else:
        out["schema_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    return out
