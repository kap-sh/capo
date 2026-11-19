"""Generated from Smithy shape ``com.amazonaws.fms#GetNotificationChannelRequest``."""

from typing_extensions import TypedDict


class GetNotificationChannelRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNotificationChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNotificationChannelRequest:
    out: GetNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetNotificationChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> GetNotificationChannelRequest:
    out: GetNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    return out
