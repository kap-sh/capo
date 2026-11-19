"""Generated from Smithy shape ``com.amazonaws.directoryservice#SnapshotType``."""

from typing import Literal, TypeAlias, cast

SnapshotType: TypeAlias = Literal[
    "Auto",
    "Manual",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotType:
    return cast(SnapshotType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnapshotType) -> str:
    return value


def deserialize_cbor(data: str) -> SnapshotType:
    return cast(SnapshotType, data)
