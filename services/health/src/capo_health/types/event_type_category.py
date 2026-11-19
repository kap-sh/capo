"""Generated from Smithy shape ``com.amazonaws.health#eventTypeCategory``."""

from typing import Literal, TypeAlias, cast

eventTypeCategory: TypeAlias = Literal[
    "issue",
    "accountNotification",
    "scheduledChange",
    "investigation",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventTypeCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> eventTypeCategory:
    return cast(eventTypeCategory, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: eventTypeCategory) -> str:
    return value


def deserialize_cbor(data: str) -> eventTypeCategory:
    return cast(eventTypeCategory, data)
