"""Generated from Smithy shape ``com.amazonaws.firehose#S3DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.bucket_arn
    import capo_firehose.types.buffering_hints
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.compression_format
    import capo_firehose.types.encryption_configuration
    import capo_firehose.types.error_output_prefix
    import capo_firehose.types.prefix
    import capo_firehose.types.role_arn


class S3DestinationConfiguration(TypedDict, closed=True):
    role_arn: "capo_firehose.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    bucket_arn: "capo_firehose.types.bucket_arn.BucketARN"
    """<p>The ARN of the S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    prefix: NotRequired["capo_firehose.types.prefix.Prefix"]
    """<p>The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in <a href="https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html">Custom Prefixes for Amazon S3 Objects</a>.</p>"""
    error_output_prefix: NotRequired[
        "capo_firehose.types.error_output_prefix.ErrorOutputPrefix"
    ]
    """<p>A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html">Custom Prefixes for Amazon S3 Objects</a>.</p>"""
    buffering_hints: NotRequired["capo_firehose.types.buffering_hints.BufferingHints"]
    """<p>The buffering option. If no value is specified, <code>BufferingHints</code> object default values are used.</p>"""
    compression_format: NotRequired[
        "capo_firehose.types.compression_format.CompressionFormat"
    ]
    """<p>The compression format. If no value is specified, the default is <code>UNCOMPRESSED</code>.</p> <p>The compression formats <code>SNAPPY</code> or <code>ZIP</code> cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift <code>COPY</code> operation that reads from the S3 bucket.</p>"""
    encryption_configuration: NotRequired[
        "capo_firehose.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration. If no value is specified, the default is no encryption.</p>"""
    cloud_watch_logging_options: NotRequired[
        "capo_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>The CloudWatch logging options for your Firehose stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DestinationConfiguration) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    out["BucketARN"] = value["bucket_arn"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "error_output_prefix" in value:
        out["ErrorOutputPrefix"] = value["error_output_prefix"]
    if "buffering_hints" in value:
        import capo_firehose.types.buffering_hints

        out["BufferingHints"] = (
            capo_firehose.types.buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "compression_format" in value:
        import capo_firehose.types.compression_format

        out["CompressionFormat"] = (
            capo_firehose.types.compression_format.serialize_aws_json_1_1(
                value["compression_format"]
            )
        )
    if "encryption_configuration" in value:
        import capo_firehose.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_firehose.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "cloud_watch_logging_options" in value:
        import capo_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            capo_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DestinationConfiguration:
    out: S3DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("S3DestinationConfiguration.role_arn required")
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        raise DeserializationError("S3DestinationConfiguration.bucket_arn required")
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    if data.get("ErrorOutputPrefix") is not None:
        out["error_output_prefix"] = data["ErrorOutputPrefix"]
    if data.get("BufferingHints") is not None:
        import capo_firehose.types.buffering_hints

        out["buffering_hints"] = (
            capo_firehose.types.buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if data.get("CompressionFormat") is not None:
        import capo_firehose.types.compression_format

        out["compression_format"] = (
            capo_firehose.types.compression_format.deserialize_aws_json_1_1(
                data["CompressionFormat"]
            )
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_firehose.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_firehose.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("CloudWatchLoggingOptions") is not None:
        import capo_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            capo_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    return out
