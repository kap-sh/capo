"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class DeleteSnapshotRequest(TypedDict, closed=True):
    snapshot_name: "capo_memorydb.types.string.String"
    """<p>The name of the snapshot to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotRequest) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotRequest:
    out: DeleteSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    return out
