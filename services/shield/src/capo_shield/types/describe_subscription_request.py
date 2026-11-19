"""Generated from Smithy shape ``com.amazonaws.shield#DescribeSubscriptionRequest``."""

from typing_extensions import TypedDict


class DescribeSubscriptionRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscriptionRequest:
    out: DescribeSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DescribeSubscriptionRequest:
    out: DescribeSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
