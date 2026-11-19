"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspacePropertiesResult``."""

from typing_extensions import TypedDict


class ModifyWorkspacePropertiesResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspacePropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspacePropertiesResult:
    out: ModifyWorkspacePropertiesResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyWorkspacePropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ModifyWorkspacePropertiesResult:
    out: ModifyWorkspacePropertiesResult = {}  # type: ignore[typeddict-item]
    return out
