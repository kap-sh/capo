"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspaceAccessPropertiesResult``."""

from typing_extensions import TypedDict


class ModifyWorkspaceAccessPropertiesResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspaceAccessPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspaceAccessPropertiesResult:
    out: ModifyWorkspaceAccessPropertiesResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyWorkspaceAccessPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ModifyWorkspaceAccessPropertiesResult:
    out: ModifyWorkspaceAccessPropertiesResult = {}  # type: ignore[typeddict-item]
    return out
