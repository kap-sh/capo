"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.destination_schema
    import capo_kinesis_analytics.types.in_app_stream_name
    import capo_kinesis_analytics.types.kinesis_firehose_output
    import capo_kinesis_analytics.types.kinesis_streams_output
    import capo_kinesis_analytics.types.lambda_output


class Output(TypedDict, closed=True):
    name: "capo_kinesis_analytics.types.in_app_stream_name.InAppStreamName"
    """<p>Name of the in-application stream.</p>"""
    kinesis_streams_output: NotRequired[
        "capo_kinesis_analytics.types.kinesis_streams_output.KinesisStreamsOutput"
    ]
    """<p>Identifies an Amazon Kinesis stream as the destination.</p>"""
    kinesis_firehose_output: NotRequired[
        "capo_kinesis_analytics.types.kinesis_firehose_output.KinesisFirehoseOutput"
    ]
    """<p>Identifies an Amazon Kinesis Firehose delivery stream as the destination.</p>"""
    lambda_output: NotRequired[
        "capo_kinesis_analytics.types.lambda_output.LambdaOutput"
    ]
    """<p>Identifies an AWS Lambda function as the destination.</p>"""
    destination_schema: (
        "capo_kinesis_analytics.types.destination_schema.DestinationSchema"
    )
    """<p>Describes the data format when records are written to the destination. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html">Configuring Application Output</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Output) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "kinesis_streams_output" in value:
        import capo_kinesis_analytics.types.kinesis_streams_output

        out["KinesisStreamsOutput"] = (
            capo_kinesis_analytics.types.kinesis_streams_output.serialize_aws_json_1_1(
                value["kinesis_streams_output"]
            )
        )
    if "kinesis_firehose_output" in value:
        import capo_kinesis_analytics.types.kinesis_firehose_output

        out["KinesisFirehoseOutput"] = (
            capo_kinesis_analytics.types.kinesis_firehose_output.serialize_aws_json_1_1(
                value["kinesis_firehose_output"]
            )
        )
    if "lambda_output" in value:
        import capo_kinesis_analytics.types.lambda_output

        out["LambdaOutput"] = (
            capo_kinesis_analytics.types.lambda_output.serialize_aws_json_1_1(
                value["lambda_output"]
            )
        )
    import capo_kinesis_analytics.types.destination_schema

    out["DestinationSchema"] = (
        capo_kinesis_analytics.types.destination_schema.serialize_aws_json_1_1(
            value["destination_schema"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Output:
    out: Output = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Output.name required")
    if data.get("KinesisStreamsOutput") is not None:
        import capo_kinesis_analytics.types.kinesis_streams_output

        out["kinesis_streams_output"] = (
            capo_kinesis_analytics.types.kinesis_streams_output.deserialize_aws_json_1_1(
                data["KinesisStreamsOutput"]
            )
        )
    if data.get("KinesisFirehoseOutput") is not None:
        import capo_kinesis_analytics.types.kinesis_firehose_output

        out["kinesis_firehose_output"] = (
            capo_kinesis_analytics.types.kinesis_firehose_output.deserialize_aws_json_1_1(
                data["KinesisFirehoseOutput"]
            )
        )
    if data.get("LambdaOutput") is not None:
        import capo_kinesis_analytics.types.lambda_output

        out["lambda_output"] = (
            capo_kinesis_analytics.types.lambda_output.deserialize_aws_json_1_1(
                data["LambdaOutput"]
            )
        )
    if data.get("DestinationSchema") is not None:
        import capo_kinesis_analytics.types.destination_schema

        out["destination_schema"] = (
            capo_kinesis_analytics.types.destination_schema.deserialize_aws_json_1_1(
                data["DestinationSchema"]
            )
        )
    else:
        raise DeserializationError("Output.destination_schema required")
    return out
