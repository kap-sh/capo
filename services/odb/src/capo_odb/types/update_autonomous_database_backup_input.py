"""Generated from Smithy shape ``com.amazonaws.odb#UpdateAutonomousDatabaseBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class UpdateAutonomousDatabaseBackupInput(TypedDict, closed=True):
    autonomous_database_backup_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous Database backup to update.</p>"""
    retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for the Autonomous Database backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAutonomousDatabaseBackupInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseBackupId"] = value["autonomous_database_backup_id"]
    if "retention_period_in_days" in value:
        out["retentionPeriodInDays"] = value["retention_period_in_days"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAutonomousDatabaseBackupInput:
    out: UpdateAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseBackupId") is not None:
        out["autonomous_database_backup_id"] = data["autonomousDatabaseBackupId"]
    else:
        out["autonomous_database_backup_id"] = ""
    if data.get("retentionPeriodInDays") is not None:
        out["retention_period_in_days"] = data["retentionPeriodInDays"]
    return out
