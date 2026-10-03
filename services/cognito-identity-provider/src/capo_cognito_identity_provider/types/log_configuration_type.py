"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#LogConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.cloud_watch_logs_configuration_type
    import capo_cognito_identity_provider.types.event_source_name
    import capo_cognito_identity_provider.types.firehose_configuration_type
    import capo_cognito_identity_provider.types.log_level
    import capo_cognito_identity_provider.types.s3_configuration_type


class LogConfigurationType(TypedDict, closed=True):
    log_level: "capo_cognito_identity_provider.types.log_level.LogLevel"
    """<p>The <code>errorlevel</code> selection of logs that a user pool sends for detailed activity logging. To send <code>userNotification</code> activity with <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html">information about message delivery</a>, choose <code>ERROR</code> with <code>CloudWatchLogsConfiguration</code>. To send <code>userAuthEvents</code> activity with user logs from threat protection with the Plus feature plan, choose <code>INFO</code> with one of <code>CloudWatchLogsConfiguration</code>, <code>FirehoseConfiguration</code>, or <code>S3Configuration</code>.</p>"""
    event_source: (
        "capo_cognito_identity_provider.types.event_source_name.EventSourceName"
    )
    """<p>The source of events that your user pool sends for logging. To send error-level logs about user notification activity, set to <code>userNotification</code>. To send info-level logs about threat-protection user activity in user pools with the Plus feature plan, set to <code>userAuthEvents</code>.</p>"""
    cloud_watch_logs_configuration: NotRequired[
        "capo_cognito_identity_provider.types.cloud_watch_logs_configuration_type.CloudWatchLogsConfigurationType"
    ]
    """<p>The CloudWatch log group destination of user pool detailed activity logs, or of user activity log export with threat protection.</p>"""
    s3_configuration: NotRequired[
        "capo_cognito_identity_provider.types.s3_configuration_type.S3ConfigurationType"
    ]
    """<p>The Amazon S3 bucket destination of user activity log export with threat protection. To activate this setting, your user pool must be on the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html"> Plus tier</a>.</p>"""
    firehose_configuration: NotRequired[
        "capo_cognito_identity_provider.types.firehose_configuration_type.FirehoseConfigurationType"
    ]
    """<p>The Amazon Data Firehose stream destination of user activity log export with threat protection. To activate this setting, your user pool must be on the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html"> Plus tier</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogConfigurationType) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.log_level

    out["LogLevel"] = (
        capo_cognito_identity_provider.types.log_level.serialize_aws_json_1_1(
            value["log_level"]
        )
    )
    import capo_cognito_identity_provider.types.event_source_name

    out["EventSource"] = (
        capo_cognito_identity_provider.types.event_source_name.serialize_aws_json_1_1(
            value["event_source"]
        )
    )
    if "cloud_watch_logs_configuration" in value:
        import capo_cognito_identity_provider.types.cloud_watch_logs_configuration_type

        out["CloudWatchLogsConfiguration"] = (
            capo_cognito_identity_provider.types.cloud_watch_logs_configuration_type.serialize_aws_json_1_1(
                value["cloud_watch_logs_configuration"]
            )
        )
    if "s3_configuration" in value:
        import capo_cognito_identity_provider.types.s3_configuration_type

        out["S3Configuration"] = (
            capo_cognito_identity_provider.types.s3_configuration_type.serialize_aws_json_1_1(
                value["s3_configuration"]
            )
        )
    if "firehose_configuration" in value:
        import capo_cognito_identity_provider.types.firehose_configuration_type

        out["FirehoseConfiguration"] = (
            capo_cognito_identity_provider.types.firehose_configuration_type.serialize_aws_json_1_1(
                value["firehose_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogConfigurationType:
    out: LogConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("LogLevel") is not None:
        import capo_cognito_identity_provider.types.log_level

        out["log_level"] = (
            capo_cognito_identity_provider.types.log_level.deserialize_aws_json_1_1(
                data["LogLevel"]
            )
        )
    else:
        raise DeserializationError("LogConfigurationType.log_level required")
    if data.get("EventSource") is not None:
        import capo_cognito_identity_provider.types.event_source_name

        out["event_source"] = (
            capo_cognito_identity_provider.types.event_source_name.deserialize_aws_json_1_1(
                data["EventSource"]
            )
        )
    else:
        raise DeserializationError("LogConfigurationType.event_source required")
    if data.get("CloudWatchLogsConfiguration") is not None:
        import capo_cognito_identity_provider.types.cloud_watch_logs_configuration_type

        out["cloud_watch_logs_configuration"] = (
            capo_cognito_identity_provider.types.cloud_watch_logs_configuration_type.deserialize_aws_json_1_1(
                data["CloudWatchLogsConfiguration"]
            )
        )
    if data.get("S3Configuration") is not None:
        import capo_cognito_identity_provider.types.s3_configuration_type

        out["s3_configuration"] = (
            capo_cognito_identity_provider.types.s3_configuration_type.deserialize_aws_json_1_1(
                data["S3Configuration"]
            )
        )
    if data.get("FirehoseConfiguration") is not None:
        import capo_cognito_identity_provider.types.firehose_configuration_type

        out["firehose_configuration"] = (
            capo_cognito_identity_provider.types.firehose_configuration_type.deserialize_aws_json_1_1(
                data["FirehoseConfiguration"]
            )
        )
    return out
