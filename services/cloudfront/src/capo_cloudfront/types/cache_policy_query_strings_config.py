"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicyQueryStringsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cache_policy_query_string_behavior
    import capo_cloudfront.types.query_string_names


class CachePolicyQueryStringsConfig(TypedDict, closed=True):
    query_string_behavior: "capo_cloudfront.types.cache_policy_query_string_behavior.CachePolicyQueryStringBehavior"
    """<p>Determines whether any URL query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:</p> <ul> <li> <p> <code>none</code> – No query strings in viewer requests are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to <code>none</code>, any query strings that are listed in an <code>OriginRequestPolicy</code> <i>are</i> included in origin requests.</p> </li> <li> <p> <code>whitelist</code> – Only the query strings in viewer requests that are listed in the <code>QueryStringNames</code> type are included in the cache key and in requests that CloudFront sends to the origin.</p> </li> <li> <p> <code>allExcept</code> – All query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin, <i> <b>except</b> </i> those that are listed in the <code>QueryStringNames</code> type, which are not included.</p> </li> <li> <p> <code>all</code> – All query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin.</p> </li> </ul>"""
    query_strings: NotRequired[
        "capo_cloudfront.types.query_string_names.QueryStringNames"
    ]
    """<p>Contains the specific query strings in viewer requests that either <i> <b>are</b> </i> or <i> <b>are not</b> </i> included in the cache key and in requests that CloudFront sends to the origin. The behavior depends on whether the <code>QueryStringBehavior</code> field in the <code>CachePolicyQueryStringsConfig</code> type is set to <code>whitelist</code> (the listed query strings <i> <b>are</b> </i> included) or <code>allExcept</code> (the listed query strings <i> <b>are not</b> </i> included, but all other query strings are).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CachePolicyQueryStringsConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.cache_policy_query_string_behavior

    capo_cloudfront.types.cache_policy_query_string_behavior.serialize_xml(
        value["query_string_behavior"], el, "QueryStringBehavior"
    )
    if "query_strings" in value:
        import capo_cloudfront.types.query_string_names

        capo_cloudfront.types.query_string_names.serialize_xml(
            value["query_strings"], el, "QueryStrings"
        )


def deserialize_xml(el: Element) -> CachePolicyQueryStringsConfig:
    out: CachePolicyQueryStringsConfig = {}  # type: ignore[typeddict-item]
    child_query_string_behavior = el.find("QueryStringBehavior")
    if child_query_string_behavior is not None:
        import capo_cloudfront.types.cache_policy_query_string_behavior

        out["query_string_behavior"] = (
            capo_cloudfront.types.cache_policy_query_string_behavior.deserialize_xml(
                child_query_string_behavior
            )
        )
    else:
        import typing

        out["query_string_behavior"] = typing.cast(
            "capo_cloudfront.types.cache_policy_query_string_behavior.CachePolicyQueryStringBehavior",
            "",
        )
    child_query_strings = el.find("QueryStrings")
    if child_query_strings is not None:
        import capo_cloudfront.types.query_string_names

        out["query_strings"] = capo_cloudfront.types.query_string_names.deserialize_xml(
            child_query_strings
        )
    return out
