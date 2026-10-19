"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#StartApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name
    import capo_kinesis_analytics.types.input_configurations


class StartApplicationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of the application.</p>"""
    input_configurations: (
        "capo_kinesis_analytics.types.input_configurations.InputConfigurations"
    )
    """<p>Identifies the specific input, by ID, that the application starts consuming. Amazon Kinesis Analytics starts reading the streaming source associated with the input. You can also specify where in the streaming source you want Amazon Kinesis Analytics to start reading.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    import capo_kinesis_analytics.types.input_configurations

    out["InputConfigurations"] = (
        capo_kinesis_analytics.types.input_configurations.serialize_aws_json_1_1(
            value["input_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartApplicationRequest:
    out: StartApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("InputConfigurations") is not None:
        import capo_kinesis_analytics.types.input_configurations

        out["input_configurations"] = (
            capo_kinesis_analytics.types.input_configurations.deserialize_aws_json_1_1(
                data["InputConfigurations"]
            )
        )
    else:
        out["input_configurations"] = []
    return out
