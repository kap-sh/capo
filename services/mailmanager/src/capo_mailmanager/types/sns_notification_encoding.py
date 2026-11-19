"""Generated from Smithy shape ``com.amazonaws.mailmanager#SnsNotificationEncoding``."""

from typing import Literal, TypeAlias, cast

SnsNotificationEncoding: TypeAlias = Literal[
    "UTF-8",
    "BASE64",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SnsNotificationEncoding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SnsNotificationEncoding:
    return cast(SnsNotificationEncoding, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnsNotificationEncoding) -> str:
    return value


def deserialize_cbor(data: str) -> SnsNotificationEncoding:
    return cast(SnsNotificationEncoding, data)
