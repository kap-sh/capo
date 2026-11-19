"""Generated from Smithy shape ``com.amazonaws.memorydb#CopySnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.snapshot


class CopySnapshotResponse(TypedDict, closed=True):
    snapshot: NotRequired["capo_memorydb.types.snapshot.Snapshot"]
    """<p>Represents a copy of an entire cluster as of the time when the snapshot was taken.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopySnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot" in value:
        import capo_memorydb.types.snapshot

        out["Snapshot"] = capo_memorydb.types.snapshot.serialize_aws_json_1_1(
            value["snapshot"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopySnapshotResponse:
    out: CopySnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("Snapshot") is not None:
        import capo_memorydb.types.snapshot

        out["snapshot"] = capo_memorydb.types.snapshot.deserialize_aws_json_1_1(
            data["Snapshot"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CopySnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot" in value:
        import capo_memorydb.types.snapshot

        out["Snapshot"] = capo_memorydb.types.snapshot.serialize_cbor(value["snapshot"])
    return out


def deserialize_cbor(data: dict) -> CopySnapshotResponse:
    out: CopySnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("Snapshot") is not None:
        import capo_memorydb.types.snapshot

        out["snapshot"] = capo_memorydb.types.snapshot.deserialize_cbor(
            data["Snapshot"]
        )
    return out
