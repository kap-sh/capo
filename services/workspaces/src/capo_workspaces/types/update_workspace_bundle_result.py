"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateWorkspaceBundleResult``."""

from typing_extensions import TypedDict


class UpdateWorkspaceBundleResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkspaceBundleResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkspaceBundleResult:
    out: UpdateWorkspaceBundleResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateWorkspaceBundleResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateWorkspaceBundleResult:
    out: UpdateWorkspaceBundleResult = {}  # type: ignore[typeddict-item]
    return out
