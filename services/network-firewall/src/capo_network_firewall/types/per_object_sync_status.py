"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PerObjectSyncStatus``."""

from typing import Literal, TypeAlias, cast

PerObjectSyncStatus: TypeAlias = Literal[
    "PENDING",
    "IN_SYNC",
    "CAPACITY_CONSTRAINED",
    "NOT_SUBSCRIBED",
    "DEPRECATED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PerObjectSyncStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PerObjectSyncStatus:
    return cast(PerObjectSyncStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PerObjectSyncStatus) -> str:
    return value


def deserialize_cbor(data: str) -> PerObjectSyncStatus:
    return cast(PerObjectSyncStatus, data)
