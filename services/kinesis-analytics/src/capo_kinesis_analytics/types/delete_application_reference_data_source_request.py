"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DeleteApplicationReferenceDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name
    import capo_kinesis_analytics.types.application_version_id
    import capo_kinesis_analytics.types.id


class DeleteApplicationReferenceDataSourceRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of an existing application.</p>"""
    current_application_version_id: (
        "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>Version of the application. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>"""
    reference_id: "capo_kinesis_analytics.types.id.Id"
    """<p>ID of the reference data source. When you add a reference data source to your application using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html">AddApplicationReferenceDataSource</a>, Amazon Kinesis Analytics assigns an ID. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the reference ID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationReferenceDataSourceRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    out["ReferenceId"] = value["reference_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationReferenceDataSourceRequest:
    out: DeleteApplicationReferenceDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DeleteApplicationReferenceDataSourceRequest.application_name required"
        )
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "DeleteApplicationReferenceDataSourceRequest.current_application_version_id required"
        )
    if data.get("ReferenceId") is not None:
        out["reference_id"] = data["ReferenceId"]
    else:
        raise DeserializationError(
            "DeleteApplicationReferenceDataSourceRequest.reference_id required"
        )
    return out
