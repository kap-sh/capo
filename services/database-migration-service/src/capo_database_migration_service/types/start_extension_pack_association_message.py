"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartExtensionPackAssociationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_project_identifier


class StartExtensionPackAssociationMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartExtensionPackAssociationMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartExtensionPackAssociationMessage:
    out: StartExtensionPackAssociationMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        out["migration_project_identifier"] = ""
    return out
