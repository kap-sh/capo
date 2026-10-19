"""Generated from Smithy shape ``com.amazonaws.odb#GetAutonomousDatabaseBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class GetAutonomousDatabaseBackupInput(TypedDict, closed=True):
    autonomous_database_backup_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous Database backup to retrieve information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutonomousDatabaseBackupInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseBackupId"] = value["autonomous_database_backup_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutonomousDatabaseBackupInput:
    out: GetAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseBackupId") is not None:
        out["autonomous_database_backup_id"] = data["autonomousDatabaseBackupId"]
    else:
        out["autonomous_database_backup_id"] = ""
    return out
