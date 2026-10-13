"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataMigrationSettings``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.secret_string


class DataMigrationSettings(TypedDict, closed=True):
    number_of_jobs: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.</p>"""
    cloudwatch_logs_enabled: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether to enable CloudWatch logging for the data migration.</p>"""
    selection_rules: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>A JSON-formatted string that defines what objects to include and exclude from the migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataMigrationSettings) -> dict:
    out: dict = {}
    if "number_of_jobs" in value:
        out["NumberOfJobs"] = value["number_of_jobs"]
    if "cloudwatch_logs_enabled" in value:
        out["CloudwatchLogsEnabled"] = value["cloudwatch_logs_enabled"]
    if "selection_rules" in value:
        out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataMigrationSettings:
    out: DataMigrationSettings = {}  # type: ignore[typeddict-item]
    if data.get("NumberOfJobs") is not None:
        out["number_of_jobs"] = data["NumberOfJobs"]
    if data.get("CloudwatchLogsEnabled") is not None:
        out["cloudwatch_logs_enabled"] = data["CloudwatchLogsEnabled"]
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    return out


def redact_sensitive(value: DataMigrationSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "selection_rules" in value:
        out["selection_rules"] = "*** Sensitive Data Redacted ***"
    return out
