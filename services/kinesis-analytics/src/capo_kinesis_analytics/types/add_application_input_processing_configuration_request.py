"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#AddApplicationInputProcessingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name
    import capo_kinesis_analytics.types.application_version_id
    import capo_kinesis_analytics.types.id
    import capo_kinesis_analytics.types.input_processing_configuration


class AddApplicationInputProcessingConfigurationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of the application to which you want to add the input processing configuration.</p>"""
    current_application_version_id: (
        "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>Version of the application to which you want to add the input processing configuration. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>"""
    input_id: "capo_kinesis_analytics.types.id.Id"
    """<p>The ID of the input configuration to add the input processing configuration to. You can get a list of the input IDs for an application using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation.</p>"""
    input_processing_configuration: "capo_kinesis_analytics.types.input_processing_configuration.InputProcessingConfiguration"
    """<p>The <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html">InputProcessingConfiguration</a> to add to the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AddApplicationInputProcessingConfigurationRequest,
) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    out["InputId"] = value["input_id"]
    import capo_kinesis_analytics.types.input_processing_configuration

    out["InputProcessingConfiguration"] = (
        capo_kinesis_analytics.types.input_processing_configuration.serialize_aws_json_1_1(
            value["input_processing_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AddApplicationInputProcessingConfigurationRequest:
    out: AddApplicationInputProcessingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "AddApplicationInputProcessingConfigurationRequest.application_name required"
        )
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "AddApplicationInputProcessingConfigurationRequest.current_application_version_id required"
        )
    if data.get("InputId") is not None:
        out["input_id"] = data["InputId"]
    else:
        raise DeserializationError(
            "AddApplicationInputProcessingConfigurationRequest.input_id required"
        )
    if data.get("InputProcessingConfiguration") is not None:
        import capo_kinesis_analytics.types.input_processing_configuration

        out["input_processing_configuration"] = (
            capo_kinesis_analytics.types.input_processing_configuration.deserialize_aws_json_1_1(
                data["InputProcessingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AddApplicationInputProcessingConfigurationRequest.input_processing_configuration required"
        )
    return out
