"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspaceCreationPropertiesResult``."""

from typing_extensions import TypedDict


class ModifyWorkspaceCreationPropertiesResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspaceCreationPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspaceCreationPropertiesResult:
    out: ModifyWorkspaceCreationPropertiesResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyWorkspaceCreationPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ModifyWorkspaceCreationPropertiesResult:
    out: ModifyWorkspaceCreationPropertiesResult = {}  # type: ignore[typeddict-item]
    return out
