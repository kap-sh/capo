"""Generated from Smithy shape ``com.amazonaws.appsync#CreateApiCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.api_cache_type
    import capo_appsync.types.api_caching_behavior
    import capo_appsync.types.boolean
    import capo_appsync.types.cache_health_metrics_config
    import capo_appsync.types.long
    import capo_appsync.types.string


class CreateApiCacheRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The GraphQL API ID.</p>"""
    ttl: "capo_appsync.types.long.Long"
    """<p>TTL in seconds for cache entries.</p> <p>Valid values are 1–3,600 seconds.</p>"""
    transit_encryption_enabled: NotRequired["capo_appsync.types.boolean.Boolean"]
    """<p>Transit encryption flag when connecting to cache. You cannot update this setting after creation.</p>"""
    at_rest_encryption_enabled: NotRequired["capo_appsync.types.boolean.Boolean"]
    """<p>At-rest encryption flag for cache. You cannot update this setting after creation.</p>"""
    api_caching_behavior: "capo_appsync.types.api_caching_behavior.ApiCachingBehavior"
    """<p>Caching behavior.</p> <ul> <li> <p> <b>FULL_REQUEST_CACHING</b>: All requests from the same user are cached. Individual resolvers are automatically cached. All API calls will try to return responses from the cache.</p> </li> <li> <p> <b>PER_RESOLVER_CACHING</b>: Individual resolvers that you specify are cached.</p> </li> <li> <p> <b>OPERATION_LEVEL_CACHING</b>: Full requests are cached together and returned without executing resolvers.</p> </li> </ul>"""
    type: "capo_appsync.types.api_cache_type.ApiCacheType"
    """<p>The cache instance type. Valid values are </p> <ul> <li> <p> <code>SMALL</code> </p> </li> <li> <p> <code>MEDIUM</code> </p> </li> <li> <p> <code>LARGE</code> </p> </li> <li> <p> <code>XLARGE</code> </p> </li> <li> <p> <code>LARGE_2X</code> </p> </li> <li> <p> <code>LARGE_4X</code> </p> </li> <li> <p> <code>LARGE_8X</code> (not available in all regions)</p> </li> <li> <p> <code>LARGE_12X</code> </p> </li> </ul> <p>Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.</p> <p>The following legacy instance types are available, but their use is discouraged:</p> <ul> <li> <p> <b>T2_SMALL</b>: A t2.small instance type.</p> </li> <li> <p> <b>T2_MEDIUM</b>: A t2.medium instance type.</p> </li> <li> <p> <b>R4_LARGE</b>: A r4.large instance type.</p> </li> <li> <p> <b>R4_XLARGE</b>: A r4.xlarge instance type.</p> </li> <li> <p> <b>R4_2XLARGE</b>: A r4.2xlarge instance type.</p> </li> <li> <p> <b>R4_4XLARGE</b>: A r4.4xlarge instance type.</p> </li> <li> <p> <b>R4_8XLARGE</b>: A r4.8xlarge instance type.</p> </li> </ul>"""
    health_metrics_config: NotRequired[
        "capo_appsync.types.cache_health_metrics_config.CacheHealthMetricsConfig"
    ]
    """<p>Controls how cache health metrics will be emitted to CloudWatch. Cache health metrics include:</p> <ul> <li> <p>NetworkBandwidthOutAllowanceExceeded: The network packets dropped because the throughput exceeded the aggregated bandwidth limit. This is useful for diagnosing bottlenecks in a cache configuration.</p> </li> <li> <p>EngineCPUUtilization: The CPU utilization (percentage) allocated to the Redis process. This is useful for diagnosing bottlenecks in a cache configuration.</p> </li> </ul> <p>Metrics will be recorded by API ID. You can set the value to <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiCacheRequest) -> dict:
    out: dict = {}
    out["ttl"] = value["ttl"]
    if "transit_encryption_enabled" in value:
        out["transitEncryptionEnabled"] = value["transit_encryption_enabled"]
    if "at_rest_encryption_enabled" in value:
        out["atRestEncryptionEnabled"] = value["at_rest_encryption_enabled"]
    import capo_appsync.types.api_caching_behavior

    out["apiCachingBehavior"] = capo_appsync.types.api_caching_behavior.serialize_json(
        value["api_caching_behavior"]
    )
    import capo_appsync.types.api_cache_type

    out["type"] = capo_appsync.types.api_cache_type.serialize_json(value["type"])
    if "health_metrics_config" in value:
        import capo_appsync.types.cache_health_metrics_config

        out["healthMetricsConfig"] = (
            capo_appsync.types.cache_health_metrics_config.serialize_json(
                value["health_metrics_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateApiCacheRequest:
    out: CreateApiCacheRequest = {}  # type: ignore[typeddict-item]
    if data.get("ttl") is not None:
        out["ttl"] = data["ttl"]
    else:
        raise DeserializationError("CreateApiCacheRequest.ttl required")
    if data.get("transitEncryptionEnabled") is not None:
        out["transit_encryption_enabled"] = data["transitEncryptionEnabled"]
    if data.get("atRestEncryptionEnabled") is not None:
        out["at_rest_encryption_enabled"] = data["atRestEncryptionEnabled"]
    if data.get("apiCachingBehavior") is not None:
        import capo_appsync.types.api_caching_behavior

        out["api_caching_behavior"] = (
            capo_appsync.types.api_caching_behavior.deserialize_json(
                data["apiCachingBehavior"]
            )
        )
    else:
        raise DeserializationError(
            "CreateApiCacheRequest.api_caching_behavior required"
        )
    if data.get("type") is not None:
        import capo_appsync.types.api_cache_type

        out["type"] = capo_appsync.types.api_cache_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("CreateApiCacheRequest.type required")
    if data.get("healthMetricsConfig") is not None:
        import capo_appsync.types.cache_health_metrics_config

        out["health_metrics_config"] = (
            capo_appsync.types.cache_health_metrics_config.deserialize_json(
                data["healthMetricsConfig"]
            )
        )
    return out
