"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDiskSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class GetDiskSnapshotRequest(TypedDict, closed=True):
    disk_snapshot_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the disk snapshot (<code>my-disk-snapshot</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiskSnapshotRequest) -> dict:
    out: dict = {}
    out["diskSnapshotName"] = value["disk_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiskSnapshotRequest:
    out: GetDiskSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("diskSnapshotName") is not None:
        out["disk_snapshot_name"] = data["diskSnapshotName"]
    else:
        out["disk_snapshot_name"] = ""
    return out
