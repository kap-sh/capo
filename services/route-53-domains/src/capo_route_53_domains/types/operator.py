"""Generated from Smithy shape ``com.amazonaws.route53domains#Operator``."""

from typing import Literal, TypeAlias, cast

Operator: TypeAlias = Literal[
    "LE",
    "GE",
    "BEGINS_WITH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Operator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Operator:
    return cast(Operator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Operator) -> str:
    return value


def deserialize_cbor(data: str) -> Operator:
    return cast(Operator, data)
