"""Generated from Smithy shape ``com.amazonaws.proton#RepositorySyncAttempt``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.repository_sync_events
    import capo_proton.types.repository_sync_status


class RepositorySyncAttempt(TypedDict, closed=True):
    started_at: "datetime.datetime"
    """<p>The time when the sync attempt started.</p>"""
    status: "capo_proton.types.repository_sync_status.RepositorySyncStatus"
    """<p>The sync attempt status.</p>"""
    events: "capo_proton.types.repository_sync_events.RepositorySyncEvents"
    """<p>Detail data for sync attempt events.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncAttempt) -> dict:
    out: dict = {}
    import capo_proton.types._prelude.timestamp

    out["startedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["started_at"]
    )
    out["status"] = value["status"]
    import capo_proton.types.repository_sync_events

    out["events"] = capo_proton.types.repository_sync_events.serialize_aws_json_1_0(
        value["events"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositorySyncAttempt:
    out: RepositorySyncAttempt = {}  # type: ignore[typeddict-item]
    if data.get("startedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["started_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("events") is not None:
        import capo_proton.types.repository_sync_events

        out["events"] = (
            capo_proton.types.repository_sync_events.deserialize_aws_json_1_0(
                data["events"]
            )
        )
    else:
        out["events"] = []
    return out
