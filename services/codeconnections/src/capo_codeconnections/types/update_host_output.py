"""Generated from Smithy shape ``com.amazonaws.codeconnections#UpdateHostOutput``."""

from typing_extensions import TypedDict


class UpdateHostOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateHostOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateHostOutput:
    out: UpdateHostOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateHostOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateHostOutput:
    out: UpdateHostOutput = {}  # type: ignore[typeddict-item]
    return out
