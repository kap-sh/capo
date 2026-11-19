"""Generated from Smithy shape ``com.amazonaws.shield#DeleteSubscriptionRequest``."""

from typing_extensions import TypedDict


class DeleteSubscriptionRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSubscriptionRequest:
    out: DeleteSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteSubscriptionRequest:
    out: DeleteSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
