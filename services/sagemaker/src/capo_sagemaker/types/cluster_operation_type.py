"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOperationType``."""

from typing import Literal, TypeAlias, cast

ClusterOperationType: TypeAlias = Literal[
    "Scaling",
    "DeepHealthCheck",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOperationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterOperationType:
    return cast(ClusterOperationType, data)
