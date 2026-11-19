"""Generated from Smithy shape ``com.amazonaws.directoryservice#AddRegionResult``."""

from typing_extensions import TypedDict


class AddRegionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddRegionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AddRegionResult:
    out: AddRegionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AddRegionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AddRegionResult:
    out: AddRegionResult = {}  # type: ignore[typeddict-item]
    return out
