"""Generated from Smithy shape ``com.amazonaws.health#EventPersona``."""

from typing import Literal, TypeAlias, cast

EventPersona: TypeAlias = Literal[
    "OPERATIONS",
    "SECURITY",
    "BILLING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventPersona) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventPersona:
    return cast(EventPersona, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventPersona) -> str:
    return value


def deserialize_cbor(data: str) -> EventPersona:
    return cast(EventPersona, data)
