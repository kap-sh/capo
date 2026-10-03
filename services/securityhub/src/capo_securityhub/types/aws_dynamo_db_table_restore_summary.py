"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableRestoreSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsDynamoDbTableRestoreSummary(TypedDict, closed=True):
    source_backup_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the source backup from which the table was restored.</p>"""
    source_table_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the source table for the backup.</p>"""
    restore_date_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates the point in time that the table was restored to.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    restore_in_progress: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether a restore is currently in progress.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableRestoreSummary) -> dict:
    out: dict = {}
    if "source_backup_arn" in value:
        out["SourceBackupArn"] = value["source_backup_arn"]
    if "source_table_arn" in value:
        out["SourceTableArn"] = value["source_table_arn"]
    if "restore_date_time" in value:
        out["RestoreDateTime"] = value["restore_date_time"]
    if "restore_in_progress" in value:
        out["RestoreInProgress"] = value["restore_in_progress"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableRestoreSummary:
    out: AwsDynamoDbTableRestoreSummary = {}  # type: ignore[typeddict-item]
    if data.get("SourceBackupArn") is not None:
        out["source_backup_arn"] = data["SourceBackupArn"]
    if data.get("SourceTableArn") is not None:
        out["source_table_arn"] = data["SourceTableArn"]
    if data.get("RestoreDateTime") is not None:
        out["restore_date_time"] = data["RestoreDateTime"]
    if data.get("RestoreInProgress") is not None:
        out["restore_in_progress"] = data["RestoreInProgress"]
    return out
