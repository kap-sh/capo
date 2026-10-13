"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointDestinationDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.http_endpoint_buffering_hints
    import capo_firehose.types.http_endpoint_description
    import capo_firehose.types.http_endpoint_request_configuration
    import capo_firehose.types.http_endpoint_retry_options
    import capo_firehose.types.http_endpoint_s3_backup_mode
    import capo_firehose.types.processing_configuration
    import capo_firehose.types.role_arn
    import capo_firehose.types.s3_destination_description
    import capo_firehose.types.secrets_manager_configuration


class HttpEndpointDestinationDescription(TypedDict, closed=True):
    endpoint_configuration: NotRequired[
        "capo_firehose.types.http_endpoint_description.HttpEndpointDescription"
    ]
    """<p>The configuration of the specified HTTP endpoint destination.</p>"""
    buffering_hints: NotRequired[
        "capo_firehose.types.http_endpoint_buffering_hints.HttpEndpointBufferingHints"
    ]
    """<p>Describes buffering options that can be applied to the data before it is delivered to the HTTPS endpoint destination. Firehose teats these options as hints, and it might choose to use more optimal values. The <code>SizeInMBs</code> and <code>IntervalInSeconds</code> parameters are optional. However, if specify a value for one of them, you must also provide a value for the other. </p>"""
    cloud_watch_logging_options: NotRequired[
        "capo_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    request_configuration: NotRequired[
        "capo_firehose.types.http_endpoint_request_configuration.HttpEndpointRequestConfiguration"
    ]
    """<p>The configuration of request sent to the HTTP endpoint specified as the destination.</p>"""
    processing_configuration: NotRequired[
        "capo_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    role_arn: NotRequired["capo_firehose.types.role_arn.RoleARN"]
    """<p>Firehose uses this IAM role for all the permissions that the delivery stream needs.</p>"""
    retry_options: NotRequired[
        "capo_firehose.types.http_endpoint_retry_options.HttpEndpointRetryOptions"
    ]
    """<p>Describes the retry behavior in case Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.</p>"""
    s3_backup_mode: NotRequired[
        "capo_firehose.types.http_endpoint_s3_backup_mode.HttpEndpointS3BackupMode"
    ]
    """<p>Describes the S3 bucket backup options for the data that Kinesis Firehose delivers to the HTTP endpoint destination. You can back up all documents (<code>AllData</code>) or only the documents that Firehose could not deliver to the specified HTTP endpoint destination (<code>FailedDataOnly</code>).</p>"""
    s3_destination_description: NotRequired[
        "capo_firehose.types.s3_destination_description.S3DestinationDescription"
    ]
    secrets_manager_configuration: NotRequired[
        "capo_firehose.types.secrets_manager_configuration.SecretsManagerConfiguration"
    ]
    """<p> The configuration that defines how you access secrets for HTTP Endpoint destination. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointDestinationDescription) -> dict:
    out: dict = {}
    if "endpoint_configuration" in value:
        import capo_firehose.types.http_endpoint_description

        out["EndpointConfiguration"] = (
            capo_firehose.types.http_endpoint_description.serialize_aws_json_1_1(
                value["endpoint_configuration"]
            )
        )
    if "buffering_hints" in value:
        import capo_firehose.types.http_endpoint_buffering_hints

        out["BufferingHints"] = (
            capo_firehose.types.http_endpoint_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "cloud_watch_logging_options" in value:
        import capo_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            capo_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "request_configuration" in value:
        import capo_firehose.types.http_endpoint_request_configuration

        out["RequestConfiguration"] = (
            capo_firehose.types.http_endpoint_request_configuration.serialize_aws_json_1_1(
                value["request_configuration"]
            )
        )
    if "processing_configuration" in value:
        import capo_firehose.types.processing_configuration

        out["ProcessingConfiguration"] = (
            capo_firehose.types.processing_configuration.serialize_aws_json_1_1(
                value["processing_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "retry_options" in value:
        import capo_firehose.types.http_endpoint_retry_options

        out["RetryOptions"] = (
            capo_firehose.types.http_endpoint_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import capo_firehose.types.http_endpoint_s3_backup_mode

        out["S3BackupMode"] = (
            capo_firehose.types.http_endpoint_s3_backup_mode.serialize_aws_json_1_1(
                value["s3_backup_mode"]
            )
        )
    if "s3_destination_description" in value:
        import capo_firehose.types.s3_destination_description

        out["S3DestinationDescription"] = (
            capo_firehose.types.s3_destination_description.serialize_aws_json_1_1(
                value["s3_destination_description"]
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


def deserialize_aws_json_1_1(data: dict) -> HttpEndpointDestinationDescription:
    out: HttpEndpointDestinationDescription = {}  # type: ignore[typeddict-item]
    if data.get("EndpointConfiguration") is not None:
        import capo_firehose.types.http_endpoint_description

        out["endpoint_configuration"] = (
            capo_firehose.types.http_endpoint_description.deserialize_aws_json_1_1(
                data["EndpointConfiguration"]
            )
        )
    if data.get("BufferingHints") is not None:
        import capo_firehose.types.http_endpoint_buffering_hints

        out["buffering_hints"] = (
            capo_firehose.types.http_endpoint_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if data.get("CloudWatchLoggingOptions") is not None:
        import capo_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            capo_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if data.get("RequestConfiguration") is not None:
        import capo_firehose.types.http_endpoint_request_configuration

        out["request_configuration"] = (
            capo_firehose.types.http_endpoint_request_configuration.deserialize_aws_json_1_1(
                data["RequestConfiguration"]
            )
        )
    if data.get("ProcessingConfiguration") is not None:
        import capo_firehose.types.processing_configuration

        out["processing_configuration"] = (
            capo_firehose.types.processing_configuration.deserialize_aws_json_1_1(
                data["ProcessingConfiguration"]
            )
        )
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    if data.get("RetryOptions") is not None:
        import capo_firehose.types.http_endpoint_retry_options

        out["retry_options"] = (
            capo_firehose.types.http_endpoint_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if data.get("S3BackupMode") is not None:
        import capo_firehose.types.http_endpoint_s3_backup_mode

        out["s3_backup_mode"] = (
            capo_firehose.types.http_endpoint_s3_backup_mode.deserialize_aws_json_1_1(
                data["S3BackupMode"]
            )
        )
    if data.get("S3DestinationDescription") is not None:
        import capo_firehose.types.s3_destination_description

        out["s3_destination_description"] = (
            capo_firehose.types.s3_destination_description.deserialize_aws_json_1_1(
                data["S3DestinationDescription"]
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


def redact_sensitive(value: HttpEndpointDestinationDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoint_configuration" in value:
        import capo_firehose.types.http_endpoint_description

        out["endpoint_configuration"] = (
            capo_firehose.types.http_endpoint_description.redact_sensitive(
                value["endpoint_configuration"]
            )
        )
    if "request_configuration" in value:
        import capo_firehose.types.http_endpoint_request_configuration

        out["request_configuration"] = (
            capo_firehose.types.http_endpoint_request_configuration.redact_sensitive(
                value["request_configuration"]
            )
        )
    return out
