"""Generated from Smithy shape ``com.amazonaws.workspaces#Snapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.timestamp


class Snapshot(TypedDict, closed=True):
    snapshot_time: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The time when the snapshot was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshot) -> dict:
    out: dict = {}
    if "snapshot_time" in value:
        import capo_workspaces.types.timestamp

        out["SnapshotTime"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["snapshot_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotTime") is not None:
        import capo_workspaces.types.timestamp

        out["snapshot_time"] = capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["SnapshotTime"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Snapshot) -> dict:
    out: dict = {}
    if "snapshot_time" in value:
        import capo_workspaces.types.timestamp

        out["SnapshotTime"] = capo_workspaces.types.timestamp.serialize_cbor(
            value["snapshot_time"]
        )
    return out


def deserialize_cbor(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotTime") is not None:
        import capo_workspaces.types.timestamp

        out["snapshot_time"] = capo_workspaces.types.timestamp.deserialize_cbor(
            data["SnapshotTime"]
        )
    return out
