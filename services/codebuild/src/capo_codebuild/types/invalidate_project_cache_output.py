"""Generated from Smithy shape ``com.amazonaws.codebuild#InvalidateProjectCacheOutput``."""

from typing_extensions import TypedDict


class InvalidateProjectCacheOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidateProjectCacheOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidateProjectCacheOutput:
    out: InvalidateProjectCacheOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InvalidateProjectCacheOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> InvalidateProjectCacheOutput:
    out: InvalidateProjectCacheOutput = {}  # type: ignore[typeddict-item]
    return out
