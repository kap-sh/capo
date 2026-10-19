"""Generated from Smithy shape ``com.amazonaws.appsync#CreateDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_source_level_metrics_config
    import capo_appsync.types.data_source_type
    import capo_appsync.types.dynamodb_data_source_config
    import capo_appsync.types.elasticsearch_data_source_config
    import capo_appsync.types.event_bridge_data_source_config
    import capo_appsync.types.http_data_source_config
    import capo_appsync.types.lambda_data_source_config
    import capo_appsync.types.open_search_service_data_source_config
    import capo_appsync.types.relational_database_data_source_config
    import capo_appsync.types.resource_name
    import capo_appsync.types.string


class CreateDataSourceRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID for the GraphQL API for the <code>DataSource</code>.</p>"""
    name: "capo_appsync.types.resource_name.ResourceName"
    """<p>A user-supplied name for the <code>DataSource</code>.</p>"""
    description: NotRequired["capo_appsync.types.string.String"]
    """<p>A description of the <code>DataSource</code>.</p>"""
    type: "capo_appsync.types.data_source_type.DataSourceType"
    """<p>The type of the <code>DataSource</code>.</p>"""
    service_role_arn: NotRequired["capo_appsync.types.string.String"]
    """<p>The Identity and Access Management (IAM) service role Amazon Resource Name (ARN) for the data source. The system assumes this role when accessing the data source.</p>"""
    dynamodb_config: NotRequired[
        "capo_appsync.types.dynamodb_data_source_config.DynamodbDataSourceConfig"
    ]
    """<p>Amazon DynamoDB settings.</p>"""
    lambda_config: NotRequired[
        "capo_appsync.types.lambda_data_source_config.LambdaDataSourceConfig"
    ]
    """<p>Lambda settings.</p>"""
    elasticsearch_config: NotRequired[
        "capo_appsync.types.elasticsearch_data_source_config.ElasticsearchDataSourceConfig"
    ]
    """<p>Amazon OpenSearch Service settings.</p> <p>As of September 2021, Amazon Elasticsearch service is Amazon OpenSearch Service. This configuration is deprecated. For new data sources, use <a>CreateDataSourceRequest$openSearchServiceConfig</a> to create an OpenSearch data source.</p>"""
    open_search_service_config: NotRequired[
        "capo_appsync.types.open_search_service_data_source_config.OpenSearchServiceDataSourceConfig"
    ]
    """<p>Amazon OpenSearch Service settings.</p>"""
    http_config: NotRequired[
        "capo_appsync.types.http_data_source_config.HttpDataSourceConfig"
    ]
    """<p>HTTP endpoint settings.</p>"""
    relational_database_config: NotRequired[
        "capo_appsync.types.relational_database_data_source_config.RelationalDatabaseDataSourceConfig"
    ]
    """<p>Relational database settings.</p>"""
    event_bridge_config: NotRequired[
        "capo_appsync.types.event_bridge_data_source_config.EventBridgeDataSourceConfig"
    ]
    """<p>Amazon EventBridge settings.</p>"""
    metrics_config: NotRequired[
        "capo_appsync.types.data_source_level_metrics_config.DataSourceLevelMetricsConfig"
    ]
    """<p>Enables or disables enhanced data source metrics for specified data sources. Note that <code>metricsConfig</code> won't be used unless the <code>dataSourceLevelMetricsBehavior</code> value is set to <code>PER_DATA_SOURCE_METRICS</code>. If the <code>dataSourceLevelMetricsBehavior</code> is set to <code>FULL_REQUEST_DATA_SOURCE_METRICS</code> instead, <code>metricsConfig</code> will be ignored. However, you can still set its value.</p> <p> <code>metricsConfig</code> can be <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_appsync.types.data_source_type

    out["type"] = capo_appsync.types.data_source_type.serialize_json(value["type"])
    if "service_role_arn" in value:
        out["serviceRoleArn"] = value["service_role_arn"]
    if "dynamodb_config" in value:
        import capo_appsync.types.dynamodb_data_source_config

        out["dynamodbConfig"] = (
            capo_appsync.types.dynamodb_data_source_config.serialize_json(
                value["dynamodb_config"]
            )
        )
    if "lambda_config" in value:
        import capo_appsync.types.lambda_data_source_config

        out["lambdaConfig"] = (
            capo_appsync.types.lambda_data_source_config.serialize_json(
                value["lambda_config"]
            )
        )
    if "elasticsearch_config" in value:
        import capo_appsync.types.elasticsearch_data_source_config

        out["elasticsearchConfig"] = (
            capo_appsync.types.elasticsearch_data_source_config.serialize_json(
                value["elasticsearch_config"]
            )
        )
    if "open_search_service_config" in value:
        import capo_appsync.types.open_search_service_data_source_config

        out["openSearchServiceConfig"] = (
            capo_appsync.types.open_search_service_data_source_config.serialize_json(
                value["open_search_service_config"]
            )
        )
    if "http_config" in value:
        import capo_appsync.types.http_data_source_config

        out["httpConfig"] = capo_appsync.types.http_data_source_config.serialize_json(
            value["http_config"]
        )
    if "relational_database_config" in value:
        import capo_appsync.types.relational_database_data_source_config

        out["relationalDatabaseConfig"] = (
            capo_appsync.types.relational_database_data_source_config.serialize_json(
                value["relational_database_config"]
            )
        )
    if "event_bridge_config" in value:
        import capo_appsync.types.event_bridge_data_source_config

        out["eventBridgeConfig"] = (
            capo_appsync.types.event_bridge_data_source_config.serialize_json(
                value["event_bridge_config"]
            )
        )
    if "metrics_config" in value:
        import capo_appsync.types.data_source_level_metrics_config

        out["metricsConfig"] = (
            capo_appsync.types.data_source_level_metrics_config.serialize_json(
                value["metrics_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDataSourceRequest:
    out: CreateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_appsync.types.data_source_type

        out["type"] = capo_appsync.types.data_source_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast(
            "capo_appsync.types.data_source_type.DataSourceType", ""
        )
    if data.get("serviceRoleArn") is not None:
        out["service_role_arn"] = data["serviceRoleArn"]
    if data.get("dynamodbConfig") is not None:
        import capo_appsync.types.dynamodb_data_source_config

        out["dynamodb_config"] = (
            capo_appsync.types.dynamodb_data_source_config.deserialize_json(
                data["dynamodbConfig"]
            )
        )
    if data.get("lambdaConfig") is not None:
        import capo_appsync.types.lambda_data_source_config

        out["lambda_config"] = (
            capo_appsync.types.lambda_data_source_config.deserialize_json(
                data["lambdaConfig"]
            )
        )
    if data.get("elasticsearchConfig") is not None:
        import capo_appsync.types.elasticsearch_data_source_config

        out["elasticsearch_config"] = (
            capo_appsync.types.elasticsearch_data_source_config.deserialize_json(
                data["elasticsearchConfig"]
            )
        )
    if data.get("openSearchServiceConfig") is not None:
        import capo_appsync.types.open_search_service_data_source_config

        out["open_search_service_config"] = (
            capo_appsync.types.open_search_service_data_source_config.deserialize_json(
                data["openSearchServiceConfig"]
            )
        )
    if data.get("httpConfig") is not None:
        import capo_appsync.types.http_data_source_config

        out["http_config"] = (
            capo_appsync.types.http_data_source_config.deserialize_json(
                data["httpConfig"]
            )
        )
    if data.get("relationalDatabaseConfig") is not None:
        import capo_appsync.types.relational_database_data_source_config

        out["relational_database_config"] = (
            capo_appsync.types.relational_database_data_source_config.deserialize_json(
                data["relationalDatabaseConfig"]
            )
        )
    if data.get("eventBridgeConfig") is not None:
        import capo_appsync.types.event_bridge_data_source_config

        out["event_bridge_config"] = (
            capo_appsync.types.event_bridge_data_source_config.deserialize_json(
                data["eventBridgeConfig"]
            )
        )
    if data.get("metricsConfig") is not None:
        import capo_appsync.types.data_source_level_metrics_config

        out["metrics_config"] = (
            capo_appsync.types.data_source_level_metrics_config.deserialize_json(
                data["metricsConfig"]
            )
        )
    return out
