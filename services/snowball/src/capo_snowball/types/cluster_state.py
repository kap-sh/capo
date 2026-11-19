"""Generated from Smithy shape ``com.amazonaws.snowball#ClusterState``."""

from typing import Literal, TypeAlias, cast

ClusterState: TypeAlias = Literal[
    "AwaitingQuorum",
    "Pending",
    "InUse",
    "Complete",
    "Cancelled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterState:
    return cast(ClusterState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClusterState) -> str:
    return value


def deserialize_cbor(data: str) -> ClusterState:
    return cast(ClusterState, data)
