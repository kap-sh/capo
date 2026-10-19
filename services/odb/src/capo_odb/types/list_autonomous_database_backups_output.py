"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabaseBackupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_backup_list


class ListAutonomousDatabaseBackupsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    autonomous_database_backups: (
        "capo_odb.types.autonomous_database_backup_list.AutonomousDatabaseBackupList"
    )
    """<p>The list of Autonomous Database backups along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabaseBackupsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.autonomous_database_backup_list

    out["autonomousDatabaseBackups"] = (
        capo_odb.types.autonomous_database_backup_list.serialize_aws_json_1_0(
            value["autonomous_database_backups"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabaseBackupsOutput:
    out: ListAutonomousDatabaseBackupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("autonomousDatabaseBackups") is not None:
        import capo_odb.types.autonomous_database_backup_list

        out["autonomous_database_backups"] = (
            capo_odb.types.autonomous_database_backup_list.deserialize_aws_json_1_0(
                data["autonomousDatabaseBackups"]
            )
        )
    else:
        out["autonomous_database_backups"] = []
    return out
