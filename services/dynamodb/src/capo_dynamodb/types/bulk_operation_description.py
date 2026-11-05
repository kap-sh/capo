"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_arn
    import capo_dynamodb.types.bulk_operation_end_time
    import capo_dynamodb.types.bulk_operation_item_count
    import capo_dynamodb.types.bulk_operation_max_write_request_units
    import capo_dynamodb.types.bulk_operation_performance_tier
    import capo_dynamodb.types.bulk_operation_start_time
    import capo_dynamodb.types.bulk_operation_status
    import capo_dynamodb.types.bulk_operation_table_details
    import capo_dynamodb.types.bulk_operation_usage_multiple
    import capo_dynamodb.types.client_token
    import capo_dynamodb.types.failure_code
    import capo_dynamodb.types.failure_message
    import capo_dynamodb.types.input_s3_configuration
    import capo_dynamodb.types.output_s3_configuration
    import capo_dynamodb.types.processed_input_bytes
    import capo_dynamodb.types.total_input_bytes


class BulkOperationDescription(TypedDict, closed=True):
    bulk_operation_arn: NotRequired[
        "capo_dynamodb.types.bulk_operation_arn.BulkOperationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the bulk operation.</p>"""
    bulk_operation_status: NotRequired[
        "capo_dynamodb.types.bulk_operation_status.BulkOperationStatus"
    ]
    """<p>The current status of the bulk operation can be one of the following values:</p> <dl> <dt> IN_PROGRESS </dt> <dd> <p>DynamoDB is processing the input.</p> </dd> <dt> COMPLETED </dt> <dd> <p>The bulk operation finished without parsing or validation errors. Condition-check failures do not cause the operation to complete with errors.</p> </dd> <dt> COMPLETED_WITH_ERRORS </dt> <dd> <p>The bulk operation finished, but DynamoDB couldn't process at least one input item because of a parsing or validation error. When you enable <code>ERROR</code> output, DynamoDB writes the details to the configured Amazon S3 output location.</p> </dd> <dt> CANCELLING </dt> <dd> <p>DynamoDB accepted a cancellation request and is stopping the operation.</p> </dd> <dt> CANCELLED </dt> <dd> <p>DynamoDB stopped the operation after a cancellation request.</p> </dd> <dt> FAILED </dt> <dd> <p>The bulk operation failed. DynamoDB might write some items before the operation reaches this status. See <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-FailureCode">FailureCode</a> and <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-FailureMessage">FailureMessage</a> for details.</p> </dd> </dl>"""
    table_details: NotRequired[
        "capo_dynamodb.types.bulk_operation_table_details.BulkOperationTableDetails"
    ]
    """<p>A list containing identifying information for the table targeted by the bulk operation.</p>"""
    client_token: NotRequired["capo_dynamodb.types.client_token.ClientToken"]
    """<p>The idempotency token associated with the start request.</p>"""
    input_s3_configuration: NotRequired[
        "capo_dynamodb.types.input_s3_configuration.InputS3Configuration"
    ]
    """<p>The Amazon S3 input configuration associated with the bulk operation.</p>"""
    output_s3_configuration: NotRequired[
        "capo_dynamodb.types.output_s3_configuration.OutputS3Configuration"
    ]
    """<p>The Amazon S3 output configuration associated with the bulk operation.</p>"""
    start_time: NotRequired[
        "capo_dynamodb.types.bulk_operation_start_time.BulkOperationStartTime"
    ]
    """<p>The time when DynamoDB accepted the start request.</p>"""
    end_time: NotRequired[
        "capo_dynamodb.types.bulk_operation_end_time.BulkOperationEndTime"
    ]
    """<p>The time when the operation reached a terminal status. DynamoDB omits this value while the operation remains in progress.</p>"""
    processed_item_count: (
        "capo_dynamodb.types.bulk_operation_item_count.BulkOperationItemCount"
    )
    """<p>The number of input items that DynamoDB has processed. This count includes successful writes, parsing or validation failures, and condition-check failures.</p>"""
    processed_input_bytes: NotRequired[
        "capo_dynamodb.types.processed_input_bytes.ProcessedInputBytes"
    ]
    """<p>The number of bytes that DynamoDB has read from the Amazon S3 input objects.</p>"""
    total_input_bytes: NotRequired[
        "capo_dynamodb.types.total_input_bytes.TotalInputBytes"
    ]
    """<p>The total size, in bytes, of the Amazon S3 input objects. DynamoDB omits this value until the initial input-size calculation completes.</p>"""
    bulk_operation_usage: NotRequired[
        "capo_dynamodb.types.bulk_operation_usage_multiple.BulkOperationUsageMultiple"
    ]
    """<p>Usage information for the table and its indexes.</p>"""
    failed_item_count: (
        "capo_dynamodb.types.bulk_operation_item_count.BulkOperationItemCount"
    )
    """<p>The number of processed input items that failed because of parsing or validation errors. This count is included in <code>ProcessedItemCount</code>. Condition-check failures do not increase this count.</p>"""
    failure_code: NotRequired["capo_dynamodb.types.failure_code.FailureCode"]
    """<p>A code that identifies why the bulk operation failed or was cancelled. DynamoDB returns this value only when <code>BulkOperationStatus</code> is <code>FAILED</code> or <code>CANCELLED</code>.</p>"""
    failure_message: NotRequired["capo_dynamodb.types.failure_message.FailureMessage"]
    """<p>A message that describes why the bulk operation failed or was cancelled. DynamoDB returns this value only when <code>BulkOperationStatus</code> is <code>FAILED</code> or <code>CANCELLED</code>.</p>"""
    max_write_request_units: NotRequired[
        "capo_dynamodb.types.bulk_operation_max_write_request_units.BulkOperationMaxWriteRequestUnits"
    ]
    """<p>The maximum write request unit rate configured for the bulk operation.</p>"""
    performance_tier: NotRequired[
        "capo_dynamodb.types.bulk_operation_performance_tier.BulkOperationPerformanceTier"
    ]
    """<p>The performance tier selected for the bulk operation. Valid values are <code>STANDARD</code> and <code>ACCELERATED</code>. If the start request omitted this value, DynamoDB uses <code>STANDARD</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationDescription) -> dict:
    out: dict = {}
    if "bulk_operation_arn" in value:
        out["BulkOperationArn"] = value["bulk_operation_arn"]
    if "bulk_operation_status" in value:
        import capo_dynamodb.types.bulk_operation_status

        out["BulkOperationStatus"] = (
            capo_dynamodb.types.bulk_operation_status.serialize_aws_json_1_0(
                value["bulk_operation_status"]
            )
        )
    if "table_details" in value:
        import capo_dynamodb.types.bulk_operation_table_details

        out["TableDetails"] = (
            capo_dynamodb.types.bulk_operation_table_details.serialize_aws_json_1_0(
                value["table_details"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "input_s3_configuration" in value:
        import capo_dynamodb.types.input_s3_configuration

        out["InputS3Configuration"] = (
            capo_dynamodb.types.input_s3_configuration.serialize_aws_json_1_0(
                value["input_s3_configuration"]
            )
        )
    if "output_s3_configuration" in value:
        import capo_dynamodb.types.output_s3_configuration

        out["OutputS3Configuration"] = (
            capo_dynamodb.types.output_s3_configuration.serialize_aws_json_1_0(
                value["output_s3_configuration"]
            )
        )
    if "start_time" in value:
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
    out["ProcessedItemCount"] = value.get("processed_item_count", 0)
    if "processed_input_bytes" in value:
        out["ProcessedInputBytes"] = value["processed_input_bytes"]
    if "total_input_bytes" in value:
        out["TotalInputBytes"] = value["total_input_bytes"]
    if "bulk_operation_usage" in value:
        import capo_dynamodb.types.bulk_operation_usage_multiple

        out["BulkOperationUsage"] = (
            capo_dynamodb.types.bulk_operation_usage_multiple.serialize_aws_json_1_0(
                value["bulk_operation_usage"]
            )
        )
    out["FailedItemCount"] = value.get("failed_item_count", 0)
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "max_write_request_units" in value:
        out["MaxWriteRequestUnits"] = value["max_write_request_units"]
    if "performance_tier" in value:
        import capo_dynamodb.types.bulk_operation_performance_tier

        out["PerformanceTier"] = (
            capo_dynamodb.types.bulk_operation_performance_tier.serialize_aws_json_1_0(
                value["performance_tier"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BulkOperationDescription:
    out: BulkOperationDescription = {}  # type: ignore[typeddict-item]
    if data.get("BulkOperationArn") is not None:
        out["bulk_operation_arn"] = data["BulkOperationArn"]
    if data.get("BulkOperationStatus") is not None:
        import capo_dynamodb.types.bulk_operation_status

        out["bulk_operation_status"] = (
            capo_dynamodb.types.bulk_operation_status.deserialize_aws_json_1_0(
                data["BulkOperationStatus"]
            )
        )
    if data.get("TableDetails") is not None:
        import capo_dynamodb.types.bulk_operation_table_details

        out["table_details"] = (
            capo_dynamodb.types.bulk_operation_table_details.deserialize_aws_json_1_0(
                data["TableDetails"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("InputS3Configuration") is not None:
        import capo_dynamodb.types.input_s3_configuration

        out["input_s3_configuration"] = (
            capo_dynamodb.types.input_s3_configuration.deserialize_aws_json_1_0(
                data["InputS3Configuration"]
            )
        )
    if data.get("OutputS3Configuration") is not None:
        import capo_dynamodb.types.output_s3_configuration

        out["output_s3_configuration"] = (
            capo_dynamodb.types.output_s3_configuration.deserialize_aws_json_1_0(
                data["OutputS3Configuration"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_dynamodb.types.bulk_operation_start_time

        out["start_time"] = (
            capo_dynamodb.types.bulk_operation_start_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_dynamodb.types.bulk_operation_end_time

        out["end_time"] = (
            capo_dynamodb.types.bulk_operation_end_time.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    if data.get("ProcessedItemCount") is not None:
        out["processed_item_count"] = data["ProcessedItemCount"]
    else:
        out["processed_item_count"] = 0
    if data.get("ProcessedInputBytes") is not None:
        out["processed_input_bytes"] = data["ProcessedInputBytes"]
    if data.get("TotalInputBytes") is not None:
        out["total_input_bytes"] = data["TotalInputBytes"]
    if data.get("BulkOperationUsage") is not None:
        import capo_dynamodb.types.bulk_operation_usage_multiple

        out["bulk_operation_usage"] = (
            capo_dynamodb.types.bulk_operation_usage_multiple.deserialize_aws_json_1_0(
                data["BulkOperationUsage"]
            )
        )
    if data.get("FailedItemCount") is not None:
        out["failed_item_count"] = data["FailedItemCount"]
    else:
        out["failed_item_count"] = 0
    if data.get("FailureCode") is not None:
        out["failure_code"] = data["FailureCode"]
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    if data.get("MaxWriteRequestUnits") is not None:
        out["max_write_request_units"] = data["MaxWriteRequestUnits"]
    if data.get("PerformanceTier") is not None:
        import capo_dynamodb.types.bulk_operation_performance_tier

        out["performance_tier"] = (
            capo_dynamodb.types.bulk_operation_performance_tier.deserialize_aws_json_1_0(
                data["PerformanceTier"]
            )
        )
    return out
