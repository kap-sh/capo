"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ProcessedObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class ProcessedObject(TypedDict, closed=True):
    name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the database object.</p>"""
    type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The type of the database object. For example, a table, view, procedure, and so on.</p>"""
    endpoint_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The type of the data provider. This parameter can store one of the following values: <code>"SOURCE"</code> or <code>"TARGET"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessedObject) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "endpoint_type" in value:
        out["EndpointType"] = value["endpoint_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessedObject:
    out: ProcessedObject = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("EndpointType") is not None:
        out["endpoint_type"] = data["EndpointType"]
    return out
