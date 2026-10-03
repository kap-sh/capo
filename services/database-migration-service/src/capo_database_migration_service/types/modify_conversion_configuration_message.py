"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyConversionConfigurationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.string


class ModifyConversionConfigurationMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    conversion_configuration: "capo_database_migration_service.types.string.String"
    """<p>A JSON string that contains the schema conversion settings to update. For the format and available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-settings.html">Specifying schema conversion settings for migration projects</a>.</p> <p>Usage:</p> <ul> <li> <p>Include only the sections and keys to change. The operation merges supplied values with the existing configuration.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyConversionConfigurationMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["ConversionConfiguration"] = value["conversion_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyConversionConfigurationMessage:
    out: ModifyConversionConfigurationMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "ModifyConversionConfigurationMessage.migration_project_identifier required"
        )
    if data.get("ConversionConfiguration") is not None:
        out["conversion_configuration"] = data["ConversionConfiguration"]
    else:
        raise DeserializationError(
            "ModifyConversionConfigurationMessage.conversion_configuration required"
        )
    return out
