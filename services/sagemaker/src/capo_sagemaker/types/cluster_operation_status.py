"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOperationStatus``."""

from typing import Literal, TypeAlias, cast

ClusterOperationStatus: TypeAlias = Literal[
    "InProgress",
    "Superseded",
    "Done",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOperationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterOperationStatus:
    return cast(ClusterOperationStatus, data)
