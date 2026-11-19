"""Generated from Smithy shape ``com.amazonaws.fms#DeleteNotificationChannelRequest``."""

from typing_extensions import TypedDict


class DeleteNotificationChannelRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNotificationChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNotificationChannelRequest:
    out: DeleteNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteNotificationChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteNotificationChannelRequest:
    out: DeleteNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    return out
