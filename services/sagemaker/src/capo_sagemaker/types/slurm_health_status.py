"""Generated from Smithy shape ``com.amazonaws.sagemaker#SlurmHealthStatus``."""

from typing import Literal, TypeAlias, cast

SlurmHealthStatus: TypeAlias = Literal[
    "Healthy",
    "Unhealthy",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SlurmHealthStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SlurmHealthStatus:
    return cast(SlurmHealthStatus, data)
