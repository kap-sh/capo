"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceType``."""

from typing import Literal, TypeAlias, cast

WorkspaceType: TypeAlias = Literal[
    "PERSONAL",
    "POOLS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceType:
    return cast(WorkspaceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceType) -> str:
    return value


def deserialize_cbor(data: str) -> WorkspaceType:
    return cast(WorkspaceType, data)
