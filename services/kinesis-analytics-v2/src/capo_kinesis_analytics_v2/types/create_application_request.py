"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_configuration
    import capo_kinesis_analytics_v2.types.application_description
    import capo_kinesis_analytics_v2.types.application_mode
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_options
    import capo_kinesis_analytics_v2.types.role_arn
    import capo_kinesis_analytics_v2.types.runtime_environment
    import capo_kinesis_analytics_v2.types.tags


class CreateApplicationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of your application (for example, <code>sample-app</code>).</p>"""
    application_description: NotRequired[
        "capo_kinesis_analytics_v2.types.application_description.ApplicationDescription"
    ]
    """<p>A summary description of the application.</p>"""
    runtime_environment: (
        "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
    )
    """<p>The runtime environment for the application.</p>"""
    service_execution_role: "capo_kinesis_analytics_v2.types.role_arn.RoleARN"
    """<p>The IAM role used by the application to access Kinesis data streams, Kinesis Data Firehose delivery streams, Amazon S3 objects, and other external resources.</p>"""
    application_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.application_configuration.ApplicationConfiguration"
    ]
    """<p>Use this parameter to configure the application.</p>"""
    cloud_watch_logging_options: NotRequired[
        "capo_kinesis_analytics_v2.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>Use this parameter to configure an Amazon CloudWatch log stream to monitor application configuration errors. </p>"""
    tags: NotRequired["capo_kinesis_analytics_v2.types.tags.Tags"]
    """<p>A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html">Using Tagging</a>.</p>"""
    application_mode: NotRequired[
        "capo_kinesis_analytics_v2.types.application_mode.ApplicationMode"
    ]
    """<p>Use the <code>STREAMING</code> mode to create a Managed Service for Apache Flink application. To create a Managed Service for Apache Flink Studio notebook, use the <code>INTERACTIVE</code> mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "application_description" in value:
        out["ApplicationDescription"] = value["application_description"]
    import capo_kinesis_analytics_v2.types.runtime_environment

    out["RuntimeEnvironment"] = (
        capo_kinesis_analytics_v2.types.runtime_environment.serialize_aws_json_1_1(
            value["runtime_environment"]
        )
    )
    out["ServiceExecutionRole"] = value["service_execution_role"]
    if "application_configuration" in value:
        import capo_kinesis_analytics_v2.types.application_configuration

        out["ApplicationConfiguration"] = (
            capo_kinesis_analytics_v2.types.application_configuration.serialize_aws_json_1_1(
                value["application_configuration"]
            )
        )
    if "cloud_watch_logging_options" in value:
        import capo_kinesis_analytics_v2.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            capo_kinesis_analytics_v2.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "tags" in value:
        import capo_kinesis_analytics_v2.types.tags

        out["Tags"] = capo_kinesis_analytics_v2.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "application_mode" in value:
        import capo_kinesis_analytics_v2.types.application_mode

        out["ApplicationMode"] = (
            capo_kinesis_analytics_v2.types.application_mode.serialize_aws_json_1_1(
                value["application_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError("CreateApplicationRequest.application_name required")
    if data.get("ApplicationDescription") is not None:
        out["application_description"] = data["ApplicationDescription"]
    if data.get("RuntimeEnvironment") is not None:
        import capo_kinesis_analytics_v2.types.runtime_environment

        out["runtime_environment"] = (
            capo_kinesis_analytics_v2.types.runtime_environment.deserialize_aws_json_1_1(
                data["RuntimeEnvironment"]
            )
        )
    else:
        raise DeserializationError(
            "CreateApplicationRequest.runtime_environment required"
        )
    if data.get("ServiceExecutionRole") is not None:
        out["service_execution_role"] = data["ServiceExecutionRole"]
    else:
        raise DeserializationError(
            "CreateApplicationRequest.service_execution_role required"
        )
    if data.get("ApplicationConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.application_configuration

        out["application_configuration"] = (
            capo_kinesis_analytics_v2.types.application_configuration.deserialize_aws_json_1_1(
                data["ApplicationConfiguration"]
            )
        )
    if data.get("CloudWatchLoggingOptions") is not None:
        import capo_kinesis_analytics_v2.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            capo_kinesis_analytics_v2.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if data.get("Tags") is not None:
        import capo_kinesis_analytics_v2.types.tags

        out["tags"] = capo_kinesis_analytics_v2.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ApplicationMode") is not None:
        import capo_kinesis_analytics_v2.types.application_mode

        out["application_mode"] = (
            capo_kinesis_analytics_v2.types.application_mode.deserialize_aws_json_1_1(
                data["ApplicationMode"]
            )
        )
    return out
