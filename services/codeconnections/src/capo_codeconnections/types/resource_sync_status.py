"""Generated from Smithy shape ``com.amazonaws.codeconnections#ResourceSyncStatus``."""

from typing import Literal, TypeAlias, cast

ResourceSyncStatus: TypeAlias = Literal[
    "FAILED",
    "INITIATED",
    "IN_PROGRESS",
    "SUCCEEDED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceSyncStatus:
    return cast(ResourceSyncStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceSyncStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceSyncStatus:
    return cast(ResourceSyncStatus, data)
