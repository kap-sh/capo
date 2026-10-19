"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteInstanceSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class DeleteInstanceSnapshotRequest(TypedDict, closed=True):
    instance_snapshot_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the snapshot to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInstanceSnapshotRequest) -> dict:
    out: dict = {}
    out["instanceSnapshotName"] = value["instance_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInstanceSnapshotRequest:
    out: DeleteInstanceSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("instanceSnapshotName") is not None:
        out["instance_snapshot_name"] = data["instanceSnapshotName"]
    else:
        out["instance_snapshot_name"] = ""
    return out
