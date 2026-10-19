"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CancelMetadataModelConversionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.string


class CancelMetadataModelConversionMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    request_identifier: "capo_database_migration_service.types.string.String"
    """<p>The identifier for the metadata model conversion operation to cancel. This operation was initiated by StartMetadataModelConversion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMetadataModelConversionMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["RequestIdentifier"] = value["request_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMetadataModelConversionMessage:
    out: CancelMetadataModelConversionMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        out["migration_project_identifier"] = ""
    if data.get("RequestIdentifier") is not None:
        out["request_identifier"] = data["RequestIdentifier"]
    else:
        out["request_identifier"] = ""
    return out
