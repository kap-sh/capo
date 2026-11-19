"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoveIpRoutesResult``."""

from typing_extensions import TypedDict


class RemoveIpRoutesResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveIpRoutesResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveIpRoutesResult:
    out: RemoveIpRoutesResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RemoveIpRoutesResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RemoveIpRoutesResult:
    out: RemoveIpRoutesResult = {}  # type: ignore[typeddict-item]
    return out
