"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyDataMigrationMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.source_data_settings
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.target_data_settings


class ModifyDataMigrationMessage(TypedDict, closed=True):
    data_migration_identifier: "capo_database_migration_service.types.string.String"
    """<p>The identifier (name or ARN) of the data migration to modify.</p>"""
    data_migration_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The new name for the data migration.</p>"""
    enable_cloudwatch_logs: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether to enable Cloudwatch logs for the data migration.</p>"""
    service_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The new service access role ARN for the data migration.</p>"""
    data_migration_type: NotRequired[
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>The new migration type for the data migration.</p>"""
    source_data_settings: NotRequired[
        "capo_database_migration_service.types.source_data_settings.SourceDataSettings"
    ]
    """<p>The new information about the source data provider for the data migration.</p>"""
    target_data_settings: NotRequired[
        "capo_database_migration_service.types.target_data_settings.TargetDataSettings"
    ]
    """<p>The new information about the target data provider for the data migration.</p>"""
    number_of_jobs: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.</p>"""
    selection_rules: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>A JSON-formatted string that defines what objects to include and exclude from the migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyDataMigrationMessage) -> dict:
    out: dict = {}
    out["DataMigrationIdentifier"] = value["data_migration_identifier"]
    if "data_migration_name" in value:
        out["DataMigrationName"] = value["data_migration_name"]
    if "enable_cloudwatch_logs" in value:
        out["EnableCloudwatchLogs"] = value["enable_cloudwatch_logs"]
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "data_migration_type" in value:
        import capo_database_migration_service.types.migration_type_value

        out["DataMigrationType"] = (
            capo_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["data_migration_type"]
            )
        )
    if "source_data_settings" in value:
        import capo_database_migration_service.types.source_data_settings

        out["SourceDataSettings"] = (
            capo_database_migration_service.types.source_data_settings.serialize_aws_json_1_1(
                value["source_data_settings"]
            )
        )
    if "target_data_settings" in value:
        import capo_database_migration_service.types.target_data_settings

        out["TargetDataSettings"] = (
            capo_database_migration_service.types.target_data_settings.serialize_aws_json_1_1(
                value["target_data_settings"]
            )
        )
    if "number_of_jobs" in value:
        out["NumberOfJobs"] = value["number_of_jobs"]
    if "selection_rules" in value:
        out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyDataMigrationMessage:
    out: ModifyDataMigrationMessage = {}  # type: ignore[typeddict-item]
    if data.get("DataMigrationIdentifier") is not None:
        out["data_migration_identifier"] = data["DataMigrationIdentifier"]
    else:
        raise DeserializationError(
            "ModifyDataMigrationMessage.data_migration_identifier required"
        )
    if data.get("DataMigrationName") is not None:
        out["data_migration_name"] = data["DataMigrationName"]
    if data.get("EnableCloudwatchLogs") is not None:
        out["enable_cloudwatch_logs"] = data["EnableCloudwatchLogs"]
    if data.get("ServiceAccessRoleArn") is not None:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if data.get("DataMigrationType") is not None:
        import capo_database_migration_service.types.migration_type_value

        out["data_migration_type"] = (
            capo_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["DataMigrationType"]
            )
        )
    if data.get("SourceDataSettings") is not None:
        import capo_database_migration_service.types.source_data_settings

        out["source_data_settings"] = (
            capo_database_migration_service.types.source_data_settings.deserialize_aws_json_1_1(
                data["SourceDataSettings"]
            )
        )
    if data.get("TargetDataSettings") is not None:
        import capo_database_migration_service.types.target_data_settings

        out["target_data_settings"] = (
            capo_database_migration_service.types.target_data_settings.deserialize_aws_json_1_1(
                data["TargetDataSettings"]
            )
        )
    if data.get("NumberOfJobs") is not None:
        out["number_of_jobs"] = data["NumberOfJobs"]
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    return out


def redact_sensitive(value: ModifyDataMigrationMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "selection_rules" in value:
        out["selection_rules"] = "*** Sensitive Data Redacted ***"
    return out
