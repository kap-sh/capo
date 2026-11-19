"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreExecutionPlanStatus``."""

from typing import Literal, TypeAlias, cast

RescoreExecutionPlanStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreExecutionPlanStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RescoreExecutionPlanStatus:
    return cast(RescoreExecutionPlanStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RescoreExecutionPlanStatus) -> str:
    return value


def deserialize_cbor(data: str) -> RescoreExecutionPlanStatus:
    return cast(RescoreExecutionPlanStatus, data)
