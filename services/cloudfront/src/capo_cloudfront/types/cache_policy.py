"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.cache_policy_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class CachePolicy(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The unique identifier for the cache policy.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the cache policy was last modified.</p>"""
    cache_policy_config: "capo_cloudfront.types.cache_policy_config.CachePolicyConfig"
    """<p>The cache policy configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CachePolicy, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    import capo_cloudfront.types.cache_policy_config

    capo_cloudfront.types.cache_policy_config.serialize_xml(
        value["cache_policy_config"], el, "CachePolicyConfig"
    )


def deserialize_xml(el: Element) -> CachePolicy:
    out: CachePolicy = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_cache_policy_config = el.find("CachePolicyConfig")
    if child_cache_policy_config is not None:
        import capo_cloudfront.types.cache_policy_config

        out["cache_policy_config"] = (
            capo_cloudfront.types.cache_policy_config.deserialize_xml(
                child_cache_policy_config
            )
        )
    else:
        raise DeserializationError("CachePolicy.cache_policy_config required")
    return out
