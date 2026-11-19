"""Generated from Smithy shape ``com.amazonaws.health#EventActionability``."""

from typing import Literal, TypeAlias, cast

EventActionability: TypeAlias = Literal[
    "ACTION_REQUIRED",
    "ACTION_MAY_BE_REQUIRED",
    "INFORMATIONAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventActionability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventActionability:
    return cast(EventActionability, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventActionability) -> str:
    return value


def deserialize_cbor(data: str) -> EventActionability:
    return cast(EventActionability, data)
