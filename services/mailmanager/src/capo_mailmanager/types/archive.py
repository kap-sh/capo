"""Generated from Smithy shape ``com.amazonaws.mailmanager#Archive``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.archive_id_string
    import capo_mailmanager.types.archive_name_string
    import capo_mailmanager.types.archive_state


class Archive(TypedDict, closed=True):
    archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString"
    """<p>The unique identifier of the archive.</p>"""
    archive_name: NotRequired[
        "capo_mailmanager.types.archive_name_string.ArchiveNameString"
    ]
    """<p>The unique name assigned to the archive.</p>"""
    archive_state: NotRequired["capo_mailmanager.types.archive_state.ArchiveState"]
    """<p>The current state of the archive:</p> <ul> <li> <p> <code>ACTIVE</code> – The archive is ready and available for use. </p> </li> <li> <p> <code>PENDING_DELETION</code> – The archive has been marked for deletion and will be permanently deleted in 30 days. No further modifications can be made in this state. </p> </li> </ul>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the archive was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Archive) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    if "archive_name" in value:
        out["ArchiveName"] = value["archive_name"]
    if "archive_state" in value:
        import capo_mailmanager.types.archive_state

        out["ArchiveState"] = (
            capo_mailmanager.types.archive_state.serialize_aws_json_1_0(
                value["archive_state"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Archive:
    out: Archive = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    else:
        out["archive_id"] = ""
    if data.get("ArchiveName") is not None:
        out["archive_name"] = data["ArchiveName"]
    if data.get("ArchiveState") is not None:
        import capo_mailmanager.types.archive_state

        out["archive_state"] = (
            capo_mailmanager.types.archive_state.deserialize_aws_json_1_0(
                data["ArchiveState"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    return out
