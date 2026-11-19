"""Generated from Smithy shape ``com.amazonaws.mailmanager#SnsNotificationPayloadType``."""

from typing import Literal, TypeAlias, cast

SnsNotificationPayloadType: TypeAlias = Literal[
    "HEADERS",
    "CONTENT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SnsNotificationPayloadType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SnsNotificationPayloadType:
    return cast(SnsNotificationPayloadType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnsNotificationPayloadType) -> str:
    return value


def deserialize_cbor(data: str) -> SnsNotificationPayloadType:
    return cast(SnsNotificationPayloadType, data)
