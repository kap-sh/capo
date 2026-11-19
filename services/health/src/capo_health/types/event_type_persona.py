"""Generated from Smithy shape ``com.amazonaws.health#EventTypePersona``."""

from typing import Literal, TypeAlias, cast

EventTypePersona: TypeAlias = Literal[
    "OPERATIONS",
    "SECURITY",
    "BILLING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypePersona) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventTypePersona:
    return cast(EventTypePersona, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventTypePersona) -> str:
    return value


def deserialize_cbor(data: str) -> EventTypePersona:
    return cast(EventTypePersona, data)
