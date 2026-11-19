"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceDirectoryState``."""

from typing import Literal, TypeAlias, cast

WorkspaceDirectoryState: TypeAlias = Literal[
    "REGISTERING",
    "REGISTERED",
    "DEREGISTERING",
    "DEREGISTERED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceDirectoryState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceDirectoryState:
    return cast(WorkspaceDirectoryState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceDirectoryState) -> str:
    return value


def deserialize_cbor(data: str) -> WorkspaceDirectoryState:
    return cast(WorkspaceDirectoryState, data)
