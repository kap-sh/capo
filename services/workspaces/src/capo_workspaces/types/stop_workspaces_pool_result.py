"""Generated from Smithy shape ``com.amazonaws.workspaces#StopWorkspacesPoolResult``."""

from typing_extensions import TypedDict


class StopWorkspacesPoolResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopWorkspacesPoolResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopWorkspacesPoolResult:
    out: StopWorkspacesPoolResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopWorkspacesPoolResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopWorkspacesPoolResult:
    out: StopWorkspacesPoolResult = {}  # type: ignore[typeddict-item]
    return out
