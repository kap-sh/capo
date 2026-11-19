"""Generated from Smithy shape ``com.amazonaws.shield#CreateSubscriptionRequest``."""

from typing_extensions import TypedDict


class CreateSubscriptionRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSubscriptionRequest:
    out: CreateSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CreateSubscriptionRequest:
    out: CreateSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
