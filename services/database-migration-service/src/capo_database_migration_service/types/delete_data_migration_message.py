"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteDataMigrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteDataMigrationMessage(TypedDict, closed=True):
    data_migration_identifier: "capo_database_migration_service.types.string.String"
    """<p>The identifier (name or ARN) of the data migration to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataMigrationMessage) -> dict:
    out: dict = {}
    out["DataMigrationIdentifier"] = value["data_migration_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataMigrationMessage:
    out: DeleteDataMigrationMessage = {}  # type: ignore[typeddict-item]
    if data.get("DataMigrationIdentifier") is not None:
        out["data_migration_identifier"] = data["DataMigrationIdentifier"]
    else:
        out["data_migration_identifier"] = ""
    return out
