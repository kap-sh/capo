"""Generated from Smithy shape ``com.amazonaws.dynamodb#StartBulkPutItemsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_max_write_request_units
    import capo_dynamodb.types.bulk_operation_performance_tier
    import capo_dynamodb.types.client_token
    import capo_dynamodb.types.input_s3_configuration
    import capo_dynamodb.types.output_s3_configuration
    import capo_dynamodb.types.table_arn


class StartBulkPutItemsInput(TypedDict, closed=True):
    client_token: NotRequired["capo_dynamodb.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that ensures the bulk operation starts no more than one time. During the 8 hours after the initial request, repeated requests that use the same token and parameters return the same bulk operation. If a request reuses the token with different parameters, DynamoDB returns an <code>IdempotentParameterMismatchException</code>. If you omit the token, an Amazon Web Services SDK automatically generates one.</p>"""
    input_s3_configuration: (
        "capo_dynamodb.types.input_s3_configuration.InputS3Configuration"
    )
    """<p>The Amazon S3 location, data format, and compression settings for the input objects.</p>"""
    output_s3_configuration: (
        "capo_dynamodb.types.output_s3_configuration.OutputS3Configuration"
    )
    """<p>The Amazon S3 location, encryption settings, and output types for the bulk operation.</p>"""
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name or ARN of the existing DynamoDB table that receives the items.</p>"""
    max_write_request_units: NotRequired[
        "capo_dynamodb.types.bulk_operation_max_write_request_units.BulkOperationMaxWriteRequestUnits"
    ]
    """<p>The maximum rate, in write request units per second, at which the bulk operation attempts to write. The value must be at least 1,024. With this setting, you limit only the bulk operation; the table's provisioned or on-demand capacity settings don't change. The actual write rate can be lower.</p>"""
    performance_tier: NotRequired[
        "capo_dynamodb.types.bulk_operation_performance_tier.BulkOperationPerformanceTier"
    ]
    """<p>The performance tier for the bulk operation. Valid values are <code>STANDARD</code> and <code>ACCELERATED</code>. If you don't specify a value, the operation uses <code>STANDARD</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartBulkPutItemsInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import capo_dynamodb.types.input_s3_configuration

    out["InputS3Configuration"] = (
        capo_dynamodb.types.input_s3_configuration.serialize_aws_json_1_0(
            value["input_s3_configuration"]
        )
    )
    import capo_dynamodb.types.output_s3_configuration

    out["OutputS3Configuration"] = (
        capo_dynamodb.types.output_s3_configuration.serialize_aws_json_1_0(
            value["output_s3_configuration"]
        )
    )
    out["TableName"] = value["table_name"]
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


def deserialize_aws_json_1_0(data: dict) -> StartBulkPutItemsInput:
    out: StartBulkPutItemsInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("InputS3Configuration") is not None:
        import capo_dynamodb.types.input_s3_configuration

        out["input_s3_configuration"] = (
            capo_dynamodb.types.input_s3_configuration.deserialize_aws_json_1_0(
                data["InputS3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "StartBulkPutItemsInput.input_s3_configuration required"
        )
    if data.get("OutputS3Configuration") is not None:
        import capo_dynamodb.types.output_s3_configuration

        out["output_s3_configuration"] = (
            capo_dynamodb.types.output_s3_configuration.deserialize_aws_json_1_0(
                data["OutputS3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "StartBulkPutItemsInput.output_s3_configuration required"
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
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
