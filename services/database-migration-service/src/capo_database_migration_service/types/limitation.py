"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Limitation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class Limitation(TypedDict, closed=True):
    database_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The identifier of the source database.</p>"""
    engine_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the target engine that Fleet Advisor should use in the target engine recommendation. Valid values include <code>"rds-aurora-mysql"</code>, <code>"rds-aurora-postgresql"</code>, <code>"rds-mysql"</code>, <code>"rds-oracle"</code>, <code>"rds-sql-server"</code>, and <code>"rds-postgresql"</code>.</p>"""
    name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the limitation. Describes unsupported database features, migration action items, and other limitations.</p>"""
    description: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A description of the limitation. Provides additional information about the limitation, and includes recommended actions that you can take to address or avoid this limitation.</p>"""
    impact: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The impact of the limitation. You can use this parameter to prioritize limitations that you want to address. Valid values include <code>"Blocker"</code>, <code>"High"</code>, <code>"Medium"</code>, and <code>"Low"</code>.</p>"""
    type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The type of the limitation, such as action required, upgrade required, and limited feature.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Limitation) -> dict:
    out: dict = {}
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "engine_name" in value:
        out["EngineName"] = value["engine_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "impact" in value:
        out["Impact"] = value["impact"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Limitation:
    out: Limitation = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseId") is not None:
        out["database_id"] = data["DatabaseId"]
    if data.get("EngineName") is not None:
        out["engine_name"] = data["EngineName"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Impact") is not None:
        out["impact"] = data["Impact"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
