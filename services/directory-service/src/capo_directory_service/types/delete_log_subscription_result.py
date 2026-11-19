"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteLogSubscriptionResult``."""

from typing_extensions import TypedDict


class DeleteLogSubscriptionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLogSubscriptionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLogSubscriptionResult:
    out: DeleteLogSubscriptionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteLogSubscriptionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteLogSubscriptionResult:
    out: DeleteLogSubscriptionResult = {}  # type: ignore[typeddict-item]
    return out
