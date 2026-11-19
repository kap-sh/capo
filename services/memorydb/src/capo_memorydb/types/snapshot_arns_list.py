"""Generated from Smithy shape ``com.amazonaws.memorydb#SnapshotArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.string

SnapshotArnsList: TypeAlias = list["capo_memorydb.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotArnsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SnapshotArnsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnapshotArnsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SnapshotArnsList:
    return [item for item in data if item is not None]
