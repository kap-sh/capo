"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolState``."""

from typing import Literal, TypeAlias, cast

WorkspacesPoolState: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspacesPoolState:
    return cast(WorkspacesPoolState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspacesPoolState) -> str:
    return value


def deserialize_cbor(data: str) -> WorkspacesPoolState:
    return cast(WorkspacesPoolState, data)
