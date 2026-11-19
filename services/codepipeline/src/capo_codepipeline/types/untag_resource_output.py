"""Generated from Smithy shape ``com.amazonaws.codepipeline#UntagResourceOutput``."""

from typing_extensions import TypedDict


class UntagResourceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceOutput:
    out: UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UntagResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UntagResourceOutput:
    out: UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out
