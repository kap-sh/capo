"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleBooleanOperator``."""

from typing import Literal, TypeAlias, cast

RuleBooleanOperator: TypeAlias = Literal[
    "IS_TRUE",
    "IS_FALSE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleBooleanOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleBooleanOperator:
    return cast(RuleBooleanOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleBooleanOperator) -> str:
    return value


def deserialize_cbor(data: str) -> RuleBooleanOperator:
    return cast(RuleBooleanOperator, data)
