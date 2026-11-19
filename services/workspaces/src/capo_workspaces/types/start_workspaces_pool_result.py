"""Generated from Smithy shape ``com.amazonaws.workspaces#StartWorkspacesPoolResult``."""

from typing_extensions import TypedDict


class StartWorkspacesPoolResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkspacesPoolResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StartWorkspacesPoolResult:
    out: StartWorkspacesPoolResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartWorkspacesPoolResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StartWorkspacesPoolResult:
    out: StartWorkspacesPoolResult = {}  # type: ignore[typeddict-item]
    return out
