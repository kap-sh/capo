"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationPerformanceTier``."""

from typing import Literal, TypeAlias, cast

BulkOperationPerformanceTier: TypeAlias = Literal[
    "STANDARD",
    "ACCELERATED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationPerformanceTier) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BulkOperationPerformanceTier:
    return cast(BulkOperationPerformanceTier, data)
