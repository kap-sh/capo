"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#AddApplicationInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name
    import capo_kinesis_analytics.types.application_version_id
    import capo_kinesis_analytics.types.input


class AddApplicationInputRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of your existing Amazon Kinesis Analytics application to which you want to add the streaming source.</p>"""
    current_application_version_id: (
        "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>Current version of your Amazon Kinesis Analytics application. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to find the current application version.</p>"""
    input: "capo_kinesis_analytics.types.input.Input"
    """<p>The <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Input.html">Input</a> to add.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationInputRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    import capo_kinesis_analytics.types.input

    out["Input"] = capo_kinesis_analytics.types.input.serialize_aws_json_1_1(
        value["input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationInputRequest:
    out: AddApplicationInputRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "AddApplicationInputRequest.application_name required"
        )
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "AddApplicationInputRequest.current_application_version_id required"
        )
    if data.get("Input") is not None:
        import capo_kinesis_analytics.types.input

        out["input"] = capo_kinesis_analytics.types.input.deserialize_aws_json_1_1(
            data["Input"]
        )
    else:
        raise DeserializationError("AddApplicationInputRequest.input required")
    return out
