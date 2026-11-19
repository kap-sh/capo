"""Generated from Smithy shape ``com.amazonaws.servicediscovery#FilterCondition``."""

from typing import Literal, TypeAlias, cast

FilterCondition: TypeAlias = Literal[
    "EQ",
    "IN",
    "BETWEEN",
    "BEGINS_WITH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterCondition:
    return cast(FilterCondition, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterCondition) -> str:
    return value


def deserialize_cbor(data: str) -> FilterCondition:
    return cast(FilterCondition, data)
