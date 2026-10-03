"""Generated from Smithy shape ``com.amazonaws.firehose#SplunkDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.hec_acknowledgment_timeout_in_seconds
    import capo_firehose.types.hec_endpoint
    import capo_firehose.types.hec_endpoint_type
    import capo_firehose.types.hec_token
    import capo_firehose.types.processing_configuration
    import capo_firehose.types.s3_destination_configuration
    import capo_firehose.types.secrets_manager_configuration
    import capo_firehose.types.splunk_buffering_hints
    import capo_firehose.types.splunk_retry_options
    import capo_firehose.types.splunk_s3_backup_mode


class SplunkDestinationConfiguration(TypedDict, closed=True):
    hec_endpoint: "capo_firehose.types.hec_endpoint.HECEndpoint"
    """<p>The HTTP Event Collector (HEC) endpoint to which Firehose sends your data.</p>"""
    hec_endpoint_type: "capo_firehose.types.hec_endpoint_type.HECEndpointType"
    """<p>This type can be either "Raw" or "Event."</p>"""
    hec_token: NotRequired["capo_firehose.types.hec_token.HECToken"]
    """<p>This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.</p>"""
    hec_acknowledgment_timeout_in_seconds: NotRequired[
        "capo_firehose.types.hec_acknowledgment_timeout_in_seconds.HECAcknowledgmentTimeoutInSeconds"
    ]
    """<p>The amount of time that Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Firehose either tries to send the data again or considers it an error, based on your retry settings.</p>"""
    retry_options: NotRequired[
        "capo_firehose.types.splunk_retry_options.SplunkRetryOptions"
    ]
    """<p>The retry behavior in case Firehose is unable to deliver data to Splunk, or if it doesn't receive an acknowledgment of receipt from Splunk.</p>"""
    s3_backup_mode: NotRequired[
        "capo_firehose.types.splunk_s3_backup_mode.SplunkS3BackupMode"
    ]
    """<p>Defines how documents should be delivered to Amazon S3. When set to <code>FailedEventsOnly</code>, Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to <code>AllEvents</code>, Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. The default value is <code>FailedEventsOnly</code>.</p> <p>You can update this backup mode from <code>FailedEventsOnly</code> to <code>AllEvents</code>. You can't update it from <code>AllEvents</code> to <code>FailedEventsOnly</code>.</p>"""
    s3_configuration: (
        "capo_firehose.types.s3_destination_configuration.S3DestinationConfiguration"
    )
    """<p>The configuration for the backup Amazon S3 location.</p>"""
    processing_configuration: NotRequired[
        "capo_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    """<p>The data processing configuration.</p>"""
    cloud_watch_logging_options: NotRequired[
        "capo_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>The Amazon CloudWatch logging options for your Firehose stream.</p>"""
    buffering_hints: NotRequired[
        "capo_firehose.types.splunk_buffering_hints.SplunkBufferingHints"
    ]
    """<p>The buffering options. If no value is specified, the default values for Splunk are used.</p>"""
    secrets_manager_configuration: NotRequired[
        "capo_firehose.types.secrets_manager_configuration.SecretsManagerConfiguration"
    ]
    """<p> The configuration that defines how you access secrets for Splunk. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplunkDestinationConfiguration) -> dict:
    out: dict = {}
    out["HECEndpoint"] = value["hec_endpoint"]
    import capo_firehose.types.hec_endpoint_type

    out["HECEndpointType"] = (
        capo_firehose.types.hec_endpoint_type.serialize_aws_json_1_1(
            value["hec_endpoint_type"]
        )
    )
    if "hec_token" in value:
        out["HECToken"] = value["hec_token"]
    if "hec_acknowledgment_timeout_in_seconds" in value:
        out["HECAcknowledgmentTimeoutInSeconds"] = value[
            "hec_acknowledgment_timeout_in_seconds"
        ]
    if "retry_options" in value:
        import capo_firehose.types.splunk_retry_options

        out["RetryOptions"] = (
            capo_firehose.types.splunk_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import capo_firehose.types.splunk_s3_backup_mode

        out["S3BackupMode"] = (
            capo_firehose.types.splunk_s3_backup_mode.serialize_aws_json_1_1(
                value["s3_backup_mode"]
            )
        )
    import capo_firehose.types.s3_destination_configuration

    out["S3Configuration"] = (
        capo_firehose.types.s3_destination_configuration.serialize_aws_json_1_1(
            value["s3_configuration"]
        )
    )
    if "processing_configuration" in value:
        import capo_firehose.types.processing_configuration

        out["ProcessingConfiguration"] = (
            capo_firehose.types.processing_configuration.serialize_aws_json_1_1(
                value["processing_configuration"]
            )
        )
    if "cloud_watch_logging_options" in value:
        import capo_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            capo_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "buffering_hints" in value:
        import capo_firehose.types.splunk_buffering_hints

        out["BufferingHints"] = (
            capo_firehose.types.splunk_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "secrets_manager_configuration" in value:
        import capo_firehose.types.secrets_manager_configuration

        out["SecretsManagerConfiguration"] = (
            capo_firehose.types.secrets_manager_configuration.serialize_aws_json_1_1(
                value["secrets_manager_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SplunkDestinationConfiguration:
    out: SplunkDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("HECEndpoint") is not None:
        out["hec_endpoint"] = data["HECEndpoint"]
    else:
        raise DeserializationError(
            "SplunkDestinationConfiguration.hec_endpoint required"
        )
    if data.get("HECEndpointType") is not None:
        import capo_firehose.types.hec_endpoint_type

        out["hec_endpoint_type"] = (
            capo_firehose.types.hec_endpoint_type.deserialize_aws_json_1_1(
                data["HECEndpointType"]
            )
        )
    else:
        raise DeserializationError(
            "SplunkDestinationConfiguration.hec_endpoint_type required"
        )
    if data.get("HECToken") is not None:
        out["hec_token"] = data["HECToken"]
    if data.get("HECAcknowledgmentTimeoutInSeconds") is not None:
        out["hec_acknowledgment_timeout_in_seconds"] = data[
            "HECAcknowledgmentTimeoutInSeconds"
        ]
    if data.get("RetryOptions") is not None:
        import capo_firehose.types.splunk_retry_options

        out["retry_options"] = (
            capo_firehose.types.splunk_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if data.get("S3BackupMode") is not None:
        import capo_firehose.types.splunk_s3_backup_mode

        out["s3_backup_mode"] = (
            capo_firehose.types.splunk_s3_backup_mode.deserialize_aws_json_1_1(
                data["S3BackupMode"]
            )
        )
    if data.get("S3Configuration") is not None:
        import capo_firehose.types.s3_destination_configuration

        out["s3_configuration"] = (
            capo_firehose.types.s3_destination_configuration.deserialize_aws_json_1_1(
                data["S3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "SplunkDestinationConfiguration.s3_configuration required"
        )
    if data.get("ProcessingConfiguration") is not None:
        import capo_firehose.types.processing_configuration

        out["processing_configuration"] = (
            capo_firehose.types.processing_configuration.deserialize_aws_json_1_1(
                data["ProcessingConfiguration"]
            )
        )
    if data.get("CloudWatchLoggingOptions") is not None:
        import capo_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            capo_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if data.get("BufferingHints") is not None:
        import capo_firehose.types.splunk_buffering_hints

        out["buffering_hints"] = (
            capo_firehose.types.splunk_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if data.get("SecretsManagerConfiguration") is not None:
        import capo_firehose.types.secrets_manager_configuration

        out["secrets_manager_configuration"] = (
            capo_firehose.types.secrets_manager_configuration.deserialize_aws_json_1_1(
                data["SecretsManagerConfiguration"]
            )
        )
    return out
