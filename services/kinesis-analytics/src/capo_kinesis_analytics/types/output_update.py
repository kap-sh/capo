"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#OutputUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.destination_schema
    import capo_kinesis_analytics.types.id
    import capo_kinesis_analytics.types.in_app_stream_name
    import capo_kinesis_analytics.types.kinesis_firehose_output_update
    import capo_kinesis_analytics.types.kinesis_streams_output_update
    import capo_kinesis_analytics.types.lambda_output_update


class OutputUpdate(TypedDict, closed=True):
    output_id: "capo_kinesis_analytics.types.id.Id"
    """<p>Identifies the specific output configuration that you want to update.</p>"""
    name_update: NotRequired[
        "capo_kinesis_analytics.types.in_app_stream_name.InAppStreamName"
    ]
    """<p>If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.</p>"""
    kinesis_streams_output_update: NotRequired[
        "capo_kinesis_analytics.types.kinesis_streams_output_update.KinesisStreamsOutputUpdate"
    ]
    """<p>Describes an Amazon Kinesis stream as the destination for the output.</p>"""
    kinesis_firehose_output_update: NotRequired[
        "capo_kinesis_analytics.types.kinesis_firehose_output_update.KinesisFirehoseOutputUpdate"
    ]
    """<p>Describes an Amazon Kinesis Firehose delivery stream as the destination for the output.</p>"""
    lambda_output_update: NotRequired[
        "capo_kinesis_analytics.types.lambda_output_update.LambdaOutputUpdate"
    ]
    """<p>Describes an AWS Lambda function as the destination for the output.</p>"""
    destination_schema_update: NotRequired[
        "capo_kinesis_analytics.types.destination_schema.DestinationSchema"
    ]
    """<p>Describes the data format when records are written to the destination. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html">Configuring Application Output</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputUpdate) -> dict:
    out: dict = {}
    out["OutputId"] = value["output_id"]
    if "name_update" in value:
        out["NameUpdate"] = value["name_update"]
    if "kinesis_streams_output_update" in value:
        import capo_kinesis_analytics.types.kinesis_streams_output_update

        out["KinesisStreamsOutputUpdate"] = (
            capo_kinesis_analytics.types.kinesis_streams_output_update.serialize_aws_json_1_1(
                value["kinesis_streams_output_update"]
            )
        )
    if "kinesis_firehose_output_update" in value:
        import capo_kinesis_analytics.types.kinesis_firehose_output_update

        out["KinesisFirehoseOutputUpdate"] = (
            capo_kinesis_analytics.types.kinesis_firehose_output_update.serialize_aws_json_1_1(
                value["kinesis_firehose_output_update"]
            )
        )
    if "lambda_output_update" in value:
        import capo_kinesis_analytics.types.lambda_output_update

        out["LambdaOutputUpdate"] = (
            capo_kinesis_analytics.types.lambda_output_update.serialize_aws_json_1_1(
                value["lambda_output_update"]
            )
        )
    if "destination_schema_update" in value:
        import capo_kinesis_analytics.types.destination_schema

        out["DestinationSchemaUpdate"] = (
            capo_kinesis_analytics.types.destination_schema.serialize_aws_json_1_1(
                value["destination_schema_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputUpdate:
    out: OutputUpdate = {}  # type: ignore[typeddict-item]
    if data.get("OutputId") is not None:
        out["output_id"] = data["OutputId"]
    else:
        raise DeserializationError("OutputUpdate.output_id required")
    if data.get("NameUpdate") is not None:
        out["name_update"] = data["NameUpdate"]
    if data.get("KinesisStreamsOutputUpdate") is not None:
        import capo_kinesis_analytics.types.kinesis_streams_output_update

        out["kinesis_streams_output_update"] = (
            capo_kinesis_analytics.types.kinesis_streams_output_update.deserialize_aws_json_1_1(
                data["KinesisStreamsOutputUpdate"]
            )
        )
    if data.get("KinesisFirehoseOutputUpdate") is not None:
        import capo_kinesis_analytics.types.kinesis_firehose_output_update

        out["kinesis_firehose_output_update"] = (
            capo_kinesis_analytics.types.kinesis_firehose_output_update.deserialize_aws_json_1_1(
                data["KinesisFirehoseOutputUpdate"]
            )
        )
    if data.get("LambdaOutputUpdate") is not None:
        import capo_kinesis_analytics.types.lambda_output_update

        out["lambda_output_update"] = (
            capo_kinesis_analytics.types.lambda_output_update.deserialize_aws_json_1_1(
                data["LambdaOutputUpdate"]
            )
        )
    if data.get("DestinationSchemaUpdate") is not None:
        import capo_kinesis_analytics.types.destination_schema

        out["destination_schema_update"] = (
            capo_kinesis_analytics.types.destination_schema.deserialize_aws_json_1_1(
                data["DestinationSchemaUpdate"]
            )
        )
    return out
