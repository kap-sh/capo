"""Generated from Smithy shape ``com.amazonaws.shield#DeleteSubscriptionResponse``."""

from typing_extensions import TypedDict


class DeleteSubscriptionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSubscriptionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSubscriptionResponse:
    out: DeleteSubscriptionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteSubscriptionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteSubscriptionResponse:
    out: DeleteSubscriptionResponse = {}  # type: ignore[typeddict-item]
    return out
