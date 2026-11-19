"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ClusterState``."""

from typing import Literal, TypeAlias, cast

ClusterState: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "UNINITIALIZED",
    "INITIALIZE_IN_PROGRESS",
    "INITIALIZED",
    "ACTIVE",
    "UPDATE_IN_PROGRESS",
    "MODIFY_IN_PROGRESS",
    "ROLLBACK_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "DELETED",
    "DEGRADED",
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
