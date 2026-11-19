"""Generated from Smithy shape ``com.amazonaws.kendraranking#TagResourceResponse``."""

from typing_extensions import TypedDict


class TagResourceResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceResponse:
    out: TagResourceResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagResourceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> TagResourceResponse:
    out: TagResourceResponse = {}  # type: ignore[typeddict-item]
    return out
