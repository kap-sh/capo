"""Generated from Smithy shape ``com.amazonaws.apigateway#Stage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.access_log_settings
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.cache_cluster_size
    import capo_api_gateway.types.cache_cluster_status
    import capo_api_gateway.types.canary_settings
    import capo_api_gateway.types.map_of_method_settings
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string
    import capo_api_gateway.types.timestamp


class Stage(TypedDict, closed=True):
    deployment_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier of the Deployment that the stage points to.</p>"""
    client_certificate_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier of a client certificate for an API stage.</p>"""
    stage_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The stage's description.</p>"""
    cache_cluster_enabled: "capo_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether a cache cluster is enabled for the stage. To activate a method-level cache, set <code>CachingEnabled</code> to <code>true</code> for a method. </p>"""
    cache_cluster_size: NotRequired[
        "capo_api_gateway.types.cache_cluster_size.CacheClusterSize"
    ]
    """<p>The stage's cache capacity in GB. For more information about choosing a cache size, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html">Enabling API caching to enhance responsiveness</a>.</p>"""
    cache_cluster_status: NotRequired[
        "capo_api_gateway.types.cache_cluster_status.CacheClusterStatus"
    ]
    """<p>The status of the cache cluster for the stage, if enabled.</p>"""
    method_settings: NotRequired[
        "capo_api_gateway.types.map_of_method_settings.MapOfMethodSettings"
    ]
    r"""<p>A map that defines the method settings for a Stage resource. Keys (designated as <code>/{method_setting_key</code> below) are method paths defined as <code>{resource_path}/{http_method}</code> for an individual method override, or <code>/\*/\*</code> for overriding all methods in the stage. </p>"""
    variables: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A map that defines the stage variables for a Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match <code>[A-Za-z0-9-._~:/?#&=,]+</code>.</p>"""
    documentation_version: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The version of the associated API documentation.</p>"""
    access_log_settings: NotRequired[
        "capo_api_gateway.types.access_log_settings.AccessLogSettings"
    ]
    """<p>Settings for logging access in this stage.</p>"""
    canary_settings: NotRequired[
        "capo_api_gateway.types.canary_settings.CanarySettings"
    ]
    """<p>Settings for the canary deployment in this stage.</p>"""
    tracing_enabled: "capo_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether active tracing with X-ray is enabled for the Stage.</p>"""
    web_acl_arn: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The ARN of the WebAcl associated with the Stage.</p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""
    created_date: NotRequired["capo_api_gateway.types.timestamp.Timestamp"]
    """<p>The timestamp when the stage was created.</p>"""
    last_updated_date: NotRequired["capo_api_gateway.types.timestamp.Timestamp"]
    """<p>The timestamp when the stage last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Stage) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "client_certificate_id" in value:
        out["clientCertificateId"] = value["client_certificate_id"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["cacheClusterEnabled"] = value.get("cache_cluster_enabled", False)
    if "cache_cluster_size" in value:
        import capo_api_gateway.types.cache_cluster_size

        out["cacheClusterSize"] = (
            capo_api_gateway.types.cache_cluster_size.serialize_json(
                value["cache_cluster_size"]
            )
        )
    if "cache_cluster_status" in value:
        import capo_api_gateway.types.cache_cluster_status

        out["cacheClusterStatus"] = (
            capo_api_gateway.types.cache_cluster_status.serialize_json(
                value["cache_cluster_status"]
            )
        )
    if "method_settings" in value:
        import capo_api_gateway.types.map_of_method_settings

        out["methodSettings"] = (
            capo_api_gateway.types.map_of_method_settings.serialize_json(
                value["method_settings"]
            )
        )
    if "variables" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["variables"] = (
            capo_api_gateway.types.map_of_string_to_string.serialize_json(
                value["variables"]
            )
        )
    if "documentation_version" in value:
        out["documentationVersion"] = value["documentation_version"]
    if "access_log_settings" in value:
        import capo_api_gateway.types.access_log_settings

        out["accessLogSettings"] = (
            capo_api_gateway.types.access_log_settings.serialize_json(
                value["access_log_settings"]
            )
        )
    if "canary_settings" in value:
        import capo_api_gateway.types.canary_settings

        out["canarySettings"] = capo_api_gateway.types.canary_settings.serialize_json(
            value["canary_settings"]
        )
    out["tracingEnabled"] = value.get("tracing_enabled", False)
    if "web_acl_arn" in value:
        out["webAclArn"] = value["web_acl_arn"]
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    if "created_date" in value:
        import capo_api_gateway.types.timestamp

        out["createdDate"] = capo_api_gateway.types.timestamp.serialize_json(
            value["created_date"]
        )
    if "last_updated_date" in value:
        import capo_api_gateway.types.timestamp

        out["lastUpdatedDate"] = capo_api_gateway.types.timestamp.serialize_json(
            value["last_updated_date"]
        )
    return out


def deserialize_json(data: dict) -> Stage:
    out: Stage = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("clientCertificateId") is not None:
        out["client_certificate_id"] = data["clientCertificateId"]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("cacheClusterEnabled") is not None:
        out["cache_cluster_enabled"] = data["cacheClusterEnabled"]
    else:
        out["cache_cluster_enabled"] = False
    if data.get("cacheClusterSize") is not None:
        import capo_api_gateway.types.cache_cluster_size

        out["cache_cluster_size"] = (
            capo_api_gateway.types.cache_cluster_size.deserialize_json(
                data["cacheClusterSize"]
            )
        )
    if data.get("cacheClusterStatus") is not None:
        import capo_api_gateway.types.cache_cluster_status

        out["cache_cluster_status"] = (
            capo_api_gateway.types.cache_cluster_status.deserialize_json(
                data["cacheClusterStatus"]
            )
        )
    if data.get("methodSettings") is not None:
        import capo_api_gateway.types.map_of_method_settings

        out["method_settings"] = (
            capo_api_gateway.types.map_of_method_settings.deserialize_json(
                data["methodSettings"]
            )
        )
    if data.get("variables") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["variables"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["variables"]
            )
        )
    if data.get("documentationVersion") is not None:
        out["documentation_version"] = data["documentationVersion"]
    if data.get("accessLogSettings") is not None:
        import capo_api_gateway.types.access_log_settings

        out["access_log_settings"] = (
            capo_api_gateway.types.access_log_settings.deserialize_json(
                data["accessLogSettings"]
            )
        )
    if data.get("canarySettings") is not None:
        import capo_api_gateway.types.canary_settings

        out["canary_settings"] = (
            capo_api_gateway.types.canary_settings.deserialize_json(
                data["canarySettings"]
            )
        )
    if data.get("tracingEnabled") is not None:
        out["tracing_enabled"] = data["tracingEnabled"]
    else:
        out["tracing_enabled"] = False
    if data.get("webAclArn") is not None:
        out["web_acl_arn"] = data["webAclArn"]
    if data.get("tags") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    if data.get("createdDate") is not None:
        import capo_api_gateway.types.timestamp

        out["created_date"] = capo_api_gateway.types.timestamp.deserialize_json(
            data["createdDate"]
        )
    if data.get("lastUpdatedDate") is not None:
        import capo_api_gateway.types.timestamp

        out["last_updated_date"] = capo_api_gateway.types.timestamp.deserialize_json(
            data["lastUpdatedDate"]
        )
    return out
