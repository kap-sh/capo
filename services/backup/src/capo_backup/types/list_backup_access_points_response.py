"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupAccessPointsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_access_points


class ListBackupAccessPointsResponse(TypedDict, closed=True):
    backup_access_points: "capo_backup.types.backup_access_points.BackupAccessPoints"
    """<p>A list of backup access points, each containing metadata such as its name, ARN, status, and associated recovery point.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupAccessPointsResponse) -> dict:
    out: dict = {}
    import capo_backup.types.backup_access_points

    out["BackupAccessPoints"] = capo_backup.types.backup_access_points.serialize_json(
        value["backup_access_points"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBackupAccessPointsResponse:
    out: ListBackupAccessPointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("BackupAccessPoints") is not None:
        import capo_backup.types.backup_access_points

        out["backup_access_points"] = (
            capo_backup.types.backup_access_points.deserialize_json(
                data["BackupAccessPoints"]
            )
        )
    else:
        out["backup_access_points"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListBackupAccessPointsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "backup_access_points" in value:
        import capo_backup.types.backup_access_points

        out["backup_access_points"] = (
            capo_backup.types.backup_access_points.redact_sensitive(
                value["backup_access_points"]
            )
        )
    return out
