"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionStatus``."""

from typing import Literal, TypeAlias, cast

PipelineExecutionStatus: TypeAlias = Literal[
    "Cancelled",
    "InProgress",
    "Stopped",
    "Stopping",
    "Succeeded",
    "Superseded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineExecutionStatus:
    return cast(PipelineExecutionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PipelineExecutionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> PipelineExecutionStatus:
    return cast(PipelineExecutionStatus, data)
