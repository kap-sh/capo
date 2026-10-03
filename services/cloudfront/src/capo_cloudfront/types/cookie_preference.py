"""Generated from Smithy shape ``com.amazonaws.cloudfront#CookiePreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.cookie_names
    import capo_cloudfront.types.item_selection


class CookiePreference(TypedDict, closed=True):
    forward: "capo_cloudfront.types.item_selection.ItemSelection"
    """<p>This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.</p> <p>If you want to include cookies in the cache key, use a cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you want to send cookies to the origin but not include them in the cache key, use origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy">Creating origin request policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the <code>WhitelistedNames</code> complex type.</p> <p>Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the <code>Forward</code> element.</p>"""
    whitelisted_names: NotRequired["capo_cloudfront.types.cookie_names.CookieNames"]
    """<p>This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.</p> <p>If you want to include cookies in the cache key, use a cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you want to send cookies to the origin but not include them in the cache key, use an origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy">Creating origin request policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>Required if you specify <code>whitelist</code> for the value of <code>Forward</code>. A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.</p> <p>If you specify <code>all</code> or <code>none</code> for the value of <code>Forward</code>, omit <code>WhitelistedNames</code>. If you change the value of <code>Forward</code> from <code>whitelist</code> to <code>all</code> or <code>none</code> and you don't delete the <code>WhitelistedNames</code> element and its child elements, CloudFront deletes them automatically.</p> <p>For the current limit on the number of cookie names that you can whitelist for each cache behavior, see <a href="https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront"> CloudFront Limits</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CookiePreference, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.item_selection

    capo_cloudfront.types.item_selection.serialize_xml(value["forward"], el, "Forward")
    if "whitelisted_names" in value:
        import capo_cloudfront.types.cookie_names

        capo_cloudfront.types.cookie_names.serialize_xml(
            value["whitelisted_names"], el, "WhitelistedNames"
        )


def deserialize_xml(el: Element) -> CookiePreference:
    out: CookiePreference = {}  # type: ignore[typeddict-item]
    child_forward = el.find("Forward")
    if child_forward is not None:
        import capo_cloudfront.types.item_selection

        out["forward"] = capo_cloudfront.types.item_selection.deserialize_xml(
            child_forward
        )
    else:
        raise DeserializationError("CookiePreference.forward required")
    child_whitelisted_names = el.find("WhitelistedNames")
    if child_whitelisted_names is not None:
        import capo_cloudfront.types.cookie_names

        out["whitelisted_names"] = capo_cloudfront.types.cookie_names.deserialize_xml(
            child_whitelisted_names
        )
    return out
