"""Generated from Smithy shape ``com.amazonaws.shield#GetSubscriptionStateRequest``."""

from typing_extensions import TypedDict


class GetSubscriptionStateRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSubscriptionStateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSubscriptionStateRequest:
    out: GetSubscriptionStateRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSubscriptionStateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> GetSubscriptionStateRequest:
    out: GetSubscriptionStateRequest = {}  # type: ignore[typeddict-item]
    return out
