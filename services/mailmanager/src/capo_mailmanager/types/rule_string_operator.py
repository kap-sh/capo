"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringOperator``."""

from typing import Literal, TypeAlias, cast

RuleStringOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleStringOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleStringOperator:
    return cast(RuleStringOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleStringOperator) -> str:
    return value


def deserialize_cbor(data: str) -> RuleStringOperator:
    return cast(RuleStringOperator, data)
