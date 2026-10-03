"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputProcessingConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.input_lambda_processor_update


class InputProcessingConfigurationUpdate(TypedDict, closed=True):
    input_lambda_processor_update: "capo_kinesis_analytics.types.input_lambda_processor_update.InputLambdaProcessorUpdate"
    """<p>Provides update information for an <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html">InputLambdaProcessor</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputProcessingConfigurationUpdate) -> dict:
    out: dict = {}
    import capo_kinesis_analytics.types.input_lambda_processor_update

    out["InputLambdaProcessorUpdate"] = (
        capo_kinesis_analytics.types.input_lambda_processor_update.serialize_aws_json_1_1(
            value["input_lambda_processor_update"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputProcessingConfigurationUpdate:
    out: InputProcessingConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("InputLambdaProcessorUpdate") is not None:
        import capo_kinesis_analytics.types.input_lambda_processor_update

        out["input_lambda_processor_update"] = (
            capo_kinesis_analytics.types.input_lambda_processor_update.deserialize_aws_json_1_1(
                data["InputLambdaProcessorUpdate"]
            )
        )
    else:
        raise DeserializationError(
            "InputProcessingConfigurationUpdate.input_lambda_processor_update required"
        )
    return out
