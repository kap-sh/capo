"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonOpenSearchServerlessDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.amazon_open_search_serverless_buffering_hints
    import capo_firehose.types.amazon_open_search_serverless_collection_endpoint
    import capo_firehose.types.amazon_open_search_serverless_index_name
    import capo_firehose.types.amazon_open_search_serverless_retry_options
    import capo_firehose.types.amazon_open_search_serverless_s3_backup_mode
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.processing_configuration
    import capo_firehose.types.role_arn
    import capo_firehose.types.s3_destination_configuration
    import capo_firehose.types.vpc_configuration


class AmazonOpenSearchServerlessDestinationConfiguration(TypedDict, closed=True):
    role_arn: "capo_firehose.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Serverless offering for Amazon OpenSearch Service Configuration API and for indexing documents.</p>"""
    collection_endpoint: NotRequired[
        "capo_firehose.types.amazon_open_search_serverless_collection_endpoint.AmazonOpenSearchServerlessCollectionEndpoint"
    ]
    """<p>The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.</p>"""
    index_name: "capo_firehose.types.amazon_open_search_serverless_index_name.AmazonOpenSearchServerlessIndexName"
    """<p>The Serverless offering for Amazon OpenSearch Service index name.</p>"""
    buffering_hints: NotRequired[
        "capo_firehose.types.amazon_open_search_serverless_buffering_hints.AmazonOpenSearchServerlessBufferingHints"
    ]
    """<p>The buffering options. If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.</p>"""
    retry_options: NotRequired[
        "capo_firehose.types.amazon_open_search_serverless_retry_options.AmazonOpenSearchServerlessRetryOptions"
    ]
    """<p>The retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service. The default value is 300 (5 minutes).</p>"""
    s3_backup_mode: NotRequired[
        "capo_firehose.types.amazon_open_search_serverless_s3_backup_mode.AmazonOpenSearchServerlessS3BackupMode"
    ]
    """<p>Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix.</p>"""
    s3_configuration: (
        "capo_firehose.types.s3_destination_configuration.S3DestinationConfiguration"
    )
    processing_configuration: NotRequired[
        "capo_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    cloud_watch_logging_options: NotRequired[
        "capo_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    vpc_configuration: NotRequired[
        "capo_firehose.types.vpc_configuration.VpcConfiguration"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AmazonOpenSearchServerlessDestinationConfiguration,
) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    if "collection_endpoint" in value:
        out["CollectionEndpoint"] = value["collection_endpoint"]
    out["IndexName"] = value["index_name"]
    if "buffering_hints" in value:
        import capo_firehose.types.amazon_open_search_serverless_buffering_hints

        out["BufferingHints"] = (
            capo_firehose.types.amazon_open_search_serverless_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "retry_options" in value:
        import capo_firehose.types.amazon_open_search_serverless_retry_options

        out["RetryOptions"] = (
            capo_firehose.types.amazon_open_search_serverless_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import capo_firehose.types.amazon_open_search_serverless_s3_backup_mode

        out["S3BackupMode"] = (
            capo_firehose.types.amazon_open_search_serverless_s3_backup_mode.serialize_aws_json_1_1(
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
    if "vpc_configuration" in value:
        import capo_firehose.types.vpc_configuration

        out["VpcConfiguration"] = (
            capo_firehose.types.vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AmazonOpenSearchServerlessDestinationConfiguration:
    out: AmazonOpenSearchServerlessDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        out["role_arn"] = ""
    if data.get("CollectionEndpoint") is not None:
        out["collection_endpoint"] = data["CollectionEndpoint"]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    if data.get("BufferingHints") is not None:
        import capo_firehose.types.amazon_open_search_serverless_buffering_hints

        out["buffering_hints"] = (
            capo_firehose.types.amazon_open_search_serverless_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if data.get("RetryOptions") is not None:
        import capo_firehose.types.amazon_open_search_serverless_retry_options

        out["retry_options"] = (
            capo_firehose.types.amazon_open_search_serverless_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if data.get("S3BackupMode") is not None:
        import capo_firehose.types.amazon_open_search_serverless_s3_backup_mode

        out["s3_backup_mode"] = (
            capo_firehose.types.amazon_open_search_serverless_s3_backup_mode.deserialize_aws_json_1_1(
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
            "AmazonOpenSearchServerlessDestinationConfiguration.s3_configuration required"
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
    if data.get("VpcConfiguration") is not None:
        import capo_firehose.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_firehose.types.vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    return out
