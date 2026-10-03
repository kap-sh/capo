"""Generated from Smithy shape ``com.amazonaws.cloudfront#CustomErrorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.long
    import capo_cloudfront.types.string


class CustomErrorResponse(TypedDict, closed=True):
    error_code: "capo_cloudfront.types.integer.integer"
    """<p>The HTTP status code for which you want to specify a custom error page and/or a caching duration.</p>"""
    response_page_path: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by <code>ErrorCode</code>, for example, <code>/4xx-errors/403-forbidden.html</code>. If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:</p> <ul> <li> <p>The value of <code>PathPattern</code> matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named <code>/4xx-errors</code>. Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, <code>/4xx-errors/*</code>.</p> </li> <li> <p>The value of <code>TargetOriginId</code> specifies the value of the <code>ID</code> element for the origin that contains your custom error pages.</p> </li> </ul> <p>If you specify a value for <code>ResponsePagePath</code>, you must also specify a value for <code>ResponseCode</code>.</p> <p>We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can't get the files that you want to return to viewers because the origin server is unavailable.</p>"""
    response_code: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:</p> <ul> <li> <p>Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute <code>200</code>, the response typically won't be intercepted.</p> </li> <li> <p>If you don't care about distinguishing among different client errors or server errors, you can specify <code>400</code> or <code>500</code> as the <code>ResponseCode</code> for all 4xx or 5xx errors.</p> </li> <li> <p>You might want to return a <code>200</code> status code (OK) and static website so your customers don't know that your website is down.</p> </li> </ul> <p>If you specify a value for <code>ResponseCode</code>, you must also specify a value for <code>ResponsePagePath</code>.</p>"""
    error_caching_min_ttl: NotRequired["capo_cloudfront.types.long.long"]
    """<p>The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in <code>ErrorCode</code>. When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html">Customizing Error Responses</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CustomErrorResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ErrorCode").text = str(value["error_code"])
    if "response_page_path" in value:
        SubElement(el, "ResponsePagePath").text = str(value["response_page_path"])
    if "response_code" in value:
        SubElement(el, "ResponseCode").text = str(value["response_code"])
    if "error_caching_min_ttl" in value:
        SubElement(el, "ErrorCachingMinTTL").text = str(value["error_caching_min_ttl"])


def deserialize_xml(el: Element) -> CustomErrorResponse:
    out: CustomErrorResponse = {}  # type: ignore[typeddict-item]
    child_error_code = el.find("ErrorCode")
    if child_error_code is not None:
        out["error_code"] = int(child_error_code.text or "")
    else:
        raise DeserializationError("CustomErrorResponse.error_code required")
    child_response_page_path = el.find("ResponsePagePath")
    if child_response_page_path is not None:
        out["response_page_path"] = str(child_response_page_path.text or "")
    child_response_code = el.find("ResponseCode")
    if child_response_code is not None:
        out["response_code"] = str(child_response_code.text or "")
    child_error_caching_min_ttl = el.find("ErrorCachingMinTTL")
    if child_error_caching_min_ttl is not None:
        out["error_caching_min_ttl"] = int(child_error_caching_min_ttl.text or "")
    return out
