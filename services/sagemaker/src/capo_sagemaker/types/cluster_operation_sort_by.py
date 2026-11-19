"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOperationSortBy``."""

from typing import Literal, TypeAlias, cast

ClusterOperationSortBy: TypeAlias = Literal["CreationTime",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOperationSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterOperationSortBy:
    return cast(ClusterOperationSortBy, data)
