"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationTableDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_table_detail

BulkOperationTableDetails: TypeAlias = list[
    "capo_dynamodb.types.bulk_operation_table_detail.BulkOperationTableDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationTableDetails) -> list:
    import capo_dynamodb.types.bulk_operation_table_detail

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.bulk_operation_table_detail.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BulkOperationTableDetails:
    import capo_dynamodb.types.bulk_operation_table_detail

    out: BulkOperationTableDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.bulk_operation_table_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
