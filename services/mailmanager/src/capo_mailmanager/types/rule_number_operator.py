"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleNumberOperator``."""

from typing import Literal, TypeAlias, cast

RuleNumberOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "LESS_THAN",
    "GREATER_THAN",
    "LESS_THAN_OR_EQUAL",
    "GREATER_THAN_OR_EQUAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleNumberOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleNumberOperator:
    return cast(RuleNumberOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleNumberOperator) -> str:
    return value


def deserialize_cbor(data: str) -> RuleNumberOperator:
    return cast(RuleNumberOperator, data)
