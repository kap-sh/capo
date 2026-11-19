"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.snapshot_id


class DeleteSnapshotResult(TypedDict, closed=True):
    snapshot_id: NotRequired["capo_directory_service.types.snapshot_id.SnapshotId"]
    """<p>The identifier of the directory snapshot that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotResult) -> dict:
    out: dict = {}
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotResult:
    out: DeleteSnapshotResult = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteSnapshotResult) -> dict:
    out: dict = {}
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteSnapshotResult:
    out: DeleteSnapshotResult = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    return out
