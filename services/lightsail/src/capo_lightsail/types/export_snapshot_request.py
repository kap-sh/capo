"""Generated from Smithy shape ``com.amazonaws.lightsail#ExportSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class ExportSnapshotRequest(TypedDict, closed=True):
    source_snapshot_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance or disk snapshot to be exported to Amazon EC2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSnapshotRequest) -> dict:
    out: dict = {}
    out["sourceSnapshotName"] = value["source_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportSnapshotRequest:
    out: ExportSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceSnapshotName") is not None:
        out["source_snapshot_name"] = data["sourceSnapshotName"]
    else:
        out["source_snapshot_name"] = ""
    return out
