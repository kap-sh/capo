"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbBackupConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_timestream_influxdb.types.automated_backup_retention_days
    import capo_timestream_influxdb.types.automated_db_backup_type
    import capo_timestream_influxdb.types.aws_cron_schedule


class DbBackupConfigurationOutput(TypedDict, closed=True):
    type: (
        "capo_timestream_influxdb.types.automated_db_backup_type.AutomatedDbBackupType"
    )
    """<p>The type of automated backup schedule.</p>"""
    retention_days: "capo_timestream_influxdb.types.automated_backup_retention_days.AutomatedBackupRetentionDays"
    """<p>The number of days automated backups are retained.</p>"""
    enabled: "bool"
    """<p>Indicates whether this backup configuration is enabled.</p>"""
    custom_schedule: NotRequired[
        "capo_timestream_influxdb.types.aws_cron_schedule.AwsCronSchedule"
    ]
    """<p>The custom cron schedule expression for the backup, if applicable.</p>"""
    next_automated_backup_time: NotRequired["datetime.datetime"]
    """<p>The next scheduled time for an automated backup to be taken.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbBackupConfigurationOutput) -> dict:
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
    if "next_automated_backup_time" in value:
        import capo_timestream_influxdb._protocol.serialize

        out["nextAutomatedBackupTime"] = (
            capo_timestream_influxdb._protocol.serialize.fmt_date_time(
                value["next_automated_backup_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DbBackupConfigurationOutput:
    out: DbBackupConfigurationOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("nextAutomatedBackupTime") is not None:
        import datetime

        out["next_automated_backup_time"] = datetime.datetime.fromisoformat(
            data["nextAutomatedBackupTime"].replace("Z", "+00:00")
        )
    return out
