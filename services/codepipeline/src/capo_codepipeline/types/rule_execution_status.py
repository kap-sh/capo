"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleExecutionStatus``."""

from typing import Literal, TypeAlias, cast

RuleExecutionStatus: TypeAlias = Literal[
    "InProgress",
    "Abandoned",
    "Succeeded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleExecutionStatus:
    return cast(RuleExecutionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleExecutionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> RuleExecutionStatus:
    return cast(RuleExecutionStatus, data)
