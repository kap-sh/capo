"""Generated from Smithy shape ``com.amazonaws.firehose#DestinationDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.amazon_open_search_serverless_destination_description
    import capo_firehose.types.amazonopensearchservice_destination_description
    import capo_firehose.types.destination_id
    import capo_firehose.types.elasticsearch_destination_description
    import capo_firehose.types.extended_s3_destination_description
    import capo_firehose.types.http_endpoint_destination_description
    import capo_firehose.types.iceberg_destination_description
    import capo_firehose.types.redshift_destination_description
    import capo_firehose.types.s3_destination_description
    import capo_firehose.types.snowflake_destination_description
    import capo_firehose.types.splunk_destination_description


class DestinationDescription(TypedDict, closed=True):
    destination_id: "capo_firehose.types.destination_id.DestinationId"
    """<p>The ID of the destination.</p>"""
    s3_destination_description: NotRequired[
        "capo_firehose.types.s3_destination_description.S3DestinationDescription"
    ]
    """<p>[Deprecated] The destination in Amazon S3.</p>"""
    extended_s3_destination_description: NotRequired[
        "capo_firehose.types.extended_s3_destination_description.ExtendedS3DestinationDescription"
    ]
    """<p>The destination in Amazon S3.</p>"""
    redshift_destination_description: NotRequired[
        "capo_firehose.types.redshift_destination_description.RedshiftDestinationDescription"
    ]
    """<p>The destination in Amazon Redshift.</p>"""
    elasticsearch_destination_description: NotRequired[
        "capo_firehose.types.elasticsearch_destination_description.ElasticsearchDestinationDescription"
    ]
    """<p>The destination in Amazon OpenSearch Service.</p>"""
    amazonopensearchservice_destination_description: NotRequired[
        "capo_firehose.types.amazonopensearchservice_destination_description.AmazonopensearchserviceDestinationDescription"
    ]
    """<p>The destination in Amazon OpenSearch Service.</p>"""
    splunk_destination_description: NotRequired[
        "capo_firehose.types.splunk_destination_description.SplunkDestinationDescription"
    ]
    """<p>The destination in Splunk.</p>"""
    http_endpoint_destination_description: NotRequired[
        "capo_firehose.types.http_endpoint_destination_description.HttpEndpointDestinationDescription"
    ]
    """<p>Describes the specified HTTP endpoint destination.</p>"""
    snowflake_destination_description: NotRequired[
        "capo_firehose.types.snowflake_destination_description.SnowflakeDestinationDescription"
    ]
    """<p>Optional description for the destination</p>"""
    amazon_open_search_serverless_destination_description: NotRequired[
        "capo_firehose.types.amazon_open_search_serverless_destination_description.AmazonOpenSearchServerlessDestinationDescription"
    ]
    """<p>The destination in the Serverless offering for Amazon OpenSearch Service.</p>"""
    iceberg_destination_description: NotRequired[
        "capo_firehose.types.iceberg_destination_description.IcebergDestinationDescription"
    ]
    """<p> Describes a destination in Apache Iceberg Tables. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationDescription) -> dict:
    out: dict = {}
    out["DestinationId"] = value["destination_id"]
    if "s3_destination_description" in value:
        import capo_firehose.types.s3_destination_description

        out["S3DestinationDescription"] = (
            capo_firehose.types.s3_destination_description.serialize_aws_json_1_1(
                value["s3_destination_description"]
            )
        )
    if "extended_s3_destination_description" in value:
        import capo_firehose.types.extended_s3_destination_description

        out["ExtendedS3DestinationDescription"] = (
            capo_firehose.types.extended_s3_destination_description.serialize_aws_json_1_1(
                value["extended_s3_destination_description"]
            )
        )
    if "redshift_destination_description" in value:
        import capo_firehose.types.redshift_destination_description

        out["RedshiftDestinationDescription"] = (
            capo_firehose.types.redshift_destination_description.serialize_aws_json_1_1(
                value["redshift_destination_description"]
            )
        )
    if "elasticsearch_destination_description" in value:
        import capo_firehose.types.elasticsearch_destination_description

        out["ElasticsearchDestinationDescription"] = (
            capo_firehose.types.elasticsearch_destination_description.serialize_aws_json_1_1(
                value["elasticsearch_destination_description"]
            )
        )
    if "amazonopensearchservice_destination_description" in value:
        import capo_firehose.types.amazonopensearchservice_destination_description

        out["AmazonopensearchserviceDestinationDescription"] = (
            capo_firehose.types.amazonopensearchservice_destination_description.serialize_aws_json_1_1(
                value["amazonopensearchservice_destination_description"]
            )
        )
    if "splunk_destination_description" in value:
        import capo_firehose.types.splunk_destination_description

        out["SplunkDestinationDescription"] = (
            capo_firehose.types.splunk_destination_description.serialize_aws_json_1_1(
                value["splunk_destination_description"]
            )
        )
    if "http_endpoint_destination_description" in value:
        import capo_firehose.types.http_endpoint_destination_description

        out["HttpEndpointDestinationDescription"] = (
            capo_firehose.types.http_endpoint_destination_description.serialize_aws_json_1_1(
                value["http_endpoint_destination_description"]
            )
        )
    if "snowflake_destination_description" in value:
        import capo_firehose.types.snowflake_destination_description

        out["SnowflakeDestinationDescription"] = (
            capo_firehose.types.snowflake_destination_description.serialize_aws_json_1_1(
                value["snowflake_destination_description"]
            )
        )
    if "amazon_open_search_serverless_destination_description" in value:
        import capo_firehose.types.amazon_open_search_serverless_destination_description

        out["AmazonOpenSearchServerlessDestinationDescription"] = (
            capo_firehose.types.amazon_open_search_serverless_destination_description.serialize_aws_json_1_1(
                value["amazon_open_search_serverless_destination_description"]
            )
        )
    if "iceberg_destination_description" in value:
        import capo_firehose.types.iceberg_destination_description

        out["IcebergDestinationDescription"] = (
            capo_firehose.types.iceberg_destination_description.serialize_aws_json_1_1(
                value["iceberg_destination_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationDescription:
    out: DestinationDescription = {}  # type: ignore[typeddict-item]
    if data.get("DestinationId") is not None:
        out["destination_id"] = data["DestinationId"]
    else:
        raise DeserializationError("DestinationDescription.destination_id required")
    if data.get("S3DestinationDescription") is not None:
        import capo_firehose.types.s3_destination_description

        out["s3_destination_description"] = (
            capo_firehose.types.s3_destination_description.deserialize_aws_json_1_1(
                data["S3DestinationDescription"]
            )
        )
    if data.get("ExtendedS3DestinationDescription") is not None:
        import capo_firehose.types.extended_s3_destination_description

        out["extended_s3_destination_description"] = (
            capo_firehose.types.extended_s3_destination_description.deserialize_aws_json_1_1(
                data["ExtendedS3DestinationDescription"]
            )
        )
    if data.get("RedshiftDestinationDescription") is not None:
        import capo_firehose.types.redshift_destination_description

        out["redshift_destination_description"] = (
            capo_firehose.types.redshift_destination_description.deserialize_aws_json_1_1(
                data["RedshiftDestinationDescription"]
            )
        )
    if data.get("ElasticsearchDestinationDescription") is not None:
        import capo_firehose.types.elasticsearch_destination_description

        out["elasticsearch_destination_description"] = (
            capo_firehose.types.elasticsearch_destination_description.deserialize_aws_json_1_1(
                data["ElasticsearchDestinationDescription"]
            )
        )
    if data.get("AmazonopensearchserviceDestinationDescription") is not None:
        import capo_firehose.types.amazonopensearchservice_destination_description

        out["amazonopensearchservice_destination_description"] = (
            capo_firehose.types.amazonopensearchservice_destination_description.deserialize_aws_json_1_1(
                data["AmazonopensearchserviceDestinationDescription"]
            )
        )
    if data.get("SplunkDestinationDescription") is not None:
        import capo_firehose.types.splunk_destination_description

        out["splunk_destination_description"] = (
            capo_firehose.types.splunk_destination_description.deserialize_aws_json_1_1(
                data["SplunkDestinationDescription"]
            )
        )
    if data.get("HttpEndpointDestinationDescription") is not None:
        import capo_firehose.types.http_endpoint_destination_description

        out["http_endpoint_destination_description"] = (
            capo_firehose.types.http_endpoint_destination_description.deserialize_aws_json_1_1(
                data["HttpEndpointDestinationDescription"]
            )
        )
    if data.get("SnowflakeDestinationDescription") is not None:
        import capo_firehose.types.snowflake_destination_description

        out["snowflake_destination_description"] = (
            capo_firehose.types.snowflake_destination_description.deserialize_aws_json_1_1(
                data["SnowflakeDestinationDescription"]
            )
        )
    if data.get("AmazonOpenSearchServerlessDestinationDescription") is not None:
        import capo_firehose.types.amazon_open_search_serverless_destination_description

        out["amazon_open_search_serverless_destination_description"] = (
            capo_firehose.types.amazon_open_search_serverless_destination_description.deserialize_aws_json_1_1(
                data["AmazonOpenSearchServerlessDestinationDescription"]
            )
        )
    if data.get("IcebergDestinationDescription") is not None:
        import capo_firehose.types.iceberg_destination_description

        out["iceberg_destination_description"] = (
            capo_firehose.types.iceberg_destination_description.deserialize_aws_json_1_1(
                data["IcebergDestinationDescription"]
            )
        )
    return out


def redact_sensitive(value: DestinationDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "redshift_destination_description" in value:
        import capo_firehose.types.redshift_destination_description

        out["redshift_destination_description"] = (
            capo_firehose.types.redshift_destination_description.redact_sensitive(
                value["redshift_destination_description"]
            )
        )
    if "http_endpoint_destination_description" in value:
        import capo_firehose.types.http_endpoint_destination_description

        out["http_endpoint_destination_description"] = (
            capo_firehose.types.http_endpoint_destination_description.redact_sensitive(
                value["http_endpoint_destination_description"]
            )
        )
    if "snowflake_destination_description" in value:
        import capo_firehose.types.snowflake_destination_description

        out["snowflake_destination_description"] = (
            capo_firehose.types.snowflake_destination_description.redact_sensitive(
                value["snowflake_destination_description"]
            )
        )
    return out
