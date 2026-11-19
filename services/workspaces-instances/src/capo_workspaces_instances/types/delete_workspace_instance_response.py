"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#DeleteWorkspaceInstanceResponse``."""

from typing_extensions import TypedDict


class DeleteWorkspaceInstanceResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteWorkspaceInstanceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteWorkspaceInstanceResponse:
    out: DeleteWorkspaceInstanceResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteWorkspaceInstanceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteWorkspaceInstanceResponse:
    out: DeleteWorkspaceInstanceResponse = {}  # type: ignore[typeddict-item]
    return out
