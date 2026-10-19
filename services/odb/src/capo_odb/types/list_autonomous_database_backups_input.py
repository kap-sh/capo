"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabaseBackupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_backup_status
    import capo_odb.types.autonomous_database_backup_type
    import capo_odb.types.resource_id


class ListAutonomousDatabaseBackupsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    autonomous_database_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous Database whose backups you want to list.</p>"""
    status: NotRequired[
        "capo_odb.types.autonomous_database_backup_status.AutonomousDatabaseBackupStatus"
    ]
    """<p>The status of the Autonomous Database backups to return results for.</p>"""
    type: NotRequired[
        "capo_odb.types.autonomous_database_backup_type.AutonomousDatabaseBackupType"
    ]
    """<p>The type of the Autonomous Database backups to return results for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabaseBackupsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "status" in value:
        import capo_odb.types.autonomous_database_backup_status

        out["status"] = (
            capo_odb.types.autonomous_database_backup_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "type" in value:
        import capo_odb.types.autonomous_database_backup_type

        out["type"] = (
            capo_odb.types.autonomous_database_backup_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabaseBackupsInput:
    out: ListAutonomousDatabaseBackupsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        out["autonomous_database_id"] = ""
    if data.get("status") is not None:
        import capo_odb.types.autonomous_database_backup_status

        out["status"] = (
            capo_odb.types.autonomous_database_backup_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("type") is not None:
        import capo_odb.types.autonomous_database_backup_type

        out["type"] = (
            capo_odb.types.autonomous_database_backup_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    return out
