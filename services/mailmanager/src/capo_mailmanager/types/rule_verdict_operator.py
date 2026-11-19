"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictOperator``."""

from typing import Literal, TypeAlias, cast

RuleVerdictOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVerdictOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleVerdictOperator:
    return cast(RuleVerdictOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleVerdictOperator) -> str:
    return value


def deserialize_cbor(data: str) -> RuleVerdictOperator:
    return cast(RuleVerdictOperator, data)
