"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateWorkspacesPoolSessionResult``."""

from typing_extensions import TypedDict


class TerminateWorkspacesPoolSessionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateWorkspacesPoolSessionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateWorkspacesPoolSessionResult:
    out: TerminateWorkspacesPoolSessionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TerminateWorkspacesPoolSessionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> TerminateWorkspacesPoolSessionResult:
    out: TerminateWorkspacesPoolSessionResult = {}  # type: ignore[typeddict-item]
    return out
