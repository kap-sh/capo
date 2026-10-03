"""Generated from Smithy shape ``com.amazonaws.cloudfront#ParametersInCacheKeyAndForwardedToOrigin``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.cache_policy_cookies_config
    import capo_cloudfront.types.cache_policy_headers_config
    import capo_cloudfront.types.cache_policy_query_strings_config


class ParametersInCacheKeyAndForwardedToOrigin(TypedDict, closed=True):
    enable_accept_encoding_gzip: "capo_cloudfront.types.boolean.boolean"
    """<p>A flag that can affect whether the <code>Accept-Encoding</code> HTTP header is included in the cache key and included in requests that CloudFront sends to the origin.</p> <p>This field is related to the <code>EnableAcceptEncodingBrotli</code> field. If one or both of these fields is <code>true</code> <i>and</i> the viewer request includes the <code>Accept-Encoding</code> header, then CloudFront does the following:</p> <ul> <li> <p>Normalizes the value of the viewer's <code>Accept-Encoding</code> header</p> </li> <li> <p>Includes the normalized header in the cache key</p> </li> <li> <p>Includes the normalized header in the request to the origin, if a request is necessary</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-policy-compressed-objects">Compression support</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you set this value to <code>true</code>, and this cache behavior also has an origin request policy attached, do not include the <code>Accept-Encoding</code> header in the origin request policy. CloudFront always includes the <code>Accept-Encoding</code> header in origin requests when the value of this field is <code>true</code>, so including this header in an origin request policy has no effect.</p> <p>If both of these fields are <code>false</code>, then CloudFront treats the <code>Accept-Encoding</code> header the same as any other HTTP header in the viewer request. By default, it's not included in the cache key and it's not included in origin requests. In this case, you can manually add <code>Accept-Encoding</code> to the headers whitelist like any other HTTP header.</p>"""
    enable_accept_encoding_brotli: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>A flag that can affect whether the <code>Accept-Encoding</code> HTTP header is included in the cache key and included in requests that CloudFront sends to the origin.</p> <p>This field is related to the <code>EnableAcceptEncodingGzip</code> field. If one or both of these fields is <code>true</code> <i>and</i> the viewer request includes the <code>Accept-Encoding</code> header, then CloudFront does the following:</p> <ul> <li> <p>Normalizes the value of the viewer's <code>Accept-Encoding</code> header</p> </li> <li> <p>Includes the normalized header in the cache key</p> </li> <li> <p>Includes the normalized header in the request to the origin, if a request is necessary</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-policy-compressed-objects">Compression support</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you set this value to <code>true</code>, and this cache behavior also has an origin request policy attached, do not include the <code>Accept-Encoding</code> header in the origin request policy. CloudFront always includes the <code>Accept-Encoding</code> header in origin requests when the value of this field is <code>true</code>, so including this header in an origin request policy has no effect.</p> <p>If both of these fields are <code>false</code>, then CloudFront treats the <code>Accept-Encoding</code> header the same as any other HTTP header in the viewer request. By default, it's not included in the cache key and it's not included in origin requests. In this case, you can manually add <code>Accept-Encoding</code> to the headers whitelist like any other HTTP header.</p>"""
    headers_config: (
        "capo_cloudfront.types.cache_policy_headers_config.CachePolicyHeadersConfig"
    )
    """<p>An object that determines whether any HTTP headers (and if so, which headers) are included in the cache key and in requests that CloudFront sends to the origin.</p>"""
    cookies_config: (
        "capo_cloudfront.types.cache_policy_cookies_config.CachePolicyCookiesConfig"
    )
    """<p>An object that determines whether any cookies in viewer requests (and if so, which cookies) are included in the cache key and in requests that CloudFront sends to the origin.</p>"""
    query_strings_config: "capo_cloudfront.types.cache_policy_query_strings_config.CachePolicyQueryStringsConfig"
    """<p>An object that determines whether any URL query strings in viewer requests (and if so, which query strings) are included in the cache key and in requests that CloudFront sends to the origin.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ParametersInCacheKeyAndForwardedToOrigin, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "EnableAcceptEncodingGzip").text = (
        "true" if value["enable_accept_encoding_gzip"] else "false"
    )
    if "enable_accept_encoding_brotli" in value:
        SubElement(el, "EnableAcceptEncodingBrotli").text = (
            "true" if value["enable_accept_encoding_brotli"] else "false"
        )
    import capo_cloudfront.types.cache_policy_headers_config

    capo_cloudfront.types.cache_policy_headers_config.serialize_xml(
        value["headers_config"], el, "HeadersConfig"
    )
    import capo_cloudfront.types.cache_policy_cookies_config

    capo_cloudfront.types.cache_policy_cookies_config.serialize_xml(
        value["cookies_config"], el, "CookiesConfig"
    )
    import capo_cloudfront.types.cache_policy_query_strings_config

    capo_cloudfront.types.cache_policy_query_strings_config.serialize_xml(
        value["query_strings_config"], el, "QueryStringsConfig"
    )


def deserialize_xml(el: Element) -> ParametersInCacheKeyAndForwardedToOrigin:
    out: ParametersInCacheKeyAndForwardedToOrigin = {}  # type: ignore[typeddict-item]
    child_enable_accept_encoding_gzip = el.find("EnableAcceptEncodingGzip")
    if child_enable_accept_encoding_gzip is not None:
        out["enable_accept_encoding_gzip"] = (
            child_enable_accept_encoding_gzip.text or ""
        ).lower() == "true"
    else:
        raise DeserializationError(
            "ParametersInCacheKeyAndForwardedToOrigin.enable_accept_encoding_gzip required"
        )
    child_enable_accept_encoding_brotli = el.find("EnableAcceptEncodingBrotli")
    if child_enable_accept_encoding_brotli is not None:
        out["enable_accept_encoding_brotli"] = (
            child_enable_accept_encoding_brotli.text or ""
        ).lower() == "true"
    child_headers_config = el.find("HeadersConfig")
    if child_headers_config is not None:
        import capo_cloudfront.types.cache_policy_headers_config

        out["headers_config"] = (
            capo_cloudfront.types.cache_policy_headers_config.deserialize_xml(
                child_headers_config
            )
        )
    else:
        raise DeserializationError(
            "ParametersInCacheKeyAndForwardedToOrigin.headers_config required"
        )
    child_cookies_config = el.find("CookiesConfig")
    if child_cookies_config is not None:
        import capo_cloudfront.types.cache_policy_cookies_config

        out["cookies_config"] = (
            capo_cloudfront.types.cache_policy_cookies_config.deserialize_xml(
                child_cookies_config
            )
        )
    else:
        raise DeserializationError(
            "ParametersInCacheKeyAndForwardedToOrigin.cookies_config required"
        )
    child_query_strings_config = el.find("QueryStringsConfig")
    if child_query_strings_config is not None:
        import capo_cloudfront.types.cache_policy_query_strings_config

        out["query_strings_config"] = (
            capo_cloudfront.types.cache_policy_query_strings_config.deserialize_xml(
                child_query_strings_config
            )
        )
    else:
        raise DeserializationError(
            "ParametersInCacheKeyAndForwardedToOrigin.query_strings_config required"
        )
    return out
