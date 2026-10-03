"""Generated from Smithy shape ``com.amazonaws.firehose#CreateDeliveryStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.amazon_open_search_serverless_destination_configuration
    import capo_firehose.types.amazonopensearchservice_destination_configuration
    import capo_firehose.types.database_source_configuration
    import capo_firehose.types.delivery_stream_encryption_configuration_input
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.delivery_stream_type
    import capo_firehose.types.direct_put_source_configuration
    import capo_firehose.types.elasticsearch_destination_configuration
    import capo_firehose.types.extended_s3_destination_configuration
    import capo_firehose.types.http_endpoint_destination_configuration
    import capo_firehose.types.iceberg_destination_configuration
    import capo_firehose.types.kinesis_stream_source_configuration
    import capo_firehose.types.msk_source_configuration
    import capo_firehose.types.redshift_destination_configuration
    import capo_firehose.types.s3_destination_configuration
    import capo_firehose.types.snowflake_destination_configuration
    import capo_firehose.types.splunk_destination_configuration
    import capo_firehose.types.tag_delivery_stream_input_tag_list


class CreateDeliveryStreamInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream. This name must be unique per Amazon Web Services account in the same Amazon Web Services Region. If the Firehose streams are in different accounts or different Regions, you can have multiple Firehose streams with the same name.</p>"""
    delivery_stream_type: NotRequired[
        "capo_firehose.types.delivery_stream_type.DeliveryStreamType"
    ]
    """<p>The Firehose stream type. This parameter can be one of the following values:</p> <ul> <li> <p> <code>DirectPut</code>: Provider applications access the Firehose stream directly.</p> </li> <li> <p> <code>KinesisStreamAsSource</code>: The Firehose stream uses a Kinesis data stream as a source.</p> </li> </ul>"""
    direct_put_source_configuration: NotRequired[
        "capo_firehose.types.direct_put_source_configuration.DirectPutSourceConfiguration"
    ]
    """<p>The structure that configures parameters such as <code>ThroughputHintInMBs</code> for a stream configured with Direct PUT as a source. </p>"""
    kinesis_stream_source_configuration: NotRequired[
        "capo_firehose.types.kinesis_stream_source_configuration.KinesisStreamSourceConfiguration"
    ]
    """<p>When a Kinesis data stream is used as the source for the Firehose stream, a <a>KinesisStreamSourceConfiguration</a> containing the Kinesis data stream Amazon Resource Name (ARN) and the role ARN for the source stream.</p>"""
    delivery_stream_encryption_configuration_input: NotRequired[
        "capo_firehose.types.delivery_stream_encryption_configuration_input.DeliveryStreamEncryptionConfigurationInput"
    ]
    """<p>Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).</p>"""
    s3_destination_configuration: NotRequired[
        "capo_firehose.types.s3_destination_configuration.S3DestinationConfiguration"
    ]
    """<p>[Deprecated] The destination in Amazon S3. You can specify only one destination.</p>"""
    extended_s3_destination_configuration: NotRequired[
        "capo_firehose.types.extended_s3_destination_configuration.ExtendedS3DestinationConfiguration"
    ]
    """<p>The destination in Amazon S3. You can specify only one destination.</p>"""
    redshift_destination_configuration: NotRequired[
        "capo_firehose.types.redshift_destination_configuration.RedshiftDestinationConfiguration"
    ]
    """<p>The destination in Amazon Redshift. You can specify only one destination.</p>"""
    elasticsearch_destination_configuration: NotRequired[
        "capo_firehose.types.elasticsearch_destination_configuration.ElasticsearchDestinationConfiguration"
    ]
    """<p>The destination in Amazon OpenSearch Service. You can specify only one destination.</p>"""
    amazonopensearchservice_destination_configuration: NotRequired[
        "capo_firehose.types.amazonopensearchservice_destination_configuration.AmazonopensearchserviceDestinationConfiguration"
    ]
    """<p>The destination in Amazon OpenSearch Service. You can specify only one destination.</p>"""
    splunk_destination_configuration: NotRequired[
        "capo_firehose.types.splunk_destination_configuration.SplunkDestinationConfiguration"
    ]
    """<p>The destination in Splunk. You can specify only one destination.</p>"""
    http_endpoint_destination_configuration: NotRequired[
        "capo_firehose.types.http_endpoint_destination_configuration.HttpEndpointDestinationConfiguration"
    ]
    """<p>Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination. You can specify only one destination.</p>"""
    tags: NotRequired[
        "capo_firehose.types.tag_delivery_stream_input_tag_list.TagDeliveryStreamInputTagList"
    ]
    """<p>A set of tags to assign to the Firehose stream. A tag is a key-value pair that you can define and assign to Amazon Web Services resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the Firehose stream. For more information about tags, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the Amazon Web Services Billing and Cost Management User Guide.</p> <p>You can specify up to 50 tags when creating a Firehose stream.</p> <p>If you specify tags in the <code>CreateDeliveryStream</code> action, Amazon Data Firehose performs an additional authorization on the <code>firehose:TagDeliveryStream</code> action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose streams with IAM resource tags will fail with an <code>AccessDeniedException</code> such as following.</p> <p> <b>AccessDeniedException</b> </p> <p>User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy.</p> <p>For an example IAM policy, see <a href="https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples">Tag example.</a> </p>"""
    amazon_open_search_serverless_destination_configuration: NotRequired[
        "capo_firehose.types.amazon_open_search_serverless_destination_configuration.AmazonOpenSearchServerlessDestinationConfiguration"
    ]
    """<p>The destination in the Serverless offering for Amazon OpenSearch Service. You can specify only one destination.</p>"""
    msk_source_configuration: NotRequired[
        "capo_firehose.types.msk_source_configuration.MSKSourceConfiguration"
    ]
    snowflake_destination_configuration: NotRequired[
        "capo_firehose.types.snowflake_destination_configuration.SnowflakeDestinationConfiguration"
    ]
    """<p>Configure Snowflake destination</p>"""
    iceberg_destination_configuration: NotRequired[
        "capo_firehose.types.iceberg_destination_configuration.IcebergDestinationConfiguration"
    ]
    """<p> Configure Apache Iceberg Tables destination. </p>"""
    database_source_configuration: NotRequired[
        "capo_firehose.types.database_source_configuration.DatabaseSourceConfiguration"
    ]
    """<p> The top level object for configuring streams with database as a source. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeliveryStreamInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    if "delivery_stream_type" in value:
        import capo_firehose.types.delivery_stream_type

        out["DeliveryStreamType"] = (
            capo_firehose.types.delivery_stream_type.serialize_aws_json_1_1(
                value["delivery_stream_type"]
            )
        )
    if "direct_put_source_configuration" in value:
        import capo_firehose.types.direct_put_source_configuration

        out["DirectPutSourceConfiguration"] = (
            capo_firehose.types.direct_put_source_configuration.serialize_aws_json_1_1(
                value["direct_put_source_configuration"]
            )
        )
    if "kinesis_stream_source_configuration" in value:
        import capo_firehose.types.kinesis_stream_source_configuration

        out["KinesisStreamSourceConfiguration"] = (
            capo_firehose.types.kinesis_stream_source_configuration.serialize_aws_json_1_1(
                value["kinesis_stream_source_configuration"]
            )
        )
    if "delivery_stream_encryption_configuration_input" in value:
        import capo_firehose.types.delivery_stream_encryption_configuration_input

        out["DeliveryStreamEncryptionConfigurationInput"] = (
            capo_firehose.types.delivery_stream_encryption_configuration_input.serialize_aws_json_1_1(
                value["delivery_stream_encryption_configuration_input"]
            )
        )
    if "s3_destination_configuration" in value:
        import capo_firehose.types.s3_destination_configuration

        out["S3DestinationConfiguration"] = (
            capo_firehose.types.s3_destination_configuration.serialize_aws_json_1_1(
                value["s3_destination_configuration"]
            )
        )
    if "extended_s3_destination_configuration" in value:
        import capo_firehose.types.extended_s3_destination_configuration

        out["ExtendedS3DestinationConfiguration"] = (
            capo_firehose.types.extended_s3_destination_configuration.serialize_aws_json_1_1(
                value["extended_s3_destination_configuration"]
            )
        )
    if "redshift_destination_configuration" in value:
        import capo_firehose.types.redshift_destination_configuration

        out["RedshiftDestinationConfiguration"] = (
            capo_firehose.types.redshift_destination_configuration.serialize_aws_json_1_1(
                value["redshift_destination_configuration"]
            )
        )
    if "elasticsearch_destination_configuration" in value:
        import capo_firehose.types.elasticsearch_destination_configuration

        out["ElasticsearchDestinationConfiguration"] = (
            capo_firehose.types.elasticsearch_destination_configuration.serialize_aws_json_1_1(
                value["elasticsearch_destination_configuration"]
            )
        )
    if "amazonopensearchservice_destination_configuration" in value:
        import capo_firehose.types.amazonopensearchservice_destination_configuration

        out["AmazonopensearchserviceDestinationConfiguration"] = (
            capo_firehose.types.amazonopensearchservice_destination_configuration.serialize_aws_json_1_1(
                value["amazonopensearchservice_destination_configuration"]
            )
        )
    if "splunk_destination_configuration" in value:
        import capo_firehose.types.splunk_destination_configuration

        out["SplunkDestinationConfiguration"] = (
            capo_firehose.types.splunk_destination_configuration.serialize_aws_json_1_1(
                value["splunk_destination_configuration"]
            )
        )
    if "http_endpoint_destination_configuration" in value:
        import capo_firehose.types.http_endpoint_destination_configuration

        out["HttpEndpointDestinationConfiguration"] = (
            capo_firehose.types.http_endpoint_destination_configuration.serialize_aws_json_1_1(
                value["http_endpoint_destination_configuration"]
            )
        )
    if "tags" in value:
        import capo_firehose.types.tag_delivery_stream_input_tag_list

        out["Tags"] = (
            capo_firehose.types.tag_delivery_stream_input_tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "amazon_open_search_serverless_destination_configuration" in value:
        import capo_firehose.types.amazon_open_search_serverless_destination_configuration

        out["AmazonOpenSearchServerlessDestinationConfiguration"] = (
            capo_firehose.types.amazon_open_search_serverless_destination_configuration.serialize_aws_json_1_1(
                value["amazon_open_search_serverless_destination_configuration"]
            )
        )
    if "msk_source_configuration" in value:
        import capo_firehose.types.msk_source_configuration

        out["MSKSourceConfiguration"] = (
            capo_firehose.types.msk_source_configuration.serialize_aws_json_1_1(
                value["msk_source_configuration"]
            )
        )
    if "snowflake_destination_configuration" in value:
        import capo_firehose.types.snowflake_destination_configuration

        out["SnowflakeDestinationConfiguration"] = (
            capo_firehose.types.snowflake_destination_configuration.serialize_aws_json_1_1(
                value["snowflake_destination_configuration"]
            )
        )
    if "iceberg_destination_configuration" in value:
        import capo_firehose.types.iceberg_destination_configuration

        out["IcebergDestinationConfiguration"] = (
            capo_firehose.types.iceberg_destination_configuration.serialize_aws_json_1_1(
                value["iceberg_destination_configuration"]
            )
        )
    if "database_source_configuration" in value:
        import capo_firehose.types.database_source_configuration

        out["DatabaseSourceConfiguration"] = (
            capo_firehose.types.database_source_configuration.serialize_aws_json_1_1(
                value["database_source_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeliveryStreamInput:
    out: CreateDeliveryStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "CreateDeliveryStreamInput.delivery_stream_name required"
        )
    if data.get("DeliveryStreamType") is not None:
        import capo_firehose.types.delivery_stream_type

        out["delivery_stream_type"] = (
            capo_firehose.types.delivery_stream_type.deserialize_aws_json_1_1(
                data["DeliveryStreamType"]
            )
        )
    if data.get("DirectPutSourceConfiguration") is not None:
        import capo_firehose.types.direct_put_source_configuration

        out["direct_put_source_configuration"] = (
            capo_firehose.types.direct_put_source_configuration.deserialize_aws_json_1_1(
                data["DirectPutSourceConfiguration"]
            )
        )
    if data.get("KinesisStreamSourceConfiguration") is not None:
        import capo_firehose.types.kinesis_stream_source_configuration

        out["kinesis_stream_source_configuration"] = (
            capo_firehose.types.kinesis_stream_source_configuration.deserialize_aws_json_1_1(
                data["KinesisStreamSourceConfiguration"]
            )
        )
    if data.get("DeliveryStreamEncryptionConfigurationInput") is not None:
        import capo_firehose.types.delivery_stream_encryption_configuration_input

        out["delivery_stream_encryption_configuration_input"] = (
            capo_firehose.types.delivery_stream_encryption_configuration_input.deserialize_aws_json_1_1(
                data["DeliveryStreamEncryptionConfigurationInput"]
            )
        )
    if data.get("S3DestinationConfiguration") is not None:
        import capo_firehose.types.s3_destination_configuration

        out["s3_destination_configuration"] = (
            capo_firehose.types.s3_destination_configuration.deserialize_aws_json_1_1(
                data["S3DestinationConfiguration"]
            )
        )
    if data.get("ExtendedS3DestinationConfiguration") is not None:
        import capo_firehose.types.extended_s3_destination_configuration

        out["extended_s3_destination_configuration"] = (
            capo_firehose.types.extended_s3_destination_configuration.deserialize_aws_json_1_1(
                data["ExtendedS3DestinationConfiguration"]
            )
        )
    if data.get("RedshiftDestinationConfiguration") is not None:
        import capo_firehose.types.redshift_destination_configuration

        out["redshift_destination_configuration"] = (
            capo_firehose.types.redshift_destination_configuration.deserialize_aws_json_1_1(
                data["RedshiftDestinationConfiguration"]
            )
        )
    if data.get("ElasticsearchDestinationConfiguration") is not None:
        import capo_firehose.types.elasticsearch_destination_configuration

        out["elasticsearch_destination_configuration"] = (
            capo_firehose.types.elasticsearch_destination_configuration.deserialize_aws_json_1_1(
                data["ElasticsearchDestinationConfiguration"]
            )
        )
    if data.get("AmazonopensearchserviceDestinationConfiguration") is not None:
        import capo_firehose.types.amazonopensearchservice_destination_configuration

        out["amazonopensearchservice_destination_configuration"] = (
            capo_firehose.types.amazonopensearchservice_destination_configuration.deserialize_aws_json_1_1(
                data["AmazonopensearchserviceDestinationConfiguration"]
            )
        )
    if data.get("SplunkDestinationConfiguration") is not None:
        import capo_firehose.types.splunk_destination_configuration

        out["splunk_destination_configuration"] = (
            capo_firehose.types.splunk_destination_configuration.deserialize_aws_json_1_1(
                data["SplunkDestinationConfiguration"]
            )
        )
    if data.get("HttpEndpointDestinationConfiguration") is not None:
        import capo_firehose.types.http_endpoint_destination_configuration

        out["http_endpoint_destination_configuration"] = (
            capo_firehose.types.http_endpoint_destination_configuration.deserialize_aws_json_1_1(
                data["HttpEndpointDestinationConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_firehose.types.tag_delivery_stream_input_tag_list

        out["tags"] = (
            capo_firehose.types.tag_delivery_stream_input_tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    if data.get("AmazonOpenSearchServerlessDestinationConfiguration") is not None:
        import capo_firehose.types.amazon_open_search_serverless_destination_configuration

        out["amazon_open_search_serverless_destination_configuration"] = (
            capo_firehose.types.amazon_open_search_serverless_destination_configuration.deserialize_aws_json_1_1(
                data["AmazonOpenSearchServerlessDestinationConfiguration"]
            )
        )
    if data.get("MSKSourceConfiguration") is not None:
        import capo_firehose.types.msk_source_configuration

        out["msk_source_configuration"] = (
            capo_firehose.types.msk_source_configuration.deserialize_aws_json_1_1(
                data["MSKSourceConfiguration"]
            )
        )
    if data.get("SnowflakeDestinationConfiguration") is not None:
        import capo_firehose.types.snowflake_destination_configuration

        out["snowflake_destination_configuration"] = (
            capo_firehose.types.snowflake_destination_configuration.deserialize_aws_json_1_1(
                data["SnowflakeDestinationConfiguration"]
            )
        )
    if data.get("IcebergDestinationConfiguration") is not None:
        import capo_firehose.types.iceberg_destination_configuration

        out["iceberg_destination_configuration"] = (
            capo_firehose.types.iceberg_destination_configuration.deserialize_aws_json_1_1(
                data["IcebergDestinationConfiguration"]
            )
        )
    if data.get("DatabaseSourceConfiguration") is not None:
        import capo_firehose.types.database_source_configuration

        out["database_source_configuration"] = (
            capo_firehose.types.database_source_configuration.deserialize_aws_json_1_1(
                data["DatabaseSourceConfiguration"]
            )
        )
    return out
