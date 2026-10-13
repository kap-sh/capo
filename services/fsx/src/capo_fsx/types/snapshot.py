"""Generated from Smithy shape ``com.amazonaws.fsx#Snapshot``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.administrative_actions
    import capo_fsx.types.creation_time
    import capo_fsx.types.lifecycle_transition_reason
    import capo_fsx.types.resource_arn
    import capo_fsx.types.snapshot_id
    import capo_fsx.types.snapshot_lifecycle
    import capo_fsx.types.snapshot_name
    import capo_fsx.types.tags
    import capo_fsx.types.volume_id


class Snapshot(TypedDict, closed=True):
    resource_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    snapshot_id: NotRequired["capo_fsx.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    name: NotRequired["capo_fsx.types.snapshot_name.SnapshotName"]
    """<p>The name of the snapshot.</p>"""
    volume_id: NotRequired["capo_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the volume that the snapshot is of.</p>"""
    creation_time: NotRequired["capo_fsx.types.creation_time.CreationTime"]
    lifecycle: NotRequired["capo_fsx.types.snapshot_lifecycle.SnapshotLifecycle"]
    """<p>The lifecycle status of the snapshot.</p> <ul> <li> <p> <code>PENDING</code> - Amazon FSx hasn't started creating the snapshot.</p> </li> <li> <p> <code>CREATING</code> - Amazon FSx is creating the snapshot.</p> </li> <li> <p> <code>DELETING</code> - Amazon FSx is deleting the snapshot.</p> </li> <li> <p> <code>AVAILABLE</code> - The snapshot is fully available.</p> </li> </ul>"""
    lifecycle_transition_reason: NotRequired[
        "capo_fsx.types.lifecycle_transition_reason.LifecycleTransitionReason"
    ]
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    administrative_actions: NotRequired[
        "capo_fsx.types.administrative_actions.AdministrativeActions"
    ]
    """<p>A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshot) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "creation_time" in value:
        import capo_fsx.types.creation_time

        out["CreationTime"] = capo_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "lifecycle" in value:
        import capo_fsx.types.snapshot_lifecycle

        out["Lifecycle"] = capo_fsx.types.snapshot_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    if "lifecycle_transition_reason" in value:
        import capo_fsx.types.lifecycle_transition_reason

        out["LifecycleTransitionReason"] = (
            capo_fsx.types.lifecycle_transition_reason.serialize_aws_json_1_1(
                value["lifecycle_transition_reason"]
            )
        )
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "administrative_actions" in value:
        import capo_fsx.types.administrative_actions

        out["AdministrativeActions"] = (
            capo_fsx.types.administrative_actions.serialize_aws_json_1_1(
                value["administrative_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    if data.get("CreationTime") is not None:
        import capo_fsx.types.creation_time

        out["creation_time"] = capo_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("Lifecycle") is not None:
        import capo_fsx.types.snapshot_lifecycle

        out["lifecycle"] = capo_fsx.types.snapshot_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    if data.get("LifecycleTransitionReason") is not None:
        import capo_fsx.types.lifecycle_transition_reason

        out["lifecycle_transition_reason"] = (
            capo_fsx.types.lifecycle_transition_reason.deserialize_aws_json_1_1(
                data["LifecycleTransitionReason"]
            )
        )
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("AdministrativeActions") is not None:
        import capo_fsx.types.administrative_actions

        out["administrative_actions"] = (
            capo_fsx.types.administrative_actions.deserialize_aws_json_1_1(
                data["AdministrativeActions"]
            )
        )
    return out


def redact_sensitive(value: Snapshot) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "administrative_actions" in value:
        import capo_fsx.types.administrative_actions

        out["administrative_actions"] = (
            capo_fsx.types.administrative_actions.redact_sensitive(
                value["administrative_actions"]
            )
        )
    return out
