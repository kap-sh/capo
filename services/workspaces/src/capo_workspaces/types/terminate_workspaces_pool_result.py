"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateWorkspacesPoolResult``."""

from typing_extensions import TypedDict


class TerminateWorkspacesPoolResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateWorkspacesPoolResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateWorkspacesPoolResult:
    out: TerminateWorkspacesPoolResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TerminateWorkspacesPoolResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> TerminateWorkspacesPoolResult:
    out: TerminateWorkspacesPoolResult = {}  # type: ignore[typeddict-item]
    return out
