"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationUsageMultiple``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_usage

BulkOperationUsageMultiple: TypeAlias = list[
    "capo_dynamodb.types.bulk_operation_usage.BulkOperationUsage"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationUsageMultiple) -> list:
    import capo_dynamodb.types.bulk_operation_usage

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.bulk_operation_usage.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BulkOperationUsageMultiple:
    import capo_dynamodb.types.bulk_operation_usage

    out: BulkOperationUsageMultiple = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.bulk_operation_usage.deserialize_aws_json_1_0(item)
        )
    return out
