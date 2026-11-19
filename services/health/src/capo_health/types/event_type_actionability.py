"""Generated from Smithy shape ``com.amazonaws.health#EventTypeActionability``."""

from typing import Literal, TypeAlias, cast

EventTypeActionability: TypeAlias = Literal[
    "ACTION_REQUIRED",
    "ACTION_MAY_BE_REQUIRED",
    "INFORMATIONAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeActionability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventTypeActionability:
    return cast(EventTypeActionability, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventTypeActionability) -> str:
    return value


def deserialize_cbor(data: str) -> EventTypeActionability:
    return cast(EventTypeActionability, data)
