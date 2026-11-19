"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateWorkspaceImagePermissionResult``."""

from typing_extensions import TypedDict


class UpdateWorkspaceImagePermissionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkspaceImagePermissionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkspaceImagePermissionResult:
    out: UpdateWorkspaceImagePermissionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateWorkspaceImagePermissionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateWorkspaceImagePermissionResult:
    out: UpdateWorkspaceImagePermissionResult = {}  # type: ignore[typeddict-item]
    return out
