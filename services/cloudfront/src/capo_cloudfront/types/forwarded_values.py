"""Generated from Smithy shape ``com.amazonaws.cloudfront#ForwardedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.cookie_preference
    import capo_cloudfront.types.headers
    import capo_cloudfront.types.query_string_cache_keys


class ForwardedValues(TypedDict, closed=True):
    query_string: "capo_cloudfront.types.boolean.boolean"
    """<p>This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.</p> <p>If you want to include query strings in the cache key, use a cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you want to send query strings to the origin but not include them in the cache key, use an origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy">Creating origin request policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of <code>QueryString</code> and on the values that you specify for <code>QueryStringCacheKeys</code>, if any:</p> <p>If you specify true for <code>QueryString</code> and you don't specify any values for <code>QueryStringCacheKeys</code>, CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.</p> <p>If you specify true for <code>QueryString</code> and you specify one or more values for <code>QueryStringCacheKeys</code>, CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.</p> <p>If you specify false for <code>QueryString</code>, CloudFront doesn't forward any query string parameters to the origin, and doesn't cache based on query string parameters.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html">Configuring CloudFront to Cache Based on Query String Parameters</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    cookies: "capo_cloudfront.types.cookie_preference.CookiePreference"
    """<p>This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.</p> <p>If you want to include cookies in the cache key, use a cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you want to send cookies to the origin but not include them in the cache key, use an origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy">Creating origin request policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html">How CloudFront Forwards, Caches, and Logs Cookies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    headers: NotRequired["capo_cloudfront.types.headers.Headers"]
    """<p>This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.</p> <p>If you want to include headers in the cache key, use a cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you want to send headers to the origin but not include them in the cache key, use an origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy">Creating origin request policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>A complex type that specifies the <code>Headers</code>, if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html"> Caching Content Based on Request Headers</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    query_string_cache_keys: NotRequired[
        "capo_cloudfront.types.query_string_cache_keys.QueryStringCacheKeys"
    ]
    """<p>This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.</p> <p>If you want to include query strings in the cache key, use a cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you want to send query strings to the origin but not include them in the cache key, use an origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy">Creating origin request policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ForwardedValues, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "QueryString").text = "true" if value["query_string"] else "false"
    import capo_cloudfront.types.cookie_preference

    capo_cloudfront.types.cookie_preference.serialize_xml(
        value["cookies"], el, "Cookies"
    )
    if "headers" in value:
        import capo_cloudfront.types.headers

        capo_cloudfront.types.headers.serialize_xml(value["headers"], el, "Headers")
    if "query_string_cache_keys" in value:
        import capo_cloudfront.types.query_string_cache_keys

        capo_cloudfront.types.query_string_cache_keys.serialize_xml(
            value["query_string_cache_keys"], el, "QueryStringCacheKeys"
        )


def deserialize_xml(el: Element) -> ForwardedValues:
    out: ForwardedValues = {}  # type: ignore[typeddict-item]
    child_query_string = el.find("QueryString")
    if child_query_string is not None:
        out["query_string"] = (child_query_string.text or "").lower() == "true"
    else:
        raise DeserializationError("ForwardedValues.query_string required")
    child_cookies = el.find("Cookies")
    if child_cookies is not None:
        import capo_cloudfront.types.cookie_preference

        out["cookies"] = capo_cloudfront.types.cookie_preference.deserialize_xml(
            child_cookies
        )
    else:
        raise DeserializationError("ForwardedValues.cookies required")
    child_headers = el.find("Headers")
    if child_headers is not None:
        import capo_cloudfront.types.headers

        out["headers"] = capo_cloudfront.types.headers.deserialize_xml(child_headers)
    child_query_string_cache_keys = el.find("QueryStringCacheKeys")
    if child_query_string_cache_keys is not None:
        import capo_cloudfront.types.query_string_cache_keys

        out["query_string_cache_keys"] = (
            capo_cloudfront.types.query_string_cache_keys.deserialize_xml(
                child_query_string_cache_keys
            )
        )
    return out
