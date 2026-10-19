"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ModifyBackupAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup_id
    import capo_cloudhsm_v2.types.boolean


class ModifyBackupAttributesRequest(TypedDict, closed=True):
    backup_id: "capo_cloudhsm_v2.types.backup_id.BackupId"
    """<p>The identifier (ID) of the backup to modify. To find the ID of a backup, use the <a>DescribeBackups</a> operation.</p>"""
    never_expires: "capo_cloudhsm_v2.types.boolean.Boolean"
    """<p>Specifies whether the service should exempt a backup from the retention policy for the cluster. <code>True</code> exempts a backup from the retention policy. <code>False</code> means the service applies the backup retention policy defined at the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyBackupAttributesRequest) -> dict:
    out: dict = {}
    out["BackupId"] = value["backup_id"]
    out["NeverExpires"] = value["never_expires"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyBackupAttributesRequest:
    out: ModifyBackupAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("BackupId") is not None:
        out["backup_id"] = data["BackupId"]
    else:
        out["backup_id"] = ""
    if data.get("NeverExpires") is not None:
        out["never_expires"] = data["NeverExpires"]
    else:
        out["never_expires"] = False
    return out
