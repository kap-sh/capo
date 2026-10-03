"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.id
    import capo_kinesis_analytics.types.input_starting_position_configuration


class InputConfiguration(TypedDict, closed=True):
    id: "capo_kinesis_analytics.types.id.Id"
    """<p>Input source ID. You can get this ID by calling the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation.</p>"""
    input_starting_position_configuration: "capo_kinesis_analytics.types.input_starting_position_configuration.InputStartingPositionConfiguration"
    """<p>Point at which you want the application to start processing records from the streaming source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputConfiguration) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_kinesis_analytics.types.input_starting_position_configuration

    out["InputStartingPositionConfiguration"] = (
        capo_kinesis_analytics.types.input_starting_position_configuration.serialize_aws_json_1_1(
            value["input_starting_position_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputConfiguration:
    out: InputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("InputConfiguration.id required")
    if data.get("InputStartingPositionConfiguration") is not None:
        import capo_kinesis_analytics.types.input_starting_position_configuration

        out["input_starting_position_configuration"] = (
            capo_kinesis_analytics.types.input_starting_position_configuration.deserialize_aws_json_1_1(
                data["InputStartingPositionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InputConfiguration.input_starting_position_configuration required"
        )
    return out
