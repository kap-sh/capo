"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#AddApplicationCloudWatchLoggingOptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option
    import capo_kinesis_analytics_v2.types.conditional_token


class AddApplicationCloudWatchLoggingOptionRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The Kinesis Data Analytics application name.</p>"""
    current_application_version_id: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The version ID of the SQL-based Kinesis Data Analytics application. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>.You can retrieve the application version ID using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""
    cloud_watch_logging_option: "capo_kinesis_analytics_v2.types.cloud_watch_logging_option.CloudWatchLoggingOption"
    """<p>Provides the Amazon CloudWatch log stream Amazon Resource Name (ARN). </p>"""
    conditional_token: NotRequired[
        "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
    ]
    """<p>A value you use to implement strong concurrency for application updates. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationCloudWatchLoggingOptionRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "current_application_version_id" in value:
        out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option

    out["CloudWatchLoggingOption"] = (
        capo_kinesis_analytics_v2.types.cloud_watch_logging_option.serialize_aws_json_1_1(
            value["cloud_watch_logging_option"]
        )
    )
    if "conditional_token" in value:
        out["ConditionalToken"] = value["conditional_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AddApplicationCloudWatchLoggingOptionRequest:
    out: AddApplicationCloudWatchLoggingOptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    if data.get("CloudWatchLoggingOption") is not None:
        import capo_kinesis_analytics_v2.types.cloud_watch_logging_option

        out["cloud_watch_logging_option"] = (
            capo_kinesis_analytics_v2.types.cloud_watch_logging_option.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOption"]
            )
        )
    else:
        raise DeserializationError(
            "AddApplicationCloudWatchLoggingOptionRequest.cloud_watch_logging_option required"
        )
    if data.get("ConditionalToken") is not None:
        out["conditional_token"] = data["ConditionalToken"]
    return out
