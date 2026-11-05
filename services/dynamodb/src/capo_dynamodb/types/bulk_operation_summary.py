"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_arn
    import capo_dynamodb.types.bulk_operation_end_time
    import capo_dynamodb.types.bulk_operation_start_time
    import capo_dynamodb.types.bulk_operation_status


class BulkOperationSummary(TypedDict, closed=True):
    bulk_operation_arn: "capo_dynamodb.types.bulk_operation_arn.BulkOperationArn"
    """<p>The Amazon Resource Name (ARN) of the bulk operation.</p>"""
    bulk_operation_status: (
        "capo_dynamodb.types.bulk_operation_status.BulkOperationStatus"
    )
    """<p>The current status of the bulk operation.</p>"""
    start_time: "capo_dynamodb.types.bulk_operation_start_time.BulkOperationStartTime"
    """<p>The time when DynamoDB accepted the start request.</p>"""
    end_time: NotRequired[
        "capo_dynamodb.types.bulk_operation_end_time.BulkOperationEndTime"
    ]
    """<p>The time when the operation reached a terminal status. DynamoDB omits this value while the operation remains in progress.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationSummary) -> dict:
    out: dict = {}
    out["BulkOperationArn"] = value["bulk_operation_arn"]
    import capo_dynamodb.types.bulk_operation_status

    out["BulkOperationStatus"] = (
        capo_dynamodb.types.bulk_operation_status.serialize_aws_json_1_0(
            value["bulk_operation_status"]
        )
    )
    import capo_dynamodb.types.bulk_operation_start_time

    out["StartTime"] = (
        capo_dynamodb.types.bulk_operation_start_time.serialize_aws_json_1_0(
            value["start_time"]
        )
    )
    if "end_time" in value:
        import capo_dynamodb.types.bulk_operation_end_time

        out["EndTime"] = (
            capo_dynamodb.types.bulk_operation_end_time.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BulkOperationSummary:
    out: BulkOperationSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("StartTime") is not None:
        import capo_dynamodb.types.bulk_operation_start_time

        out["start_time"] = (
            capo_dynamodb.types.bulk_operation_start_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_dynamodb.types.bulk_operation_end_time

        out["end_time"] = (
            capo_dynamodb.types.bulk_operation_end_time.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    return out
