"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DeleteApplicationOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name
    import capo_kinesis_analytics.types.application_version_id
    import capo_kinesis_analytics.types.id


class DeleteApplicationOutputRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Amazon Kinesis Analytics application name.</p>"""
    current_application_version_id: (
        "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>Amazon Kinesis Analytics application version. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. </p>"""
    output_id: "capo_kinesis_analytics.types.id.Id"
    """<p>The ID of the configuration to delete. Each output configuration that is added to the application, either when the application is created or later using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationOutput.html">AddApplicationOutput</a> operation, has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the specific <code>OutputId</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationOutputRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    out["OutputId"] = value["output_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationOutputRequest:
    out: DeleteApplicationOutputRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DeleteApplicationOutputRequest.application_name required"
        )
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "DeleteApplicationOutputRequest.current_application_version_id required"
        )
    if data.get("OutputId") is not None:
        out["output_id"] = data["OutputId"]
    else:
        raise DeserializationError("DeleteApplicationOutputRequest.output_id required")
    return out
