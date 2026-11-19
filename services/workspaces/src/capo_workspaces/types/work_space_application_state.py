"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceApplicationState``."""

from typing import Literal, TypeAlias, cast

WorkSpaceApplicationState: TypeAlias = Literal[
    "PENDING",
    "ERROR",
    "AVAILABLE",
    "UNINSTALL_ONLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceApplicationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkSpaceApplicationState:
    return cast(WorkSpaceApplicationState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkSpaceApplicationState) -> str:
    return value


def deserialize_cbor(data: str) -> WorkSpaceApplicationState:
    return cast(WorkSpaceApplicationState, data)
