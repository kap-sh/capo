"""Generated from Smithy shape ``com.amazonaws.firehose#ElasticsearchDestinationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.document_id_options
    import capo_firehose.types.elasticsearch_buffering_hints
    import capo_firehose.types.elasticsearch_cluster_endpoint
    import capo_firehose.types.elasticsearch_domain_arn
    import capo_firehose.types.elasticsearch_index_name
    import capo_firehose.types.elasticsearch_index_rotation_period
    import capo_firehose.types.elasticsearch_retry_options
    import capo_firehose.types.elasticsearch_type_name
    import capo_firehose.types.processing_configuration
    import capo_firehose.types.role_arn
    import capo_firehose.types.s3_destination_update


class ElasticsearchDestinationUpdate(TypedDict, closed=True):
    role_arn: NotRequired["capo_firehose.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents. For more information, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3">Grant Firehose Access to an Amazon S3 Destination</a> and <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    domain_arn: NotRequired[
        "capo_firehose.types.elasticsearch_domain_arn.ElasticsearchDomainARN"
    ]
    """<p>The ARN of the Amazon OpenSearch Service domain. The IAM role must have permissions for <code>DescribeDomain</code>, <code>DescribeDomains</code>, and <code>DescribeDomainConfig</code> after assuming the IAM role specified in <code>RoleARN</code>. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p> <p>Specify either <code>ClusterEndpoint</code> or <code>DomainARN</code>.</p>"""
    cluster_endpoint: NotRequired[
        "capo_firehose.types.elasticsearch_cluster_endpoint.ElasticsearchClusterEndpoint"
    ]
    """<p>The endpoint to use when communicating with the cluster. Specify either this <code>ClusterEndpoint</code> or the <code>DomainARN</code> field.</p>"""
    index_name: NotRequired[
        "capo_firehose.types.elasticsearch_index_name.ElasticsearchIndexName"
    ]
    """<p>The Elasticsearch index name.</p>"""
    type_name: NotRequired[
        "capo_firehose.types.elasticsearch_type_name.ElasticsearchTypeName"
    ]
    """<p>The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Firehose returns an error during runtime.</p> <p>If you upgrade Elasticsearch from 6.x to 7.x and don’t update your Firehose stream, Firehose still delivers data to Elasticsearch with the old index name and type name. If you want to update your Firehose stream with a new index name, provide an empty string for <code>TypeName</code>. </p>"""
    index_rotation_period: NotRequired[
        "capo_firehose.types.elasticsearch_index_rotation_period.ElasticsearchIndexRotationPeriod"
    ]
    """<p>The Elasticsearch index rotation period. Index rotation appends a timestamp to <code>IndexName</code> to facilitate the expiration of old data. For more information, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation">Index Rotation for the Amazon OpenSearch Service Destination</a>. Default value is <code>OneDay</code>.</p>"""
    buffering_hints: NotRequired[
        "capo_firehose.types.elasticsearch_buffering_hints.ElasticsearchBufferingHints"
    ]
    """<p>The buffering options. If no value is specified, <code>ElasticsearchBufferingHints</code> object default values are used. </p>"""
    retry_options: NotRequired[
        "capo_firehose.types.elasticsearch_retry_options.ElasticsearchRetryOptions"
    ]
    """<p>The retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service. The default value is 300 (5 minutes).</p>"""
    s3_update: NotRequired[
        "capo_firehose.types.s3_destination_update.S3DestinationUpdate"
    ]
    """<p>The Amazon S3 destination.</p>"""
    processing_configuration: NotRequired[
        "capo_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    """<p>The data processing configuration.</p>"""
    cloud_watch_logging_options: NotRequired[
        "capo_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>The CloudWatch logging options for your Firehose stream.</p>"""
    document_id_options: NotRequired[
        "capo_firehose.types.document_id_options.DocumentIdOptions"
    ]
    """<p>Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElasticsearchDestinationUpdate) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "domain_arn" in value:
        out["DomainARN"] = value["domain_arn"]
    if "cluster_endpoint" in value:
        out["ClusterEndpoint"] = value["cluster_endpoint"]
    if "index_name" in value:
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
    if "s3_update" in value:
        import capo_firehose.types.s3_destination_update

        out["S3Update"] = (
            capo_firehose.types.s3_destination_update.serialize_aws_json_1_1(
                value["s3_update"]
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
    if "document_id_options" in value:
        import capo_firehose.types.document_id_options

        out["DocumentIdOptions"] = (
            capo_firehose.types.document_id_options.serialize_aws_json_1_1(
                value["document_id_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ElasticsearchDestinationUpdate:
    out: ElasticsearchDestinationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    if data.get("DomainARN") is not None:
        out["domain_arn"] = data["DomainARN"]
    if data.get("ClusterEndpoint") is not None:
        out["cluster_endpoint"] = data["ClusterEndpoint"]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
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
    if data.get("S3Update") is not None:
        import capo_firehose.types.s3_destination_update

        out["s3_update"] = (
            capo_firehose.types.s3_destination_update.deserialize_aws_json_1_1(
                data["S3Update"]
            )
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
    if data.get("DocumentIdOptions") is not None:
        import capo_firehose.types.document_id_options

        out["document_id_options"] = (
            capo_firehose.types.document_id_options.deserialize_aws_json_1_1(
                data["DocumentIdOptions"]
            )
        )
    return out
