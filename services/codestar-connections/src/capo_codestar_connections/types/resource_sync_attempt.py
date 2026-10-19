"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ResourceSyncAttempt``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_connections.types.resource_sync_event_list
    import capo_codestar_connections.types.resource_sync_status
    import capo_codestar_connections.types.revision
    import capo_codestar_connections.types.target
    import capo_codestar_connections.types.timestamp


class ResourceSyncAttempt(TypedDict, closed=True):
    events: (
        "capo_codestar_connections.types.resource_sync_event_list.ResourceSyncEventList"
    )
    """<p>The events related to a resource sync attempt.</p>"""
    initial_revision: "capo_codestar_connections.types.revision.Revision"
    """<p>The current state of the resource as defined in the resource's <code>config-file</code> in the linked repository.</p>"""
    started_at: "capo_codestar_connections.types.timestamp.Timestamp"
    """<p>The start time for a resource sync attempt.</p>"""
    status: "capo_codestar_connections.types.resource_sync_status.ResourceSyncStatus"
    """<p>The status for a resource sync attempt. The follow are valid statuses:</p> <ul> <li> <p>SYNC-INITIATED - A resource sync attempt has been created and will begin soon.</p> </li> <li> <p>SYNCING - Syncing has started and work is being done to reconcile state.</p> </li> <li> <p>SYNCED - Syncing has completed successfully.</p> </li> <li> <p>SYNC_FAILED - A resource sync attempt has failed.</p> </li> </ul>"""
    target_revision: "capo_codestar_connections.types.revision.Revision"
    """<p>The desired state of the resource as defined in the resource's <code>config-file</code> in the linked repository. Git sync attempts to update the resource to this state.</p>"""
    target: "capo_codestar_connections.types.target.Target"
    """<p>The name of the Amazon Web Services resource that is attempted to be synchronized.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncAttempt) -> dict:
    out: dict = {}
    import capo_codestar_connections.types.resource_sync_event_list

    out["Events"] = (
        capo_codestar_connections.types.resource_sync_event_list.serialize_aws_json_1_0(
            value["events"]
        )
    )
    import capo_codestar_connections.types.revision

    out["InitialRevision"] = (
        capo_codestar_connections.types.revision.serialize_aws_json_1_0(
            value["initial_revision"]
        )
    )
    import capo_codestar_connections.types.timestamp

    out["StartedAt"] = capo_codestar_connections.types.timestamp.serialize_aws_json_1_0(
        value["started_at"]
    )
    import capo_codestar_connections.types.resource_sync_status

    out["Status"] = (
        capo_codestar_connections.types.resource_sync_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_codestar_connections.types.revision

    out["TargetRevision"] = (
        capo_codestar_connections.types.revision.serialize_aws_json_1_0(
            value["target_revision"]
        )
    )
    out["Target"] = value["target"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSyncAttempt:
    out: ResourceSyncAttempt = {}  # type: ignore[typeddict-item]
    if data.get("Events") is not None:
        import capo_codestar_connections.types.resource_sync_event_list

        out["events"] = (
            capo_codestar_connections.types.resource_sync_event_list.deserialize_aws_json_1_0(
                data["Events"]
            )
        )
    else:
        out["events"] = []
    if data.get("InitialRevision") is not None:
        import capo_codestar_connections.types.revision

        out["initial_revision"] = (
            capo_codestar_connections.types.revision.deserialize_aws_json_1_0(
                data["InitialRevision"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.initial_revision required")
    if data.get("StartedAt") is not None:
        import capo_codestar_connections.types.timestamp

        out["started_at"] = (
            capo_codestar_connections.types.timestamp.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Status") is not None:
        import capo_codestar_connections.types.resource_sync_status

        out["status"] = (
            capo_codestar_connections.types.resource_sync_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_codestar_connections.types.resource_sync_status.ResourceSyncStatus",
            "",
        )
    if data.get("TargetRevision") is not None:
        import capo_codestar_connections.types.revision

        out["target_revision"] = (
            capo_codestar_connections.types.revision.deserialize_aws_json_1_0(
                data["TargetRevision"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.target_revision required")
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    else:
        out["target"] = ""
    return out
