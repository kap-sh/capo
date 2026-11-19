"""Generated from Smithy shape ``com.amazonaws.codeconnections#DeleteHostOutput``."""

from typing_extensions import TypedDict


class DeleteHostOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteHostOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteHostOutput:
    out: DeleteHostOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteHostOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteHostOutput:
    out: DeleteHostOutput = {}  # type: ignore[typeddict-item]
    return out
