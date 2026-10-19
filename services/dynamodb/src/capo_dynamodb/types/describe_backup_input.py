"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_arn


class DescribeBackupInput(TypedDict, closed=True):
    backup_arn: "capo_dynamodb.types.backup_arn.BackupArn"
    """<p>The Amazon Resource Name (ARN) associated with the backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeBackupInput) -> dict:
    out: dict = {}
    out["BackupArn"] = value["backup_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeBackupInput:
    out: DescribeBackupInput = {}  # type: ignore[typeddict-item]
    if data.get("BackupArn") is not None:
        out["backup_arn"] = data["BackupArn"]
    else:
        out["backup_arn"] = ""
    return out
