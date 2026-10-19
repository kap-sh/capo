"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.cache_policy
    import capo_cloudfront.types.cache_policy_type


class CachePolicySummary(TypedDict, closed=True):
    type: "capo_cloudfront.types.cache_policy_type.CachePolicyType"
    """<p>The type of cache policy, either <code>managed</code> (created by Amazon Web Services) or <code>custom</code> (created in this Amazon Web Services account).</p>"""
    cache_policy: "capo_cloudfront.types.cache_policy.CachePolicy"
    """<p>The cache policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CachePolicySummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.cache_policy_type

    capo_cloudfront.types.cache_policy_type.serialize_xml(value["type"], el, "Type")
    import capo_cloudfront.types.cache_policy

    capo_cloudfront.types.cache_policy.serialize_xml(
        value["cache_policy"], el, "CachePolicy"
    )


def deserialize_xml(el: Element) -> CachePolicySummary:
    out: CachePolicySummary = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudfront.types.cache_policy_type

        out["type"] = capo_cloudfront.types.cache_policy_type.deserialize_xml(
            child_type
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cloudfront.types.cache_policy_type.CachePolicyType", ""
        )
    child_cache_policy = el.find("CachePolicy")
    if child_cache_policy is not None:
        import capo_cloudfront.types.cache_policy

        out["cache_policy"] = capo_cloudfront.types.cache_policy.deserialize_xml(
            child_cache_policy
        )
    else:
        raise DeserializationError("CachePolicySummary.cache_policy required")
    return out
