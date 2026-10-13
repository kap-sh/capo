"""Generated from Smithy shape ``com.amazonaws.firehose#UpdateDestinationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.amazon_open_search_serverless_destination_update
    import capo_firehose.types.amazonopensearchservice_destination_update
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.delivery_stream_version_id
    import capo_firehose.types.destination_id
    import capo_firehose.types.elasticsearch_destination_update
    import capo_firehose.types.extended_s3_destination_update
    import capo_firehose.types.http_endpoint_destination_update
    import capo_firehose.types.iceberg_destination_update
    import capo_firehose.types.redshift_destination_update
    import capo_firehose.types.s3_destination_update
    import capo_firehose.types.snowflake_destination_update
    import capo_firehose.types.splunk_destination_update


class UpdateDestinationInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream.</p>"""
    current_delivery_stream_version_id: (
        "capo_firehose.types.delivery_stream_version_id.DeliveryStreamVersionId"
    )
    """<p>Obtain this value from the <code>VersionId</code> result of <a>DeliveryStreamDescription</a>. This value is required, and helps the service perform conditional operations. For example, if there is an interleaving update and this value is null, then the update destination fails. After the update is successful, the <code>VersionId</code> value is updated. The service then performs a merge of the old configuration with the new configuration.</p>"""
    destination_id: "capo_firehose.types.destination_id.DestinationId"
    """<p>The ID of the destination.</p>"""
    s3_destination_update: NotRequired[
        "capo_firehose.types.s3_destination_update.S3DestinationUpdate"
    ]
    """<p>[Deprecated] Describes an update for a destination in Amazon S3.</p>"""
    extended_s3_destination_update: NotRequired[
        "capo_firehose.types.extended_s3_destination_update.ExtendedS3DestinationUpdate"
    ]
    """<p>Describes an update for a destination in Amazon S3.</p>"""
    redshift_destination_update: NotRequired[
        "capo_firehose.types.redshift_destination_update.RedshiftDestinationUpdate"
    ]
    """<p>Describes an update for a destination in Amazon Redshift.</p>"""
    elasticsearch_destination_update: NotRequired[
        "capo_firehose.types.elasticsearch_destination_update.ElasticsearchDestinationUpdate"
    ]
    """<p>Describes an update for a destination in Amazon OpenSearch Service.</p>"""
    amazonopensearchservice_destination_update: NotRequired[
        "capo_firehose.types.amazonopensearchservice_destination_update.AmazonopensearchserviceDestinationUpdate"
    ]
    """<p>Describes an update for a destination in Amazon OpenSearch Service.</p>"""
    splunk_destination_update: NotRequired[
        "capo_firehose.types.splunk_destination_update.SplunkDestinationUpdate"
    ]
    """<p>Describes an update for a destination in Splunk.</p>"""
    http_endpoint_destination_update: NotRequired[
        "capo_firehose.types.http_endpoint_destination_update.HttpEndpointDestinationUpdate"
    ]
    """<p>Describes an update to the specified HTTP endpoint destination.</p>"""
    amazon_open_search_serverless_destination_update: NotRequired[
        "capo_firehose.types.amazon_open_search_serverless_destination_update.AmazonOpenSearchServerlessDestinationUpdate"
    ]
    """<p>Describes an update for a destination in the Serverless offering for Amazon OpenSearch Service.</p>"""
    snowflake_destination_update: NotRequired[
        "capo_firehose.types.snowflake_destination_update.SnowflakeDestinationUpdate"
    ]
    """<p>Update to the Snowflake destination configuration settings.</p>"""
    iceberg_destination_update: NotRequired[
        "capo_firehose.types.iceberg_destination_update.IcebergDestinationUpdate"
    ]
    """<p> Describes an update for a destination in Apache Iceberg Tables. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDestinationInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    out["CurrentDeliveryStreamVersionId"] = value["current_delivery_stream_version_id"]
    out["DestinationId"] = value["destination_id"]
    if "s3_destination_update" in value:
        import capo_firehose.types.s3_destination_update

        out["S3DestinationUpdate"] = (
            capo_firehose.types.s3_destination_update.serialize_aws_json_1_1(
                value["s3_destination_update"]
            )
        )
    if "extended_s3_destination_update" in value:
        import capo_firehose.types.extended_s3_destination_update

        out["ExtendedS3DestinationUpdate"] = (
            capo_firehose.types.extended_s3_destination_update.serialize_aws_json_1_1(
                value["extended_s3_destination_update"]
            )
        )
    if "redshift_destination_update" in value:
        import capo_firehose.types.redshift_destination_update

        out["RedshiftDestinationUpdate"] = (
            capo_firehose.types.redshift_destination_update.serialize_aws_json_1_1(
                value["redshift_destination_update"]
            )
        )
    if "elasticsearch_destination_update" in value:
        import capo_firehose.types.elasticsearch_destination_update

        out["ElasticsearchDestinationUpdate"] = (
            capo_firehose.types.elasticsearch_destination_update.serialize_aws_json_1_1(
                value["elasticsearch_destination_update"]
            )
        )
    if "amazonopensearchservice_destination_update" in value:
        import capo_firehose.types.amazonopensearchservice_destination_update

        out["AmazonopensearchserviceDestinationUpdate"] = (
            capo_firehose.types.amazonopensearchservice_destination_update.serialize_aws_json_1_1(
                value["amazonopensearchservice_destination_update"]
            )
        )
    if "splunk_destination_update" in value:
        import capo_firehose.types.splunk_destination_update

        out["SplunkDestinationUpdate"] = (
            capo_firehose.types.splunk_destination_update.serialize_aws_json_1_1(
                value["splunk_destination_update"]
            )
        )
    if "http_endpoint_destination_update" in value:
        import capo_firehose.types.http_endpoint_destination_update

        out["HttpEndpointDestinationUpdate"] = (
            capo_firehose.types.http_endpoint_destination_update.serialize_aws_json_1_1(
                value["http_endpoint_destination_update"]
            )
        )
    if "amazon_open_search_serverless_destination_update" in value:
        import capo_firehose.types.amazon_open_search_serverless_destination_update

        out["AmazonOpenSearchServerlessDestinationUpdate"] = (
            capo_firehose.types.amazon_open_search_serverless_destination_update.serialize_aws_json_1_1(
                value["amazon_open_search_serverless_destination_update"]
            )
        )
    if "snowflake_destination_update" in value:
        import capo_firehose.types.snowflake_destination_update

        out["SnowflakeDestinationUpdate"] = (
            capo_firehose.types.snowflake_destination_update.serialize_aws_json_1_1(
                value["snowflake_destination_update"]
            )
        )
    if "iceberg_destination_update" in value:
        import capo_firehose.types.iceberg_destination_update

        out["IcebergDestinationUpdate"] = (
            capo_firehose.types.iceberg_destination_update.serialize_aws_json_1_1(
                value["iceberg_destination_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDestinationInput:
    out: UpdateDestinationInput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "UpdateDestinationInput.delivery_stream_name required"
        )
    if data.get("CurrentDeliveryStreamVersionId") is not None:
        out["current_delivery_stream_version_id"] = data[
            "CurrentDeliveryStreamVersionId"
        ]
    else:
        raise DeserializationError(
            "UpdateDestinationInput.current_delivery_stream_version_id required"
        )
    if data.get("DestinationId") is not None:
        out["destination_id"] = data["DestinationId"]
    else:
        raise DeserializationError("UpdateDestinationInput.destination_id required")
    if data.get("S3DestinationUpdate") is not None:
        import capo_firehose.types.s3_destination_update

        out["s3_destination_update"] = (
            capo_firehose.types.s3_destination_update.deserialize_aws_json_1_1(
                data["S3DestinationUpdate"]
            )
        )
    if data.get("ExtendedS3DestinationUpdate") is not None:
        import capo_firehose.types.extended_s3_destination_update

        out["extended_s3_destination_update"] = (
            capo_firehose.types.extended_s3_destination_update.deserialize_aws_json_1_1(
                data["ExtendedS3DestinationUpdate"]
            )
        )
    if data.get("RedshiftDestinationUpdate") is not None:
        import capo_firehose.types.redshift_destination_update

        out["redshift_destination_update"] = (
            capo_firehose.types.redshift_destination_update.deserialize_aws_json_1_1(
                data["RedshiftDestinationUpdate"]
            )
        )
    if data.get("ElasticsearchDestinationUpdate") is not None:
        import capo_firehose.types.elasticsearch_destination_update

        out["elasticsearch_destination_update"] = (
            capo_firehose.types.elasticsearch_destination_update.deserialize_aws_json_1_1(
                data["ElasticsearchDestinationUpdate"]
            )
        )
    if data.get("AmazonopensearchserviceDestinationUpdate") is not None:
        import capo_firehose.types.amazonopensearchservice_destination_update

        out["amazonopensearchservice_destination_update"] = (
            capo_firehose.types.amazonopensearchservice_destination_update.deserialize_aws_json_1_1(
                data["AmazonopensearchserviceDestinationUpdate"]
            )
        )
    if data.get("SplunkDestinationUpdate") is not None:
        import capo_firehose.types.splunk_destination_update

        out["splunk_destination_update"] = (
            capo_firehose.types.splunk_destination_update.deserialize_aws_json_1_1(
                data["SplunkDestinationUpdate"]
            )
        )
    if data.get("HttpEndpointDestinationUpdate") is not None:
        import capo_firehose.types.http_endpoint_destination_update

        out["http_endpoint_destination_update"] = (
            capo_firehose.types.http_endpoint_destination_update.deserialize_aws_json_1_1(
                data["HttpEndpointDestinationUpdate"]
            )
        )
    if data.get("AmazonOpenSearchServerlessDestinationUpdate") is not None:
        import capo_firehose.types.amazon_open_search_serverless_destination_update

        out["amazon_open_search_serverless_destination_update"] = (
            capo_firehose.types.amazon_open_search_serverless_destination_update.deserialize_aws_json_1_1(
                data["AmazonOpenSearchServerlessDestinationUpdate"]
            )
        )
    if data.get("SnowflakeDestinationUpdate") is not None:
        import capo_firehose.types.snowflake_destination_update

        out["snowflake_destination_update"] = (
            capo_firehose.types.snowflake_destination_update.deserialize_aws_json_1_1(
                data["SnowflakeDestinationUpdate"]
            )
        )
    if data.get("IcebergDestinationUpdate") is not None:
        import capo_firehose.types.iceberg_destination_update

        out["iceberg_destination_update"] = (
            capo_firehose.types.iceberg_destination_update.deserialize_aws_json_1_1(
                data["IcebergDestinationUpdate"]
            )
        )
    return out


def redact_sensitive(value: UpdateDestinationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "redshift_destination_update" in value:
        import capo_firehose.types.redshift_destination_update

        out["redshift_destination_update"] = (
            capo_firehose.types.redshift_destination_update.redact_sensitive(
                value["redshift_destination_update"]
            )
        )
    if "http_endpoint_destination_update" in value:
        import capo_firehose.types.http_endpoint_destination_update

        out["http_endpoint_destination_update"] = (
            capo_firehose.types.http_endpoint_destination_update.redact_sensitive(
                value["http_endpoint_destination_update"]
            )
        )
    if "snowflake_destination_update" in value:
        import capo_firehose.types.snowflake_destination_update

        out["snowflake_destination_update"] = (
            capo_firehose.types.snowflake_destination_update.redact_sensitive(
                value["snowflake_destination_update"]
            )
        )
    return out
