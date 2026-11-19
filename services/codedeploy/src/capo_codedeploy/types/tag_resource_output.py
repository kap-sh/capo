"""Generated from Smithy shape ``com.amazonaws.codedeploy#TagResourceOutput``."""

from typing_extensions import TypedDict


class TagResourceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceOutput:
    out: TagResourceOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> TagResourceOutput:
    out: TagResourceOutput = {}  # type: ignore[typeddict-item]
    return out
