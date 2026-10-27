"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeepHealthCheckType``."""

from typing import Literal, TypeAlias, cast

DeepHealthCheckType: TypeAlias = Literal[
    "InstanceStress",
    "InstanceConnectivity",
    "MultiNodeTrainingValidation",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeepHealthCheckType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeepHealthCheckType:
    return cast(DeepHealthCheckType, data)
