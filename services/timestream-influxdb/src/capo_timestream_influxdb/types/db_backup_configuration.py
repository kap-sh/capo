"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbBackupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.automated_backup_retention_days
    import capo_timestream_influxdb.types.automated_db_backup_type
    import capo_timestream_influxdb.types.aws_cron_schedule


class DbBackupConfiguration(TypedDict, closed=True):
    type: (
        "capo_timestream_influxdb.types.automated_db_backup_type.AutomatedDbBackupType"
    )
    """<p>The type of automated backup schedule. Valid values are HOURLY, DAILY, WEEKLY, MONTHLY, CUSTOM_SCHEDULE, and CONTINUOUS.</p>"""
    retention_days: "capo_timestream_influxdb.types.automated_backup_retention_days.AutomatedBackupRetentionDays"
    """<p>The number of days to retain automated backups. Valid values are 1 to 365.</p>"""
    enabled: "bool"
    """<p>Specifies whether this backup configuration is enabled.</p>"""
    custom_schedule: NotRequired[
        "capo_timestream_influxdb.types.aws_cron_schedule.AwsCronSchedule"
    ]
    """<p>A custom cron schedule expression for the backup. Required when type is CUSTOM_SCHEDULE.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbBackupConfiguration) -> dict:
    out: dict = {}
    import capo_timestream_influxdb.types.automated_db_backup_type

    out["type"] = (
        capo_timestream_influxdb.types.automated_db_backup_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    out["retentionDays"] = value["retention_days"]
    out["enabled"] = value["enabled"]
    if "custom_schedule" in value:
        out["customSchedule"] = value["custom_schedule"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DbBackupConfiguration:
    out: DbBackupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_timestream_influxdb.types.automated_db_backup_type

        out["type"] = (
            capo_timestream_influxdb.types.automated_db_backup_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_timestream_influxdb.types.automated_db_backup_type.AutomatedDbBackupType",
            "",
        )
    if data.get("retentionDays") is not None:
        out["retention_days"] = data["retentionDays"]
    else:
        out["retention_days"] = 0
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("customSchedule") is not None:
        out["custom_schedule"] = data["customSchedule"]
    return out
