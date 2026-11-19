"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IdentifiedType``."""

from typing import Literal, TypeAlias, cast

IdentifiedType: TypeAlias = Literal[
    "STATELESS_RULE_FORWARDING_ASYMMETRICALLY",
    "STATELESS_RULE_CONTAINS_TCP_FLAGS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentifiedType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdentifiedType:
    return cast(IdentifiedType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentifiedType) -> str:
    return value


def deserialize_cbor(data: str) -> IdentifiedType:
    return cast(IdentifiedType, data)
