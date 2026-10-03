"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeConversionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DescribeConversionConfigurationResponse(TypedDict, closed=True):
    migration_project_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the schema conversion project.</p>"""
    conversion_configuration: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A JSON string that contains the schema conversion settings for the migration project. For the format and available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-settings.html">Specifying schema conversion settings for migration projects</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConversionConfigurationResponse) -> dict:
    out: dict = {}
    if "migration_project_identifier" in value:
        out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    if "conversion_configuration" in value:
        out["ConversionConfiguration"] = value["conversion_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConversionConfigurationResponse:
    out: DescribeConversionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    if data.get("ConversionConfiguration") is not None:
        out["conversion_configuration"] = data["ConversionConfiguration"]
    return out
