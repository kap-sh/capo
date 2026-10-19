"""Generated from Smithy shape ``com.amazonaws.amplify#CacheConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.cache_config_type


class CacheConfig(TypedDict, closed=True):
    type: "capo_amplify.types.cache_config_type.CacheConfigType"
    """<p>The type of cache configuration to use for an Amplify app.</p> <p>The <code>AMPLIFY_MANAGED</code> cache configuration automatically applies an optimized cache configuration for your app based on its platform, routing rules, and rewrite rules.</p> <p>The <code>AMPLIFY_MANAGED_NO_COOKIES</code> cache configuration type is the same as <code>AMPLIFY_MANAGED</code>, except that it excludes all cookies from the cache key. This is the default setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CacheConfig) -> dict:
    out: dict = {}
    import capo_amplify.types.cache_config_type

    out["type"] = capo_amplify.types.cache_config_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> CacheConfig:
    out: CacheConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_amplify.types.cache_config_type

        out["type"] = capo_amplify.types.cache_config_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_amplify.types.cache_config_type.CacheConfigType", ""
        )
    return out
