"""Generated from Smithy shape ``com.amazonaws.shield#DisassociateDRTLogBucketResponse``."""

from typing_extensions import TypedDict


class DisassociateDRTLogBucketResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateDRTLogBucketResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateDRTLogBucketResponse:
    out: DisassociateDRTLogBucketResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateDRTLogBucketResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateDRTLogBucketResponse:
    out: DisassociateDRTLogBucketResponse = {}  # type: ignore[typeddict-item]
    return out
