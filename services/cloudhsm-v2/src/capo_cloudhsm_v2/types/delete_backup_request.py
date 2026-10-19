"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DeleteBackupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup_id


class DeleteBackupRequest(TypedDict, closed=True):
    backup_id: "capo_cloudhsm_v2.types.backup_id.BackupId"
    """<p>The ID of the backup to be deleted. To find the ID of a backup, use the <a>DescribeBackups</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBackupRequest) -> dict:
    out: dict = {}
    out["BackupId"] = value["backup_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBackupRequest:
    out: DeleteBackupRequest = {}  # type: ignore[typeddict-item]
    if data.get("BackupId") is not None:
        out["backup_id"] = data["BackupId"]
    else:
        out["backup_id"] = ""
    return out
