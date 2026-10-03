"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DeleteApplicationInputProcessingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name
    import capo_kinesis_analytics.types.application_version_id
    import capo_kinesis_analytics.types.id


class DeleteApplicationInputProcessingConfigurationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>The Kinesis Analytics application name.</p>"""
    current_application_version_id: (
        "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>The version ID of the Kinesis Analytics application.</p>"""
    input_id: "capo_kinesis_analytics.types.id.Id"
    """<p>The ID of the input configuration from which to delete the input processing configuration. You can get a list of the input IDs for an application by using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteApplicationInputProcessingConfigurationRequest,
) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    out["InputId"] = value["input_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteApplicationInputProcessingConfigurationRequest:
    out: DeleteApplicationInputProcessingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DeleteApplicationInputProcessingConfigurationRequest.application_name required"
        )
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "DeleteApplicationInputProcessingConfigurationRequest.current_application_version_id required"
        )
    if data.get("InputId") is not None:
        out["input_id"] = data["InputId"]
    else:
        raise DeserializationError(
            "DeleteApplicationInputProcessingConfigurationRequest.input_id required"
        )
    return out
