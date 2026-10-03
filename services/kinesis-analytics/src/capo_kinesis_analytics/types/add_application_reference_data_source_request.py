"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#AddApplicationReferenceDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_name
    import capo_kinesis_analytics.types.application_version_id
    import capo_kinesis_analytics.types.reference_data_source


class AddApplicationReferenceDataSourceRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of an existing application.</p>"""
    current_application_version_id: (
        "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>Version of the application for which you are adding the reference data source. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>"""
    reference_data_source: (
        "capo_kinesis_analytics.types.reference_data_source.ReferenceDataSource"
    )
    """<p>The reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. You must also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your behalf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationReferenceDataSourceRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    import capo_kinesis_analytics.types.reference_data_source

    out["ReferenceDataSource"] = (
        capo_kinesis_analytics.types.reference_data_source.serialize_aws_json_1_1(
            value["reference_data_source"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationReferenceDataSourceRequest:
    out: AddApplicationReferenceDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "AddApplicationReferenceDataSourceRequest.application_name required"
        )
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "AddApplicationReferenceDataSourceRequest.current_application_version_id required"
        )
    if data.get("ReferenceDataSource") is not None:
        import capo_kinesis_analytics.types.reference_data_source

        out["reference_data_source"] = (
            capo_kinesis_analytics.types.reference_data_source.deserialize_aws_json_1_1(
                data["ReferenceDataSource"]
            )
        )
    else:
        raise DeserializationError(
            "AddApplicationReferenceDataSourceRequest.reference_data_source required"
        )
    return out
