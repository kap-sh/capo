"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ConditionExecutionStatus: TypeAlias = Literal[
    "InProgress",
    "Failed",
    "Errored",
    "Succeeded",
    "Cancelled",
    "Abandoned",
    "Overridden",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConditionExecutionStatus:
    return cast(ConditionExecutionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConditionExecutionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ConditionExecutionStatus:
    return cast(ConditionExecutionStatus, data)
