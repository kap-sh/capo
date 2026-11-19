"""Generated from Smithy shape ``com.amazonaws.shield#AssociateDRTLogBucketResponse``."""

from typing_extensions import TypedDict


class AssociateDRTLogBucketResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateDRTLogBucketResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateDRTLogBucketResponse:
    out: AssociateDRTLogBucketResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateDRTLogBucketResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AssociateDRTLogBucketResponse:
    out: AssociateDRTLogBucketResponse = {}  # type: ignore[typeddict-item]
    return out
