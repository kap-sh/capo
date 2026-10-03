"""Generated from Smithy shape ``com.amazonaws.firehose#ElasticsearchDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.document_id_options
    import capo_firehose.types.elasticsearch_buffering_hints
    import capo_firehose.types.elasticsearch_cluster_endpoint
    import capo_firehose.types.elasticsearch_domain_arn
    import capo_firehose.types.elasticsearch_index_name
    import capo_firehose.types.elasticsearch_index_rotation_period
    import capo_firehose.types.elasticsearch_retry_options
    import capo_firehose.types.elasticsearch_s3_backup_mode
    import capo_firehose.types.elasticsearch_type_name
    import capo_firehose.types.processing_configuration
    import capo_firehose.types.role_arn
    import capo_firehose.types.s3_destination_configuration
    import capo_firehose.types.vpc_configuration


class ElasticsearchDestinationConfiguration(TypedDict, closed=True):
    role_arn: "capo_firehose.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents. For more information, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3">Grant Firehose Access to an Amazon S3 Destination</a> and <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    domain_arn: NotRequired[
        "capo_firehose.types.elasticsearch_domain_arn.ElasticsearchDomainARN"
    ]
    """<p>The ARN of the Amazon OpenSearch Service domain. The IAM role must have permissions for <code>DescribeDomain</code>, <code>DescribeDomains</code>, and <code>DescribeDomainConfig</code> after assuming the role specified in <b>RoleARN</b>. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p> <p>Specify either <code>ClusterEndpoint</code> or <code>DomainARN</code>.</p>"""
    cluster_endpoint: NotRequired[
        "capo_firehose.types.elasticsearch_cluster_endpoint.ElasticsearchClusterEndpoint"
    ]
    """<p>The endpoint to use when communicating with the cluster. Specify either this <code>ClusterEndpoint</code> or the <code>DomainARN</code> field.</p>"""
    index_name: "capo_firehose.types.elasticsearch_index_name.ElasticsearchIndexName"
    """<p>The Elasticsearch index name.</p>"""
    type_name: NotRequired[
        "capo_firehose.types.elasticsearch_type_name.ElasticsearchTypeName"
    ]
    """<p>The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Firehose returns an error during run time.</p> <p>For Elasticsearch 7.x, don't specify a <code>TypeName</code>.</p>"""
    index_rotation_period: NotRequired[
        "capo_firehose.types.elasticsearch_index_rotation_period.ElasticsearchIndexRotationPeriod"
    ]
    """<p>The Elasticsearch index rotation period. Index rotation appends a timestamp to the <code>IndexName</code> to facilitate the expiration of old data. For more information, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation">Index Rotation for the Amazon OpenSearch Service Destination</a>. The default value is <code>OneDay</code>.</p>"""
    buffering_hints: NotRequired[
        "capo_firehose.types.elasticsearch_buffering_hints.ElasticsearchBufferingHints"
    ]
    """<p>The buffering options. If no value is specified, the default values for <code>ElasticsearchBufferingHints</code> are used.</p>"""
    retry_options: NotRequired[
        "capo_firehose.types.elasticsearch_retry_options.ElasticsearchRetryOptions"
    ]
    """<p>The retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service. The default value is 300 (5 minutes).</p>"""
    s3_backup_mode: NotRequired[
        "capo_firehose.types.elasticsearch_s3_backup_mode.ElasticsearchS3BackupMode"
    ]
    """<p>Defines how documents should be delivered to Amazon S3. When it is set to <code>FailedDocumentsOnly</code>, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with <code>AmazonOpenSearchService-failed/</code> appended to the key prefix. When set to <code>AllDocuments</code>, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with <code>AmazonOpenSearchService-failed/</code> appended to the prefix. For more information, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-s3-backup">Amazon S3 Backup for the Amazon OpenSearch Service Destination</a>. Default value is <code>FailedDocumentsOnly</code>.</p> <p>You can't change this backup mode after you create the Firehose stream. </p>"""
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
    vpc_configuration: NotRequired[
        "capo_firehose.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The details of the VPC of the Amazon destination.</p>"""
    document_id_options: NotRequired[
        "capo_firehose.types.document_id_options.DocumentIdOptions"
    ]
    """<p>Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElasticsearchDestinationConfiguration) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    if "domain_arn" in value:
        out["DomainARN"] = value["domain_arn"]
    if "cluster_endpoint" in value:
        out["ClusterEndpoint"] = value["cluster_endpoint"]
    out["IndexName"] = value["index_name"]
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "index_rotation_period" in value:
        import capo_firehose.types.elasticsearch_index_rotation_period

        out["IndexRotationPeriod"] = (
            capo_firehose.types.elasticsearch_index_rotation_period.serialize_aws_json_1_1(
                value["index_rotation_period"]
            )
        )
    if "buffering_hints" in value:
        import capo_firehose.types.elasticsearch_buffering_hints

        out["BufferingHints"] = (
            capo_firehose.types.elasticsearch_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "retry_options" in value:
        import capo_firehose.types.elasticsearch_retry_options

        out["RetryOptions"] = (
            capo_firehose.types.elasticsearch_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import capo_firehose.types.elasticsearch_s3_backup_mode

        out["S3BackupMode"] = (
            capo_firehose.types.elasticsearch_s3_backup_mode.serialize_aws_json_1_1(
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
    if "document_id_options" in value:
        import capo_firehose.types.document_id_options

        out["DocumentIdOptions"] = (
            capo_firehose.types.document_id_options.serialize_aws_json_1_1(
                value["document_id_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ElasticsearchDestinationConfiguration:
    out: ElasticsearchDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError(
            "ElasticsearchDestinationConfiguration.role_arn required"
        )
    if data.get("DomainARN") is not None:
        out["domain_arn"] = data["DomainARN"]
    if data.get("ClusterEndpoint") is not None:
        out["cluster_endpoint"] = data["ClusterEndpoint"]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError(
            "ElasticsearchDestinationConfiguration.index_name required"
        )
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("IndexRotationPeriod") is not None:
        import capo_firehose.types.elasticsearch_index_rotation_period

        out["index_rotation_period"] = (
            capo_firehose.types.elasticsearch_index_rotation_period.deserialize_aws_json_1_1(
                data["IndexRotationPeriod"]
            )
        )
    if data.get("BufferingHints") is not None:
        import capo_firehose.types.elasticsearch_buffering_hints

        out["buffering_hints"] = (
            capo_firehose.types.elasticsearch_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if data.get("RetryOptions") is not None:
        import capo_firehose.types.elasticsearch_retry_options

        out["retry_options"] = (
            capo_firehose.types.elasticsearch_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if data.get("S3BackupMode") is not None:
        import capo_firehose.types.elasticsearch_s3_backup_mode

        out["s3_backup_mode"] = (
            capo_firehose.types.elasticsearch_s3_backup_mode.deserialize_aws_json_1_1(
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
            "ElasticsearchDestinationConfiguration.s3_configuration required"
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
    if data.get("DocumentIdOptions") is not None:
        import capo_firehose.types.document_id_options

        out["document_id_options"] = (
            capo_firehose.types.document_id_options.deserialize_aws_json_1_1(
                data["DocumentIdOptions"]
            )
        )
    return out
