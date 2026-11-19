"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteIpGroupResult``."""

from typing_extensions import TypedDict


class DeleteIpGroupResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIpGroupResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIpGroupResult:
    out: DeleteIpGroupResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteIpGroupResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteIpGroupResult:
    out: DeleteIpGroupResult = {}  # type: ignore[typeddict-item]
    return out
