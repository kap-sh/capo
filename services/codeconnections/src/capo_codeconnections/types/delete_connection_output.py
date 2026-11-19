"""Generated from Smithy shape ``com.amazonaws.codeconnections#DeleteConnectionOutput``."""

from typing_extensions import TypedDict


class DeleteConnectionOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteConnectionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteConnectionOutput:
    out: DeleteConnectionOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteConnectionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteConnectionOutput:
    out: DeleteConnectionOutput = {}  # type: ignore[typeddict-item]
    return out
