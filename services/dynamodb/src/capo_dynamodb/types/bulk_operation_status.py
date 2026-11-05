"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationStatus``."""

from typing import Literal, TypeAlias, cast

BulkOperationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "CANCELLING",
    "CANCELLED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BulkOperationStatus:
    return cast(BulkOperationStatus, data)
