"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateLogSubscriptionResult``."""

from typing_extensions import TypedDict


class CreateLogSubscriptionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLogSubscriptionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLogSubscriptionResult:
    out: CreateLogSubscriptionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateLogSubscriptionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CreateLogSubscriptionResult:
    out: CreateLogSubscriptionResult = {}  # type: ignore[typeddict-item]
    return out
