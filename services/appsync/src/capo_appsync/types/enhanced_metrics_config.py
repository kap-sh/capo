"""Generated from Smithy shape ``com.amazonaws.appsync#EnhancedMetricsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_source_level_metrics_behavior
    import capo_appsync.types.operation_level_metrics_config
    import capo_appsync.types.resolver_level_metrics_behavior


class EnhancedMetricsConfig(TypedDict, closed=True):
    resolver_level_metrics_behavior: "capo_appsync.types.resolver_level_metrics_behavior.ResolverLevelMetricsBehavior"
    """<p>Controls how resolver metrics will be emitted to CloudWatch. Resolver metrics include:</p> <ul> <li> <p>GraphQL errors: The number of GraphQL errors that occurred.</p> </li> <li> <p>Requests: The number of invocations that occurred during a request. </p> </li> <li> <p>Latency: The time to complete a resolver invocation.</p> </li> <li> <p>Cache hits: The number of cache hits during a request.</p> </li> <li> <p>Cache misses: The number of cache misses during a request.</p> </li> </ul> <p>These metrics can be emitted to CloudWatch per resolver or for all resolvers in the request. Metrics will be recorded by API ID and resolver name. <code>resolverLevelMetricsBehavior</code> accepts one of these values at a time:</p> <ul> <li> <p> <code>FULL_REQUEST_RESOLVER_METRICS</code>: Records and emits metric data for all resolvers in the request.</p> </li> <li> <p> <code>PER_RESOLVER_METRICS</code>: Records and emits metric data for resolvers that have the <code>metricsConfig</code> value set to <code>ENABLED</code>.</p> </li> </ul>"""
    data_source_level_metrics_behavior: "capo_appsync.types.data_source_level_metrics_behavior.DataSourceLevelMetricsBehavior"
    """<p>Controls how data source metrics will be emitted to CloudWatch. Data source metrics include:</p> <ul> <li> <p>Requests: The number of invocations that occured during a request.</p> </li> <li> <p>Latency: The time to complete a data source invocation.</p> </li> <li> <p>Errors: The number of errors that occurred during a data source invocation.</p> </li> </ul> <p>These metrics can be emitted to CloudWatch per data source or for all data sources in the request. Metrics will be recorded by API ID and data source name. <code>dataSourceLevelMetricsBehavior</code> accepts one of these values at a time:</p> <ul> <li> <p> <code>FULL_REQUEST_DATA_SOURCE_METRICS</code>: Records and emits metric data for all data sources in the request.</p> </li> <li> <p> <code>PER_DATA_SOURCE_METRICS</code>: Records and emits metric data for data sources that have the <code>metricsConfig</code> value set to <code>ENABLED</code>.</p> </li> </ul>"""
    operation_level_metrics_config: (
        "capo_appsync.types.operation_level_metrics_config.OperationLevelMetricsConfig"
    )
    """<p> Controls how operation metrics will be emitted to CloudWatch. Operation metrics include:</p> <ul> <li> <p>Requests: The number of times a specified GraphQL operation was called.</p> </li> <li> <p>GraphQL errors: The number of GraphQL errors that occurred during a specified GraphQL operation.</p> </li> </ul> <p>Metrics will be recorded by API ID and operation name. You can set the value to <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnhancedMetricsConfig) -> dict:
    out: dict = {}
    import capo_appsync.types.resolver_level_metrics_behavior

    out["resolverLevelMetricsBehavior"] = (
        capo_appsync.types.resolver_level_metrics_behavior.serialize_json(
            value["resolver_level_metrics_behavior"]
        )
    )
    import capo_appsync.types.data_source_level_metrics_behavior

    out["dataSourceLevelMetricsBehavior"] = (
        capo_appsync.types.data_source_level_metrics_behavior.serialize_json(
            value["data_source_level_metrics_behavior"]
        )
    )
    import capo_appsync.types.operation_level_metrics_config

    out["operationLevelMetricsConfig"] = (
        capo_appsync.types.operation_level_metrics_config.serialize_json(
            value["operation_level_metrics_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> EnhancedMetricsConfig:
    out: EnhancedMetricsConfig = {}  # type: ignore[typeddict-item]
    if data.get("resolverLevelMetricsBehavior") is not None:
        import capo_appsync.types.resolver_level_metrics_behavior

        out["resolver_level_metrics_behavior"] = (
            capo_appsync.types.resolver_level_metrics_behavior.deserialize_json(
                data["resolverLevelMetricsBehavior"]
            )
        )
    else:
        import typing

        out["resolver_level_metrics_behavior"] = typing.cast(
            "capo_appsync.types.resolver_level_metrics_behavior.ResolverLevelMetricsBehavior",
            "",
        )
    if data.get("dataSourceLevelMetricsBehavior") is not None:
        import capo_appsync.types.data_source_level_metrics_behavior

        out["data_source_level_metrics_behavior"] = (
            capo_appsync.types.data_source_level_metrics_behavior.deserialize_json(
                data["dataSourceLevelMetricsBehavior"]
            )
        )
    else:
        import typing

        out["data_source_level_metrics_behavior"] = typing.cast(
            "capo_appsync.types.data_source_level_metrics_behavior.DataSourceLevelMetricsBehavior",
            "",
        )
    if data.get("operationLevelMetricsConfig") is not None:
        import capo_appsync.types.operation_level_metrics_config

        out["operation_level_metrics_config"] = (
            capo_appsync.types.operation_level_metrics_config.deserialize_json(
                data["operationLevelMetricsConfig"]
            )
        )
    else:
        import typing

        out["operation_level_metrics_config"] = typing.cast(
            "capo_appsync.types.operation_level_metrics_config.OperationLevelMetricsConfig",
            "",
        )
    return out
