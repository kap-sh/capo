"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_arn
    import capo_dynamodb.types.date
    import capo_dynamodb.types.restore_in_progress
    import capo_dynamodb.types.table_arn


class RestoreSummary(TypedDict, closed=True):
    source_backup_arn: NotRequired["capo_dynamodb.types.backup_arn.BackupArn"]
    """<p>The Amazon Resource Name (ARN) of the backup from which the table was restored.</p>"""
    source_table_arn: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>The ARN of the source table of the backup that is being restored.</p>"""
    restore_date_time: "capo_dynamodb.types.date.Date"
    """<p>Point in time or source backup time.</p>"""
    restore_in_progress: "capo_dynamodb.types.restore_in_progress.RestoreInProgress"
    """<p>Indicates if a restore is in progress or not.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreSummary) -> dict:
    out: dict = {}
    if "source_backup_arn" in value:
        out["SourceBackupArn"] = value["source_backup_arn"]
    if "source_table_arn" in value:
        out["SourceTableArn"] = value["source_table_arn"]
    import capo_dynamodb.types.date

    out["RestoreDateTime"] = capo_dynamodb.types.date.serialize_aws_json_1_0(
        value["restore_date_time"]
    )
    out["RestoreInProgress"] = value["restore_in_progress"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreSummary:
    out: RestoreSummary = {}  # type: ignore[typeddict-item]
    if data.get("SourceBackupArn") is not None:
        out["source_backup_arn"] = data["SourceBackupArn"]
    if data.get("SourceTableArn") is not None:
        out["source_table_arn"] = data["SourceTableArn"]
    if data.get("RestoreDateTime") is not None:
        import capo_dynamodb.types.date

        out["restore_date_time"] = capo_dynamodb.types.date.deserialize_aws_json_1_0(
            data["RestoreDateTime"]
        )
    else:
        import datetime

        out["restore_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("RestoreInProgress") is not None:
        out["restore_in_progress"] = data["RestoreInProgress"]
    else:
        out["restore_in_progress"] = False
    return out
