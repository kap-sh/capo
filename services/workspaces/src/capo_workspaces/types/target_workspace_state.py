"""Generated from Smithy shape ``com.amazonaws.workspaces#TargetWorkspaceState``."""

from typing import Literal, TypeAlias, cast

TargetWorkspaceState: TypeAlias = Literal[
    "AVAILABLE",
    "ADMIN_MAINTENANCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetWorkspaceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetWorkspaceState:
    return cast(TargetWorkspaceState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetWorkspaceState) -> str:
    return value


def deserialize_cbor(data: str) -> TargetWorkspaceState:
    return cast(TargetWorkspaceState, data)
