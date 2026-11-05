"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeBulkOperationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_arn


class DescribeBulkOperationInput(TypedDict, closed=True):
    bulk_operation_arn: "capo_dynamodb.types.bulk_operation_arn.BulkOperationArn"
    """<p>The Amazon Resource Name (ARN) of the bulk operation to describe.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeBulkOperationInput) -> dict:
    out: dict = {}
    out["BulkOperationArn"] = value["bulk_operation_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeBulkOperationInput:
    out: DescribeBulkOperationInput = {}  # type: ignore[typeddict-item]
    if data.get("BulkOperationArn") is not None:
        out["bulk_operation_arn"] = data["BulkOperationArn"]
    else:
        out["bulk_operation_arn"] = ""
    return out
