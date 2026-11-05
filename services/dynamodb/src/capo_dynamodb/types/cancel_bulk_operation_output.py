"""Generated from Smithy shape ``com.amazonaws.dynamodb#CancelBulkOperationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_arn
    import capo_dynamodb.types.bulk_operation_status


class CancelBulkOperationOutput(TypedDict, closed=True):
    bulk_operation_arn: "capo_dynamodb.types.bulk_operation_arn.BulkOperationArn"
    """<p>The Amazon Resource Name (ARN) of the bulk operation for which DynamoDB accepted the cancellation request.</p>"""
    bulk_operation_status: (
        "capo_dynamodb.types.bulk_operation_status.BulkOperationStatus"
    )
    """<p>The status returned after DynamoDB accepts the cancellation request. This value is <code>CANCELLING</code>. Use <code>DescribeBulkOperation</code> to determine when the operation reaches <code>CANCELLED</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelBulkOperationOutput) -> dict:
    out: dict = {}
    out["BulkOperationArn"] = value["bulk_operation_arn"]
    import capo_dynamodb.types.bulk_operation_status

    out["BulkOperationStatus"] = (
        capo_dynamodb.types.bulk_operation_status.serialize_aws_json_1_0(
            value["bulk_operation_status"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelBulkOperationOutput:
    out: CancelBulkOperationOutput = {}  # type: ignore[typeddict-item]
    if data.get("BulkOperationArn") is not None:
        out["bulk_operation_arn"] = data["BulkOperationArn"]
    else:
        out["bulk_operation_arn"] = ""
    if data.get("BulkOperationStatus") is not None:
        import capo_dynamodb.types.bulk_operation_status

        out["bulk_operation_status"] = (
            capo_dynamodb.types.bulk_operation_status.deserialize_aws_json_1_0(
                data["BulkOperationStatus"]
            )
        )
    else:
        import typing

        out["bulk_operation_status"] = typing.cast(
            "capo_dynamodb.types.bulk_operation_status.BulkOperationStatus", ""
        )
    return out
