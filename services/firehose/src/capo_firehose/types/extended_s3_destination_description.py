"""Generated from Smithy shape ``com.amazonaws.firehose#ExtendedS3DestinationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.bucket_arn
    import capo_firehose.types.buffering_hints
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.compression_format
    import capo_firehose.types.custom_time_zone
    import capo_firehose.types.data_format_conversion_configuration
    import capo_firehose.types.dynamic_partitioning_configuration
    import capo_firehose.types.encryption_configuration
    import capo_firehose.types.error_output_prefix
    import capo_firehose.types.file_extension
    import capo_firehose.types.prefix
    import capo_firehose.types.processing_configuration
    import capo_firehose.types.role_arn
    import capo_firehose.types.s3_backup_mode
    import capo_firehose.types.s3_destination_description


class ExtendedS3DestinationDescription(TypedDict, closed=True):
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
    buffering_hints: "capo_firehose.types.buffering_hints.BufferingHints"
    """<p>The buffering option.</p>"""
    compression_format: "capo_firehose.types.compression_format.CompressionFormat"
    """<p>The compression format. If no value is specified, the default is <code>UNCOMPRESSED</code>.</p>"""
    encryption_configuration: (
        "capo_firehose.types.encryption_configuration.EncryptionConfiguration"
    )
    """<p>The encryption configuration. If no value is specified, the default is no encryption.</p>"""
    cloud_watch_logging_options: NotRequired[
        "capo_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>The Amazon CloudWatch logging options for your Firehose stream.</p>"""
    processing_configuration: NotRequired[
        "capo_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    """<p>The data processing configuration.</p>"""
    s3_backup_mode: NotRequired["capo_firehose.types.s3_backup_mode.S3BackupMode"]
    """<p>The Amazon S3 backup mode.</p>"""
    s3_backup_description: NotRequired[
        "capo_firehose.types.s3_destination_description.S3DestinationDescription"
    ]
    """<p>The configuration for backup in Amazon S3.</p>"""
    data_format_conversion_configuration: NotRequired[
        "capo_firehose.types.data_format_conversion_configuration.DataFormatConversionConfiguration"
    ]
    """<p>The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.</p>"""
    dynamic_partitioning_configuration: NotRequired[
        "capo_firehose.types.dynamic_partitioning_configuration.DynamicPartitioningConfiguration"
    ]
    """<p>The configuration of the dynamic partitioning mechanism that creates smaller data sets from the streaming data by partitioning it based on partition keys. Currently, dynamic partitioning is only supported for Amazon S3 destinations. </p>"""
    file_extension: NotRequired["capo_firehose.types.file_extension.FileExtension"]
    """<p>Specify a file extension. It will override the default file extension</p>"""
    custom_time_zone: NotRequired["capo_firehose.types.custom_time_zone.CustomTimeZone"]
    """<p>The time zone you prefer. UTC is the default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendedS3DestinationDescription) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    out["BucketARN"] = value["bucket_arn"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "error_output_prefix" in value:
        out["ErrorOutputPrefix"] = value["error_output_prefix"]
    import capo_firehose.types.buffering_hints

    out["BufferingHints"] = capo_firehose.types.buffering_hints.serialize_aws_json_1_1(
        value["buffering_hints"]
    )
    import capo_firehose.types.compression_format

    out["CompressionFormat"] = (
        capo_firehose.types.compression_format.serialize_aws_json_1_1(
            value["compression_format"]
        )
    )
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
    if "processing_configuration" in value:
        import capo_firehose.types.processing_configuration

        out["ProcessingConfiguration"] = (
            capo_firehose.types.processing_configuration.serialize_aws_json_1_1(
                value["processing_configuration"]
            )
        )
    if "s3_backup_mode" in value:
        import capo_firehose.types.s3_backup_mode

        out["S3BackupMode"] = capo_firehose.types.s3_backup_mode.serialize_aws_json_1_1(
            value["s3_backup_mode"]
        )
    if "s3_backup_description" in value:
        import capo_firehose.types.s3_destination_description

        out["S3BackupDescription"] = (
            capo_firehose.types.s3_destination_description.serialize_aws_json_1_1(
                value["s3_backup_description"]
            )
        )
    if "data_format_conversion_configuration" in value:
        import capo_firehose.types.data_format_conversion_configuration

        out["DataFormatConversionConfiguration"] = (
            capo_firehose.types.data_format_conversion_configuration.serialize_aws_json_1_1(
                value["data_format_conversion_configuration"]
            )
        )
    if "dynamic_partitioning_configuration" in value:
        import capo_firehose.types.dynamic_partitioning_configuration

        out["DynamicPartitioningConfiguration"] = (
            capo_firehose.types.dynamic_partitioning_configuration.serialize_aws_json_1_1(
                value["dynamic_partitioning_configuration"]
            )
        )
    if "file_extension" in value:
        out["FileExtension"] = value["file_extension"]
    if "custom_time_zone" in value:
        out["CustomTimeZone"] = value["custom_time_zone"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtendedS3DestinationDescription:
    out: ExtendedS3DestinationDescription = {}  # type: ignore[typeddict-item]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("ExtendedS3DestinationDescription.role_arn required")
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        raise DeserializationError(
            "ExtendedS3DestinationDescription.bucket_arn required"
        )
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
    else:
        raise DeserializationError(
            "ExtendedS3DestinationDescription.buffering_hints required"
        )
    if data.get("CompressionFormat") is not None:
        import capo_firehose.types.compression_format

        out["compression_format"] = (
            capo_firehose.types.compression_format.deserialize_aws_json_1_1(
                data["CompressionFormat"]
            )
        )
    else:
        raise DeserializationError(
            "ExtendedS3DestinationDescription.compression_format required"
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_firehose.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_firehose.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ExtendedS3DestinationDescription.encryption_configuration required"
        )
    if data.get("CloudWatchLoggingOptions") is not None:
        import capo_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            capo_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if data.get("ProcessingConfiguration") is not None:
        import capo_firehose.types.processing_configuration

        out["processing_configuration"] = (
            capo_firehose.types.processing_configuration.deserialize_aws_json_1_1(
                data["ProcessingConfiguration"]
            )
        )
    if data.get("S3BackupMode") is not None:
        import capo_firehose.types.s3_backup_mode

        out["s3_backup_mode"] = (
            capo_firehose.types.s3_backup_mode.deserialize_aws_json_1_1(
                data["S3BackupMode"]
            )
        )
    if data.get("S3BackupDescription") is not None:
        import capo_firehose.types.s3_destination_description

        out["s3_backup_description"] = (
            capo_firehose.types.s3_destination_description.deserialize_aws_json_1_1(
                data["S3BackupDescription"]
            )
        )
    if data.get("DataFormatConversionConfiguration") is not None:
        import capo_firehose.types.data_format_conversion_configuration

        out["data_format_conversion_configuration"] = (
            capo_firehose.types.data_format_conversion_configuration.deserialize_aws_json_1_1(
                data["DataFormatConversionConfiguration"]
            )
        )
    if data.get("DynamicPartitioningConfiguration") is not None:
        import capo_firehose.types.dynamic_partitioning_configuration

        out["dynamic_partitioning_configuration"] = (
            capo_firehose.types.dynamic_partitioning_configuration.deserialize_aws_json_1_1(
                data["DynamicPartitioningConfiguration"]
            )
        )
    if data.get("FileExtension") is not None:
        out["file_extension"] = data["FileExtension"]
    if data.get("CustomTimeZone") is not None:
        out["custom_time_zone"] = data["CustomTimeZone"]
    return out
