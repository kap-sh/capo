"""Generated from Smithy shape ``com.amazonaws.firehose#IcebergDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.buffering_hints
    import capo_firehose.types.catalog_configuration
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.destination_table_configuration_list
    import capo_firehose.types.iceberg_s3_backup_mode
    import capo_firehose.types.processing_configuration
    import capo_firehose.types.retry_options
    import capo_firehose.types.role_arn
    import capo_firehose.types.s3_destination_configuration
    import capo_firehose.types.schema_evolution_configuration
    import capo_firehose.types.table_creation_configuration


class IcebergDestinationConfiguration(TypedDict, closed=True):
    destination_table_configuration_list: NotRequired[
        "capo_firehose.types.destination_table_configuration_list.DestinationTableConfigurationList"
    ]
    """<p> Provides a list of <code>DestinationTableConfigurations</code> which Firehose uses to deliver data to Apache Iceberg Tables. Firehose will write data with insert if table specific configuration is not provided here.</p>"""
    schema_evolution_configuration: NotRequired[
        "capo_firehose.types.schema_evolution_configuration.SchemaEvolutionConfiguration"
    ]
    """<p>The configuration to enable automatic schema evolution.</p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    table_creation_configuration: NotRequired[
        "capo_firehose.types.table_creation_configuration.TableCreationConfiguration"
    ]
    """<p>The configuration to enable automatic table creation.</p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    buffering_hints: NotRequired["capo_firehose.types.buffering_hints.BufferingHints"]
    cloud_watch_logging_options: NotRequired[
        "capo_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    processing_configuration: NotRequired[
        "capo_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    s3_backup_mode: NotRequired[
        "capo_firehose.types.iceberg_s3_backup_mode.IcebergS3BackupMode"
    ]
    """<p> Describes how Firehose will backup records. Currently,S3 backup only supports <code>FailedDataOnly</code>. </p>"""
    retry_options: NotRequired["capo_firehose.types.retry_options.RetryOptions"]
    role_arn: "capo_firehose.types.role_arn.RoleARN"
    """<p> The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling Apache Iceberg Tables. </p>"""
    append_only: NotRequired["capo_firehose.types.boolean_object.BooleanObject"]
    """<p> Describes whether all incoming data for this delivery stream will be append only (inserts only and not for updates and deletes) for Iceberg delivery. This feature is only applicable for Apache Iceberg Tables.</p> <p>The default value is false. If you set this value to true, Firehose automatically increases the throughput limit of a stream based on the throttling levels of the stream. If you set this parameter to true for a stream with updates and deletes, you will see out of order delivery. </p>"""
    catalog_configuration: (
        "capo_firehose.types.catalog_configuration.CatalogConfiguration"
    )
    """<p> Configuration describing where the destination Apache Iceberg Tables are persisted. </p>"""
    s3_configuration: (
        "capo_firehose.types.s3_destination_configuration.S3DestinationConfiguration"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergDestinationConfiguration) -> dict:
    out: dict = {}
    if "destination_table_configuration_list" in value:
        import capo_firehose.types.destination_table_configuration_list

        out["DestinationTableConfigurationList"] = (
            capo_firehose.types.destination_table_configuration_list.serialize_aws_json_1_1(
                value["destination_table_configuration_list"]
            )
        )
    if "schema_evolution_configuration" in value:
        import capo_firehose.types.schema_evolution_configuration

        out["SchemaEvolutionConfiguration"] = (
            capo_firehose.types.schema_evolution_configuration.serialize_aws_json_1_1(
                value["schema_evolution_configuration"]
            )
        )
    if "table_creation_configuration" in value:
        import capo_firehose.types.table_creation_configuration

        out["TableCreationConfiguration"] = (
            capo_firehose.types.table_creation_configuration.serialize_aws_json_1_1(
                value["table_creation_configuration"]
            )
        )
    if "buffering_hints" in value:
        import capo_firehose.types.buffering_hints

        out["BufferingHints"] = (
            capo_firehose.types.buffering_hints.serialize_aws_json_1_1(
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
    if "processing_configuration" in value:
        import capo_firehose.types.processing_configuration

        out["ProcessingConfiguration"] = (
            capo_firehose.types.processing_configuration.serialize_aws_json_1_1(
                value["processing_configuration"]
            )
        )
    if "s3_backup_mode" in value:
        import capo_firehose.types.iceberg_s3_backup_mode

        out["S3BackupMode"] = (
            capo_firehose.types.iceberg_s3_backup_mode.serialize_aws_json_1_1(
                value["s3_backup_mode"]
            )
        )
    if "retry_options" in value:
        import capo_firehose.types.retry_options

        out["RetryOptions"] = capo_firehose.types.retry_options.serialize_aws_json_1_1(
            value["retry_options"]
        )
    out["RoleARN"] = value["role_arn"]
    if "append_only" in value:
        out["AppendOnly"] = value["append_only"]
    import capo_firehose.types.catalog_configuration

    out["CatalogConfiguration"] = (
        capo_firehose.types.catalog_configuration.serialize_aws_json_1_1(
            value["catalog_configuration"]
        )
    )
    import capo_firehose.types.s3_destination_configuration

    out["S3Configuration"] = (
        capo_firehose.types.s3_destination_configuration.serialize_aws_json_1_1(
            value["s3_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergDestinationConfiguration:
    out: IcebergDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DestinationTableConfigurationList") is not None:
        import capo_firehose.types.destination_table_configuration_list

        out["destination_table_configuration_list"] = (
            capo_firehose.types.destination_table_configuration_list.deserialize_aws_json_1_1(
                data["DestinationTableConfigurationList"]
            )
        )
    if data.get("SchemaEvolutionConfiguration") is not None:
        import capo_firehose.types.schema_evolution_configuration

        out["schema_evolution_configuration"] = (
            capo_firehose.types.schema_evolution_configuration.deserialize_aws_json_1_1(
                data["SchemaEvolutionConfiguration"]
            )
        )
    if data.get("TableCreationConfiguration") is not None:
        import capo_firehose.types.table_creation_configuration

        out["table_creation_configuration"] = (
            capo_firehose.types.table_creation_configuration.deserialize_aws_json_1_1(
                data["TableCreationConfiguration"]
            )
        )
    if data.get("BufferingHints") is not None:
        import capo_firehose.types.buffering_hints

        out["buffering_hints"] = (
            capo_firehose.types.buffering_hints.deserialize_aws_json_1_1(
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
    if data.get("ProcessingConfiguration") is not None:
        import capo_firehose.types.processing_configuration

        out["processing_configuration"] = (
            capo_firehose.types.processing_configuration.deserialize_aws_json_1_1(
                data["ProcessingConfiguration"]
            )
        )
    if data.get("S3BackupMode") is not None:
        import capo_firehose.types.iceberg_s3_backup_mode

        out["s3_backup_mode"] = (
            capo_firehose.types.iceberg_s3_backup_mode.deserialize_aws_json_1_1(
                data["S3BackupMode"]
            )
        )
    if data.get("RetryOptions") is not None:
        import capo_firehose.types.retry_options

        out["retry_options"] = (
            capo_firehose.types.retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        out["role_arn"] = ""
    if data.get("AppendOnly") is not None:
        out["append_only"] = data["AppendOnly"]
    if data.get("CatalogConfiguration") is not None:
        import capo_firehose.types.catalog_configuration

        out["catalog_configuration"] = (
            capo_firehose.types.catalog_configuration.deserialize_aws_json_1_1(
                data["CatalogConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "IcebergDestinationConfiguration.catalog_configuration required"
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
            "IcebergDestinationConfiguration.s3_configuration required"
        )
    return out
