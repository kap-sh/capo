"""Generated from Smithy shape ``com.amazonaws.shield#CreateSubscriptionResponse``."""

from typing_extensions import TypedDict


class CreateSubscriptionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSubscriptionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSubscriptionResponse:
    out: CreateSubscriptionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSubscriptionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CreateSubscriptionResponse:
    out: CreateSubscriptionResponse = {}  # type: ignore[typeddict-item]
    return out
