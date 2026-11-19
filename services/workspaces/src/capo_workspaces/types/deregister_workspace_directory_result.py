"""Generated from Smithy shape ``com.amazonaws.workspaces#DeregisterWorkspaceDirectoryResult``."""

from typing_extensions import TypedDict


class DeregisterWorkspaceDirectoryResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterWorkspaceDirectoryResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterWorkspaceDirectoryResult:
    out: DeregisterWorkspaceDirectoryResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeregisterWorkspaceDirectoryResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeregisterWorkspaceDirectoryResult:
    out: DeregisterWorkspaceDirectoryResult = {}  # type: ignore[typeddict-item]
    return out
