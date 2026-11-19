"""Generated from Smithy shape ``com.amazonaws.shield#UpdateSubscriptionResponse``."""

from typing_extensions import TypedDict


class UpdateSubscriptionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubscriptionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubscriptionResponse:
    out: UpdateSubscriptionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateSubscriptionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateSubscriptionResponse:
    out: UpdateSubscriptionResponse = {}  # type: ignore[typeddict-item]
    return out
