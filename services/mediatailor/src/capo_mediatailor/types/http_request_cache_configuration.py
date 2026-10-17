"""Generated from Smithy shape ``com.amazonaws.mediatailor#HttpRequestCacheConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer_min1
    import capo_mediatailor.types.__string


class HttpRequestCacheConfiguration(TypedDict, closed=True):
    ttl_minimum_seconds: "capo_mediatailor.types.__integer_min1.__integerMin1"
    """<p>The lower bound, in seconds, on how long MediaTailor caches a response. MediaTailor also uses this value as the cache duration when a response has no <code>Cache-Control</code> <code>max-age</code> directive.</p>"""
    ttl_maximum_seconds: "capo_mediatailor.types.__integer_min1.__integerMin1"
    """<p>The upper bound, in seconds, on how long MediaTailor caches a response. This value must be greater than or equal to <code>TtlMinimumSeconds</code>.</p>"""
    key: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>A JSONata expression that MediaTailor evaluates to a custom cache key. By default, the cache key is a hash of the HTTP URL, the request body, and the HTTP method; request headers are not included. You can specify a custom cache key expression to vary caching by request headers and more. The evaluated key must be smaller than 1 KB; otherwise the HTTP function will fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpRequestCacheConfiguration) -> dict:
    out: dict = {}
    out["TtlMinimumSeconds"] = value["ttl_minimum_seconds"]
    out["TtlMaximumSeconds"] = value["ttl_maximum_seconds"]
    if "key" in value:
        out["Key"] = value["key"]
    return out


def deserialize_json(data: dict) -> HttpRequestCacheConfiguration:
    out: HttpRequestCacheConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TtlMinimumSeconds") is not None:
        out["ttl_minimum_seconds"] = data["TtlMinimumSeconds"]
    else:
        raise DeserializationError(
            "HttpRequestCacheConfiguration.ttl_minimum_seconds required"
        )
    if data.get("TtlMaximumSeconds") is not None:
        out["ttl_maximum_seconds"] = data["TtlMaximumSeconds"]
    else:
        raise DeserializationError(
            "HttpRequestCacheConfiguration.ttl_maximum_seconds required"
        )
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    return out
