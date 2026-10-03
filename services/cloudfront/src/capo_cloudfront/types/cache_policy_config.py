"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.long
    import capo_cloudfront.types.parameters_in_cache_key_and_forwarded_to_origin
    import capo_cloudfront.types.string


class CachePolicyConfig(TypedDict, closed=True):
    comment: NotRequired["capo_cloudfront.types.string.string"]
    """<p>A comment to describe the cache policy. The comment cannot be longer than 128 characters.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>A unique name to identify the cache policy.</p>"""
    default_ttl: NotRequired["capo_cloudfront.types.long.long"]
    """<p>The default amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value as the object's time to live (TTL) only when the origin does <i>not</i> send <code>Cache-Control</code> or <code>Expires</code> headers with the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Managing How Long Content Stays in an Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>The default value for this field is 86400 seconds (one day). If the value of <code>MinTTL</code> is more than 86400 seconds, then the default value for this field is the same as the value of <code>MinTTL</code>.</p>"""
    max_ttl: NotRequired["capo_cloudfront.types.long.long"]
    """<p>The maximum amount of time, in seconds, that objects stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value only when the origin sends <code>Cache-Control</code> or <code>Expires</code> headers with the object. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Managing How Long Content Stays in an Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>The default value for this field is 31536000 seconds (one year). If the value of <code>MinTTL</code> or <code>DefaultTTL</code> is more than 31536000 seconds, then the default value for this field is the same as the value of <code>DefaultTTL</code>.</p>"""
    min_ttl: "capo_cloudfront.types.long.long"
    """<p>The minimum amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Managing How Long Content Stays in an Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    parameters_in_cache_key_and_forwarded_to_origin: NotRequired[
        "capo_cloudfront.types.parameters_in_cache_key_and_forwarded_to_origin.ParametersInCacheKeyAndForwardedToOrigin"
    ]
    """<p>The HTTP headers, cookies, and URL query strings to include in the cache key. The values included in the cache key are also included in requests that CloudFront sends to the origin.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CachePolicyConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    SubElement(el, "Name").text = str(value["name"])
    if "default_ttl" in value:
        SubElement(el, "DefaultTTL").text = str(value["default_ttl"])
    if "max_ttl" in value:
        SubElement(el, "MaxTTL").text = str(value["max_ttl"])
    SubElement(el, "MinTTL").text = str(value["min_ttl"])
    if "parameters_in_cache_key_and_forwarded_to_origin" in value:
        import capo_cloudfront.types.parameters_in_cache_key_and_forwarded_to_origin

        capo_cloudfront.types.parameters_in_cache_key_and_forwarded_to_origin.serialize_xml(
            value["parameters_in_cache_key_and_forwarded_to_origin"],
            el,
            "ParametersInCacheKeyAndForwardedToOrigin",
        )


def deserialize_xml(el: Element) -> CachePolicyConfig:
    out: CachePolicyConfig = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CachePolicyConfig.name required")
    child_default_ttl = el.find("DefaultTTL")
    if child_default_ttl is not None:
        out["default_ttl"] = int(child_default_ttl.text or "")
    child_max_ttl = el.find("MaxTTL")
    if child_max_ttl is not None:
        out["max_ttl"] = int(child_max_ttl.text or "")
    child_min_ttl = el.find("MinTTL")
    if child_min_ttl is not None:
        out["min_ttl"] = int(child_min_ttl.text or "")
    else:
        raise DeserializationError("CachePolicyConfig.min_ttl required")
    child_parameters_in_cache_key_and_forwarded_to_origin = el.find(
        "ParametersInCacheKeyAndForwardedToOrigin"
    )
    if child_parameters_in_cache_key_and_forwarded_to_origin is not None:
        import capo_cloudfront.types.parameters_in_cache_key_and_forwarded_to_origin

        out["parameters_in_cache_key_and_forwarded_to_origin"] = (
            capo_cloudfront.types.parameters_in_cache_key_and_forwarded_to_origin.deserialize_xml(
                child_parameters_in_cache_key_and_forwarded_to_origin
            )
        )
    return out
