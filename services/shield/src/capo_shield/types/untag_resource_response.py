"""Generated from Smithy shape ``com.amazonaws.shield#UntagResourceResponse``."""

from typing_extensions import TypedDict


class UntagResourceResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceResponse:
    out: UntagResourceResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UntagResourceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UntagResourceResponse:
    out: UntagResourceResponse = {}  # type: ignore[typeddict-item]
    return out
