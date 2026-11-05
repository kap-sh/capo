"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_summary

BulkOperationsSummaryList: TypeAlias = list[
    "capo_dynamodb.types.bulk_operation_summary.BulkOperationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationsSummaryList) -> list:
    import capo_dynamodb.types.bulk_operation_summary

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.bulk_operation_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BulkOperationsSummaryList:
    import capo_dynamodb.types.bulk_operation_summary

    out: BulkOperationsSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.bulk_operation_summary.deserialize_aws_json_1_0(item)
        )
    return out
