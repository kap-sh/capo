"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_arn


class DeleteBackupInput(TypedDict, closed=True):
    backup_arn: "capo_dynamodb.types.backup_arn.BackupArn"
    """<p>The ARN associated with the backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteBackupInput) -> dict:
    out: dict = {}
    out["BackupArn"] = value["backup_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteBackupInput:
    out: DeleteBackupInput = {}  # type: ignore[typeddict-item]
    if data.get("BackupArn") is not None:
        out["backup_arn"] = data["BackupArn"]
    else:
        out["backup_arn"] = ""
    return out
