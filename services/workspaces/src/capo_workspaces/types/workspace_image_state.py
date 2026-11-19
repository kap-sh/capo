"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageState``."""

from typing import Literal, TypeAlias, cast

WorkspaceImageState: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceImageState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceImageState:
    return cast(WorkspaceImageState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceImageState) -> str:
    return value


def deserialize_cbor(data: str) -> WorkspaceImageState:
    return cast(WorkspaceImageState, data)
