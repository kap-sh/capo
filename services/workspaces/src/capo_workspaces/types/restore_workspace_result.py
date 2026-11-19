"""Generated from Smithy shape ``com.amazonaws.workspaces#RestoreWorkspaceResult``."""

from typing_extensions import TypedDict


class RestoreWorkspaceResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreWorkspaceResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreWorkspaceResult:
    out: RestoreWorkspaceResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RestoreWorkspaceResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RestoreWorkspaceResult:
    out: RestoreWorkspaceResult = {}  # type: ignore[typeddict-item]
    return out
