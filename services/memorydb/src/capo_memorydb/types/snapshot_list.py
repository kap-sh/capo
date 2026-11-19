"""Generated from Smithy shape ``com.amazonaws.memorydb#SnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.snapshot

SnapshotList: TypeAlias = list["capo_memorydb.types.snapshot.Snapshot"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotList) -> list:
    import capo_memorydb.types.snapshot

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.snapshot.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SnapshotList:
    import capo_memorydb.types.snapshot

    out: SnapshotList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.snapshot.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnapshotList) -> list:
    import capo_memorydb.types.snapshot

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.snapshot.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SnapshotList:
    import capo_memorydb.types.snapshot

    out: SnapshotList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.snapshot.deserialize_cbor(item))
    return out
