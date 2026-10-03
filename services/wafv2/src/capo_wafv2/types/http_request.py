"""Generated from Smithy shape ``com.amazonaws.wafv2#HTTPRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.country
    import capo_wafv2.types.http_headers
    import capo_wafv2.types.http_method
    import capo_wafv2.types.http_version
    import capo_wafv2.types.ip_string
    import capo_wafv2.types.uri_string


class HTTPRequest(TypedDict, closed=True):
    client_ip: NotRequired["capo_wafv2.types.ip_string.IPString"]
    """<p>The IP address that the request originated from. If the web ACL is associated with a CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:</p> <ul> <li> <p> <code>c-ip</code>, if the viewer did not use an HTTP proxy or a load balancer to send the request</p> </li> <li> <p> <code>x-forwarded-for</code>, if the viewer did use an HTTP proxy or a load balancer to send the request</p> </li> </ul>"""
    country: NotRequired["capo_wafv2.types.country.Country"]
    """<p>The two-letter country code for the country that the request originated from. For a current list of country codes, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a>.</p>"""
    uri: NotRequired["capo_wafv2.types.uri_string.URIString"]
    """<p>The URI path of the request, which identifies the resource, for example, <code>/images/daily-ad.jpg</code>.</p>"""
    method: NotRequired["capo_wafv2.types.http_method.HTTPMethod"]
    """<p>The HTTP method specified in the sampled web request. </p>"""
    http_version: NotRequired["capo_wafv2.types.http_version.HTTPVersion"]
    """<p>The HTTP version specified in the sampled web request, for example, <code>HTTP/1.1</code>.</p>"""
    headers: NotRequired["capo_wafv2.types.http_headers.HTTPHeaders"]
    """<p>A complex type that contains the name and value for each header in the sampled web request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HTTPRequest) -> dict:
    out: dict = {}
    if "client_ip" in value:
        out["ClientIP"] = value["client_ip"]
    if "country" in value:
        out["Country"] = value["country"]
    if "uri" in value:
        out["URI"] = value["uri"]
    if "method" in value:
        out["Method"] = value["method"]
    if "http_version" in value:
        out["HTTPVersion"] = value["http_version"]
    if "headers" in value:
        import capo_wafv2.types.http_headers

        out["Headers"] = capo_wafv2.types.http_headers.serialize_aws_json_1_1(
            value["headers"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HTTPRequest:
    out: HTTPRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientIP") is not None:
        out["client_ip"] = data["ClientIP"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("URI") is not None:
        out["uri"] = data["URI"]
    if data.get("Method") is not None:
        out["method"] = data["Method"]
    if data.get("HTTPVersion") is not None:
        out["http_version"] = data["HTTPVersion"]
    if data.get("Headers") is not None:
        import capo_wafv2.types.http_headers

        out["headers"] = capo_wafv2.types.http_headers.deserialize_aws_json_1_1(
            data["Headers"]
        )
    return out
