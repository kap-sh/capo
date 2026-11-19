"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoveRegionResult``."""

from typing_extensions import TypedDict


class RemoveRegionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveRegionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveRegionResult:
    out: RemoveRegionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RemoveRegionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RemoveRegionResult:
    out: RemoveRegionResult = {}  # type: ignore[typeddict-item]
    return out
