"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteMigrationProjectMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteMigrationProjectMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.string.String"
    """<p>The name or Amazon Resource Name (ARN) of the migration project to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMigrationProjectMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMigrationProjectMessage:
    out: DeleteMigrationProjectMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        out["migration_project_identifier"] = ""
    return out
