"""Generated from Smithy shape ``com.amazonaws.health#eventStatusCode``."""

from typing import Literal, TypeAlias, cast

eventStatusCode: TypeAlias = Literal[
    "open",
    "closed",
    "upcoming",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> eventStatusCode:
    return cast(eventStatusCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: eventStatusCode) -> str:
    return value


def deserialize_cbor(data: str) -> eventStatusCode:
    return cast(eventStatusCode, data)
