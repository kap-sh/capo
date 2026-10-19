"""Generated from Smithy shape ``com.amazonaws.appsync#CreateResolverRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.app_sync_runtime
    import capo_appsync.types.caching_config
    import capo_appsync.types.code
    import capo_appsync.types.mapping_template
    import capo_appsync.types.max_batch_size
    import capo_appsync.types.pipeline_config
    import capo_appsync.types.resolver_kind
    import capo_appsync.types.resolver_level_metrics_config
    import capo_appsync.types.resource_name
    import capo_appsync.types.string
    import capo_appsync.types.sync_config


class CreateResolverRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The ID for the GraphQL API for which the resolver is being created.</p>"""
    type_name: "capo_appsync.types.resource_name.ResourceName"
    """<p>The name of the <code>Type</code>.</p>"""
    field_name: "capo_appsync.types.resource_name.ResourceName"
    """<p>The name of the field to attach the resolver to.</p>"""
    data_source_name: NotRequired["capo_appsync.types.resource_name.ResourceName"]
    """<p>The name of the data source for which the resolver is being created.</p>"""
    request_mapping_template: NotRequired[
        "capo_appsync.types.mapping_template.MappingTemplate"
    ]
    """<p>The mapping template to use for requests.</p> <p>A resolver uses a request mapping template to convert a GraphQL expression into a format that a data source can understand. Mapping templates are written in Apache Velocity Template Language (VTL).</p> <p>VTL request mapping templates are optional when using an Lambda data source. For all other data sources, VTL request and response mapping templates are required.</p>"""
    response_mapping_template: NotRequired[
        "capo_appsync.types.mapping_template.MappingTemplate"
    ]
    """<p>The mapping template to use for responses from the data source.</p>"""
    kind: NotRequired["capo_appsync.types.resolver_kind.ResolverKind"]
    """<p>The resolver type.</p> <ul> <li> <p> <b>UNIT</b>: A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.</p> </li> <li> <p> <b>PIPELINE</b>: A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of <code>Function</code> objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.</p> </li> </ul>"""
    pipeline_config: NotRequired["capo_appsync.types.pipeline_config.PipelineConfig"]
    """<p>The <code>PipelineConfig</code>.</p>"""
    sync_config: NotRequired["capo_appsync.types.sync_config.SyncConfig"]
    """<p>The <code>SyncConfig</code> for a resolver attached to a versioned data source.</p>"""
    caching_config: NotRequired["capo_appsync.types.caching_config.CachingConfig"]
    """<p>The caching configuration for the resolver.</p>"""
    max_batch_size: NotRequired["capo_appsync.types.max_batch_size.MaxBatchSize"]
    """<p>The maximum batching size for a resolver.</p>"""
    runtime: NotRequired["capo_appsync.types.app_sync_runtime.AppSyncRuntime"]
    code: NotRequired["capo_appsync.types.code.Code"]
    """<p>The <code>resolver</code> code that contains the request and response functions. When code is used, the <code>runtime</code> is required. The <code>runtime</code> value must be <code>APPSYNC_JS</code>.</p>"""
    metrics_config: NotRequired[
        "capo_appsync.types.resolver_level_metrics_config.ResolverLevelMetricsConfig"
    ]
    """<p>Enables or disables enhanced resolver metrics for specified resolvers. Note that <code>metricsConfig</code> won't be used unless the <code>resolverLevelMetricsBehavior</code> value is set to <code>PER_RESOLVER_METRICS</code>. If the <code>resolverLevelMetricsBehavior</code> is set to <code>FULL_REQUEST_RESOLVER_METRICS</code> instead, <code>metricsConfig</code> will be ignored. However, you can still set its value.</p> <p> <code>metricsConfig</code> can be <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResolverRequest) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    if "data_source_name" in value:
        out["dataSourceName"] = value["data_source_name"]
    if "request_mapping_template" in value:
        out["requestMappingTemplate"] = value["request_mapping_template"]
    if "response_mapping_template" in value:
        out["responseMappingTemplate"] = value["response_mapping_template"]
    if "kind" in value:
        import capo_appsync.types.resolver_kind

        out["kind"] = capo_appsync.types.resolver_kind.serialize_json(value["kind"])
    if "pipeline_config" in value:
        import capo_appsync.types.pipeline_config

        out["pipelineConfig"] = capo_appsync.types.pipeline_config.serialize_json(
            value["pipeline_config"]
        )
    if "sync_config" in value:
        import capo_appsync.types.sync_config

        out["syncConfig"] = capo_appsync.types.sync_config.serialize_json(
            value["sync_config"]
        )
    if "caching_config" in value:
        import capo_appsync.types.caching_config

        out["cachingConfig"] = capo_appsync.types.caching_config.serialize_json(
            value["caching_config"]
        )
    if "max_batch_size" in value:
        out["maxBatchSize"] = value["max_batch_size"]
    if "runtime" in value:
        import capo_appsync.types.app_sync_runtime

        out["runtime"] = capo_appsync.types.app_sync_runtime.serialize_json(
            value["runtime"]
        )
    if "code" in value:
        out["code"] = value["code"]
    if "metrics_config" in value:
        import capo_appsync.types.resolver_level_metrics_config

        out["metricsConfig"] = (
            capo_appsync.types.resolver_level_metrics_config.serialize_json(
                value["metrics_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateResolverRequest:
    out: CreateResolverRequest = {}  # type: ignore[typeddict-item]
    if data.get("fieldName") is not None:
        out["field_name"] = data["fieldName"]
    else:
        raise DeserializationError("CreateResolverRequest.field_name required")
    if data.get("dataSourceName") is not None:
        out["data_source_name"] = data["dataSourceName"]
    if data.get("requestMappingTemplate") is not None:
        out["request_mapping_template"] = data["requestMappingTemplate"]
    if data.get("responseMappingTemplate") is not None:
        out["response_mapping_template"] = data["responseMappingTemplate"]
    if data.get("kind") is not None:
        import capo_appsync.types.resolver_kind

        out["kind"] = capo_appsync.types.resolver_kind.deserialize_json(data["kind"])
    if data.get("pipelineConfig") is not None:
        import capo_appsync.types.pipeline_config

        out["pipeline_config"] = capo_appsync.types.pipeline_config.deserialize_json(
            data["pipelineConfig"]
        )
    if data.get("syncConfig") is not None:
        import capo_appsync.types.sync_config

        out["sync_config"] = capo_appsync.types.sync_config.deserialize_json(
            data["syncConfig"]
        )
    if data.get("cachingConfig") is not None:
        import capo_appsync.types.caching_config

        out["caching_config"] = capo_appsync.types.caching_config.deserialize_json(
            data["cachingConfig"]
        )
    if data.get("maxBatchSize") is not None:
        out["max_batch_size"] = data["maxBatchSize"]
    if data.get("runtime") is not None:
        import capo_appsync.types.app_sync_runtime

        out["runtime"] = capo_appsync.types.app_sync_runtime.deserialize_json(
            data["runtime"]
        )
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("metricsConfig") is not None:
        import capo_appsync.types.resolver_level_metrics_config

        out["metrics_config"] = (
            capo_appsync.types.resolver_level_metrics_config.deserialize_json(
                data["metricsConfig"]
            )
        )
    return out
