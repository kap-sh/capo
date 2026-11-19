"""Generated from Smithy shape ``com.amazonaws.health#eventScopeCode``."""

from typing import Literal, TypeAlias, cast

eventScopeCode: TypeAlias = Literal[
    "PUBLIC",
    "ACCOUNT_SPECIFIC",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventScopeCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> eventScopeCode:
    return cast(eventScopeCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: eventScopeCode) -> str:
    return value


def deserialize_cbor(data: str) -> eventScopeCode:
    return cast(eventScopeCode, data)
