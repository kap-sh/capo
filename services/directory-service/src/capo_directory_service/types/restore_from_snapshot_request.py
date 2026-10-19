"""Generated from Smithy shape ``com.amazonaws.directoryservice#RestoreFromSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.snapshot_id


class RestoreFromSnapshotRequest(TypedDict, closed=True):
    snapshot_id: "capo_directory_service.types.snapshot_id.SnapshotId"
    """<p>The identifier of the snapshot to restore from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreFromSnapshotRequest) -> dict:
    out: dict = {}
    out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreFromSnapshotRequest:
    out: RestoreFromSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    else:
        out["snapshot_id"] = ""
    return out
