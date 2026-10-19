"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisStreamingDestinationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.enable_kinesis_streaming_configuration
    import capo_dynamodb.types.stream_arn
    import capo_dynamodb.types.table_arn


class KinesisStreamingDestinationInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the DynamoDB table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    stream_arn: "capo_dynamodb.types.stream_arn.StreamArn"
    """<p>The ARN for a Kinesis data stream.</p>"""
    enable_kinesis_streaming_configuration: NotRequired[
        "capo_dynamodb.types.enable_kinesis_streaming_configuration.EnableKinesisStreamingConfiguration"
    ]
    """<p>The source for the Kinesis streaming information that is being enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KinesisStreamingDestinationInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    out["StreamArn"] = value["stream_arn"]
    if "enable_kinesis_streaming_configuration" in value:
        import capo_dynamodb.types.enable_kinesis_streaming_configuration

        out["EnableKinesisStreamingConfiguration"] = (
            capo_dynamodb.types.enable_kinesis_streaming_configuration.serialize_aws_json_1_0(
                value["enable_kinesis_streaming_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KinesisStreamingDestinationInput:
    out: KinesisStreamingDestinationInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("StreamArn") is not None:
        out["stream_arn"] = data["StreamArn"]
    else:
        out["stream_arn"] = ""
    if data.get("EnableKinesisStreamingConfiguration") is not None:
        import capo_dynamodb.types.enable_kinesis_streaming_configuration

        out["enable_kinesis_streaming_configuration"] = (
            capo_dynamodb.types.enable_kinesis_streaming_configuration.deserialize_aws_json_1_0(
                data["EnableKinesisStreamingConfiguration"]
            )
        )
    return out
