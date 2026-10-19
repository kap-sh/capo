"""Generated from Smithy shape ``com.amazonaws.proton#ResourceSyncAttempt``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.resource_sync_events
    import capo_proton.types.resource_sync_status
    import capo_proton.types.revision


class ResourceSyncAttempt(TypedDict, closed=True):
    initial_revision: "capo_proton.types.revision.Revision"
    """<p>Detail data for the initial repository commit, path and push.</p>"""
    target_revision: "capo_proton.types.revision.Revision"
    """<p>Detail data for the target revision.</p>"""
    target: "str"
    """<p>The resource that is synced to.</p>"""
    started_at: "datetime.datetime"
    """<p>The time when the sync attempt started.</p>"""
    status: "capo_proton.types.resource_sync_status.ResourceSyncStatus"
    """<p>The status of the sync attempt.</p>"""
    events: "capo_proton.types.resource_sync_events.ResourceSyncEvents"
    """<p>An array of events with detail data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncAttempt) -> dict:
    out: dict = {}
    import capo_proton.types.revision

    out["initialRevision"] = capo_proton.types.revision.serialize_aws_json_1_0(
        value["initial_revision"]
    )
    import capo_proton.types.revision

    out["targetRevision"] = capo_proton.types.revision.serialize_aws_json_1_0(
        value["target_revision"]
    )
    out["target"] = value["target"]
    import capo_proton.types._prelude.timestamp

    out["startedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["started_at"]
    )
    out["status"] = value["status"]
    import capo_proton.types.resource_sync_events

    out["events"] = capo_proton.types.resource_sync_events.serialize_aws_json_1_0(
        value["events"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSyncAttempt:
    out: ResourceSyncAttempt = {}  # type: ignore[typeddict-item]
    if data.get("initialRevision") is not None:
        import capo_proton.types.revision

        out["initial_revision"] = capo_proton.types.revision.deserialize_aws_json_1_0(
            data["initialRevision"]
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.initial_revision required")
    if data.get("targetRevision") is not None:
        import capo_proton.types.revision

        out["target_revision"] = capo_proton.types.revision.deserialize_aws_json_1_0(
            data["targetRevision"]
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.target_revision required")
    if data.get("target") is not None:
        out["target"] = data["target"]
    else:
        out["target"] = ""
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
        import capo_proton.types.resource_sync_events

        out["events"] = capo_proton.types.resource_sync_events.deserialize_aws_json_1_0(
            data["events"]
        )
    else:
        out["events"] = []
    return out
