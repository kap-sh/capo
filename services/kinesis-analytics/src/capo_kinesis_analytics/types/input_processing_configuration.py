"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputProcessingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.input_lambda_processor


class InputProcessingConfiguration(TypedDict, closed=True):
    input_lambda_processor: (
        "capo_kinesis_analytics.types.input_lambda_processor.InputLambdaProcessor"
    )
    """<p>The <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html">InputLambdaProcessor</a> that is used to preprocess the records in the stream before being processed by your application code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputProcessingConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis_analytics.types.input_lambda_processor

    out["InputLambdaProcessor"] = (
        capo_kinesis_analytics.types.input_lambda_processor.serialize_aws_json_1_1(
            value["input_lambda_processor"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputProcessingConfiguration:
    out: InputProcessingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InputLambdaProcessor") is not None:
        import capo_kinesis_analytics.types.input_lambda_processor

        out["input_lambda_processor"] = (
            capo_kinesis_analytics.types.input_lambda_processor.deserialize_aws_json_1_1(
                data["InputLambdaProcessor"]
            )
        )
    else:
        raise DeserializationError(
            "InputProcessingConfiguration.input_lambda_processor required"
        )
    return out
