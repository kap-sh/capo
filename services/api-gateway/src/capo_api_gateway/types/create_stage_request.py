"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.cache_cluster_size
    import capo_api_gateway.types.canary_settings
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string


class CreateStageRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    stage_name: "capo_api_gateway.types.string.String"
    """<p>The name for the Stage resource. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>"""
    deployment_id: "capo_api_gateway.types.string.String"
    """<p>The identifier of the Deployment resource for the Stage resource.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of the Stage resource.</p>"""
    cache_cluster_enabled: "capo_api_gateway.types.boolean.Boolean"
    """<p>Whether cache clustering is enabled for the stage.</p>"""
    cache_cluster_size: NotRequired[
        "capo_api_gateway.types.cache_cluster_size.CacheClusterSize"
    ]
    """<p>The stage's cache capacity in GB. For more information about choosing a cache size, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html">Enabling API caching to enhance responsiveness</a>.</p>"""
    variables: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A map that defines the stage variables for the new Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match <code>[A-Za-z0-9-._~:/?#&=,]+</code>.</p>"""
    documentation_version: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The version of the associated API documentation.</p>"""
    canary_settings: NotRequired[
        "capo_api_gateway.types.canary_settings.CanarySettings"
    ]
    """<p>The canary deployment settings of this stage.</p>"""
    tracing_enabled: "capo_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether active tracing with X-ray is enabled for the Stage.</p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStageRequest) -> dict:
    out: dict = {}
    out["stageName"] = value["stage_name"]
    out["deploymentId"] = value["deployment_id"]
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
    if "variables" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["variables"] = (
            capo_api_gateway.types.map_of_string_to_string.serialize_json(
                value["variables"]
            )
        )
    if "documentation_version" in value:
        out["documentationVersion"] = value["documentation_version"]
    if "canary_settings" in value:
        import capo_api_gateway.types.canary_settings

        out["canarySettings"] = capo_api_gateway.types.canary_settings.serialize_json(
            value["canary_settings"]
        )
    out["tracingEnabled"] = value.get("tracing_enabled", False)
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateStageRequest:
    out: CreateStageRequest = {}  # type: ignore[typeddict-item]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    else:
        raise DeserializationError("CreateStageRequest.stage_name required")
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("CreateStageRequest.deployment_id required")
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
    if data.get("variables") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["variables"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["variables"]
            )
        )
    if data.get("documentationVersion") is not None:
        out["documentation_version"] = data["documentationVersion"]
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
    if data.get("tags") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    return out
