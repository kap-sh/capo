"""Generated from Smithy shape ``com.amazonaws.odb#CreateAutonomousDatabaseBackupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_status


class CreateAutonomousDatabaseBackupOutput(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the Autonomous Database backup that was created.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Autonomous Database backup.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous Database backup, if applicable.</p>"""
    autonomous_database_backup_id: "str"
    """<p>The unique identifier of the Autonomous Database backup that was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutonomousDatabaseBackupOutput) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["autonomousDatabaseBackupId"] = value["autonomous_database_backup_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutonomousDatabaseBackupOutput:
    out: CreateAutonomousDatabaseBackupOutput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("autonomousDatabaseBackupId") is not None:
        out["autonomous_database_backup_id"] = data["autonomousDatabaseBackupId"]
    else:
        out["autonomous_database_backup_id"] = ""
    return out
