"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspaceStateResult``."""

from typing_extensions import TypedDict


class ModifyWorkspaceStateResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspaceStateResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspaceStateResult:
    out: ModifyWorkspaceStateResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyWorkspaceStateResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ModifyWorkspaceStateResult:
    out: ModifyWorkspaceStateResult = {}  # type: ignore[typeddict-item]
    return out
