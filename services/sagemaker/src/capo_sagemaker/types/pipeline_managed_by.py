"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineManagedBy``."""

from typing import Literal, TypeAlias, cast

PipelineManagedBy: TypeAlias = Literal[
    "AWS",
    "CUSTOMER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineManagedBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineManagedBy:
    return cast(PipelineManagedBy, data)
