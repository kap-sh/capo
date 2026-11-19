"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateConditionalForwarderResult``."""

from typing_extensions import TypedDict


class CreateConditionalForwarderResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConditionalForwarderResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConditionalForwarderResult:
    out: CreateConditionalForwarderResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateConditionalForwarderResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CreateConditionalForwarderResult:
    out: CreateConditionalForwarderResult = {}  # type: ignore[typeddict-item]
    return out
