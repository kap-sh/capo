"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteWorkspaceImageResult``."""

from typing_extensions import TypedDict


class DeleteWorkspaceImageResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkspaceImageResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkspaceImageResult:
    out: DeleteWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteWorkspaceImageResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteWorkspaceImageResult:
    out: DeleteWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    return out
