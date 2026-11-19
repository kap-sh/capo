"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteWorkspaceBundleResult``."""

from typing_extensions import TypedDict


class DeleteWorkspaceBundleResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkspaceBundleResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkspaceBundleResult:
    out: DeleteWorkspaceBundleResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteWorkspaceBundleResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteWorkspaceBundleResult:
    out: DeleteWorkspaceBundleResult = {}  # type: ignore[typeddict-item]
    return out
