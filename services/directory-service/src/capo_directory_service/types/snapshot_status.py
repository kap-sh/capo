"""Generated from Smithy shape ``com.amazonaws.directoryservice#SnapshotStatus``."""

from typing import Literal, TypeAlias, cast

SnapshotStatus: TypeAlias = Literal[
    "Creating",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotStatus:
    return cast(SnapshotStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnapshotStatus) -> str:
    return value


def deserialize_cbor(data: str) -> SnapshotStatus:
    return cast(SnapshotStatus, data)
