"""Generated from Smithy shape ``com.amazonaws.codeconnections#RepositorySyncAttempt``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.repository_sync_event_list
    import capo_codeconnections.types.repository_sync_status
    import capo_codeconnections.types.timestamp


class RepositorySyncAttempt(TypedDict, closed=True):
    started_at: "capo_codeconnections.types.timestamp.Timestamp"
    """<p>The start time of a specific sync attempt.</p>"""
    status: "capo_codeconnections.types.repository_sync_status.RepositorySyncStatus"
    """<p>The status of a specific sync attempt. The following are valid statuses:</p> <ul> <li> <p>INITIATED - A repository sync attempt has been created and will begin soon.</p> </li> <li> <p>IN_PROGRESS - A repository sync attempt has started and work is being done to reconcile the branch.</p> </li> <li> <p>SUCCEEDED - The repository sync attempt has completed successfully.</p> </li> <li> <p>FAILED - The repository sync attempt has failed.</p> </li> <li> <p>QUEUED - The repository sync attempt didn't execute and was queued.</p> </li> </ul>"""
    events: (
        "capo_codeconnections.types.repository_sync_event_list.RepositorySyncEventList"
    )
    """<p>The events associated with a specific sync attempt.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncAttempt) -> dict:
    out: dict = {}
    import capo_codeconnections.types.timestamp

    out["StartedAt"] = capo_codeconnections.types.timestamp.serialize_aws_json_1_0(
        value["started_at"]
    )
    import capo_codeconnections.types.repository_sync_status

    out["Status"] = (
        capo_codeconnections.types.repository_sync_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_codeconnections.types.repository_sync_event_list

    out["Events"] = (
        capo_codeconnections.types.repository_sync_event_list.serialize_aws_json_1_0(
            value["events"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositorySyncAttempt:
    out: RepositorySyncAttempt = {}  # type: ignore[typeddict-item]
    if data.get("StartedAt") is not None:
        import capo_codeconnections.types.timestamp

        out["started_at"] = (
            capo_codeconnections.types.timestamp.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Status") is not None:
        import capo_codeconnections.types.repository_sync_status

        out["status"] = (
            capo_codeconnections.types.repository_sync_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_codeconnections.types.repository_sync_status.RepositorySyncStatus", ""
        )
    if data.get("Events") is not None:
        import capo_codeconnections.types.repository_sync_event_list

        out["events"] = (
            capo_codeconnections.types.repository_sync_event_list.deserialize_aws_json_1_0(
                data["Events"]
            )
        )
    else:
        out["events"] = []
    return out
