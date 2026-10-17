"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineExecutionStatus``."""

from typing import Literal, TypeAlias, cast

PipelineExecutionStatus: TypeAlias = Literal[
    "Executing",
    "Stopping",
    "Stopped",
    "Failed",
    "Succeeded",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineExecutionStatus:
    return cast(PipelineExecutionStatus, data)
