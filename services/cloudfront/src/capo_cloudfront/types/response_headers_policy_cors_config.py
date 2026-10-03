"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyCorsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.response_headers_policy_access_control_allow_headers
    import capo_cloudfront.types.response_headers_policy_access_control_allow_methods
    import capo_cloudfront.types.response_headers_policy_access_control_allow_origins
    import capo_cloudfront.types.response_headers_policy_access_control_expose_headers


class ResponseHeadersPolicyCorsConfig(TypedDict, closed=True):
    access_control_allow_origins: "capo_cloudfront.types.response_headers_policy_access_control_allow_origins.ResponseHeadersPolicyAccessControlAllowOrigins"
    """<p>A list of origins (domain names) that CloudFront can use as the value for the <code>Access-Control-Allow-Origin</code> HTTP response header.</p> <p>For more information about the <code>Access-Control-Allow-Origin</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin">Access-Control-Allow-Origin</a> in the MDN Web Docs.</p>"""
    access_control_allow_headers: "capo_cloudfront.types.response_headers_policy_access_control_allow_headers.ResponseHeadersPolicyAccessControlAllowHeaders"
    """<p>A list of HTTP header names that CloudFront includes as values for the <code>Access-Control-Allow-Headers</code> HTTP response header.</p> <p>For more information about the <code>Access-Control-Allow-Headers</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers">Access-Control-Allow-Headers</a> in the MDN Web Docs.</p>"""
    access_control_allow_methods: "capo_cloudfront.types.response_headers_policy_access_control_allow_methods.ResponseHeadersPolicyAccessControlAllowMethods"
    """<p>A list of HTTP methods that CloudFront includes as values for the <code>Access-Control-Allow-Methods</code> HTTP response header.</p> <p>For more information about the <code>Access-Control-Allow-Methods</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods">Access-Control-Allow-Methods</a> in the MDN Web Docs.</p>"""
    access_control_allow_credentials: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that CloudFront uses as the value for the <code>Access-Control-Allow-Credentials</code> HTTP response header.</p> <p>For more information about the <code>Access-Control-Allow-Credentials</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials">Access-Control-Allow-Credentials</a> in the MDN Web Docs.</p>"""
    access_control_expose_headers: NotRequired[
        "capo_cloudfront.types.response_headers_policy_access_control_expose_headers.ResponseHeadersPolicyAccessControlExposeHeaders"
    ]
    """<p>A list of HTTP headers that CloudFront includes as values for the <code>Access-Control-Expose-Headers</code> HTTP response header.</p> <p>For more information about the <code>Access-Control-Expose-Headers</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers">Access-Control-Expose-Headers</a> in the MDN Web Docs.</p>"""
    access_control_max_age_sec: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>A number that CloudFront uses as the value for the <code>Access-Control-Max-Age</code> HTTP response header.</p> <p>For more information about the <code>Access-Control-Max-Age</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age">Access-Control-Max-Age</a> in the MDN Web Docs.</p>"""
    origin_override: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront overrides HTTP response headers received from the origin with the ones specified in this response headers policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyCorsConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.response_headers_policy_access_control_allow_origins

    capo_cloudfront.types.response_headers_policy_access_control_allow_origins.serialize_xml(
        value["access_control_allow_origins"], el, "AccessControlAllowOrigins"
    )
    import capo_cloudfront.types.response_headers_policy_access_control_allow_headers

    capo_cloudfront.types.response_headers_policy_access_control_allow_headers.serialize_xml(
        value["access_control_allow_headers"], el, "AccessControlAllowHeaders"
    )
    import capo_cloudfront.types.response_headers_policy_access_control_allow_methods

    capo_cloudfront.types.response_headers_policy_access_control_allow_methods.serialize_xml(
        value["access_control_allow_methods"], el, "AccessControlAllowMethods"
    )
    SubElement(el, "AccessControlAllowCredentials").text = (
        "true" if value["access_control_allow_credentials"] else "false"
    )
    if "access_control_expose_headers" in value:
        import capo_cloudfront.types.response_headers_policy_access_control_expose_headers

        capo_cloudfront.types.response_headers_policy_access_control_expose_headers.serialize_xml(
            value["access_control_expose_headers"], el, "AccessControlExposeHeaders"
        )
    if "access_control_max_age_sec" in value:
        SubElement(el, "AccessControlMaxAgeSec").text = str(
            value["access_control_max_age_sec"]
        )
    SubElement(el, "OriginOverride").text = (
        "true" if value["origin_override"] else "false"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyCorsConfig:
    out: ResponseHeadersPolicyCorsConfig = {}  # type: ignore[typeddict-item]
    child_access_control_allow_origins = el.find("AccessControlAllowOrigins")
    if child_access_control_allow_origins is not None:
        import capo_cloudfront.types.response_headers_policy_access_control_allow_origins

        out["access_control_allow_origins"] = (
            capo_cloudfront.types.response_headers_policy_access_control_allow_origins.deserialize_xml(
                child_access_control_allow_origins
            )
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyCorsConfig.access_control_allow_origins required"
        )
    child_access_control_allow_headers = el.find("AccessControlAllowHeaders")
    if child_access_control_allow_headers is not None:
        import capo_cloudfront.types.response_headers_policy_access_control_allow_headers

        out["access_control_allow_headers"] = (
            capo_cloudfront.types.response_headers_policy_access_control_allow_headers.deserialize_xml(
                child_access_control_allow_headers
            )
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyCorsConfig.access_control_allow_headers required"
        )
    child_access_control_allow_methods = el.find("AccessControlAllowMethods")
    if child_access_control_allow_methods is not None:
        import capo_cloudfront.types.response_headers_policy_access_control_allow_methods

        out["access_control_allow_methods"] = (
            capo_cloudfront.types.response_headers_policy_access_control_allow_methods.deserialize_xml(
                child_access_control_allow_methods
            )
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyCorsConfig.access_control_allow_methods required"
        )
    child_access_control_allow_credentials = el.find("AccessControlAllowCredentials")
    if child_access_control_allow_credentials is not None:
        out["access_control_allow_credentials"] = (
            child_access_control_allow_credentials.text or ""
        ).lower() == "true"
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyCorsConfig.access_control_allow_credentials required"
        )
    child_access_control_expose_headers = el.find("AccessControlExposeHeaders")
    if child_access_control_expose_headers is not None:
        import capo_cloudfront.types.response_headers_policy_access_control_expose_headers

        out["access_control_expose_headers"] = (
            capo_cloudfront.types.response_headers_policy_access_control_expose_headers.deserialize_xml(
                child_access_control_expose_headers
            )
        )
    child_access_control_max_age_sec = el.find("AccessControlMaxAgeSec")
    if child_access_control_max_age_sec is not None:
        out["access_control_max_age_sec"] = int(
            child_access_control_max_age_sec.text or ""
        )
    child_origin_override = el.find("OriginOverride")
    if child_origin_override is not None:
        out["origin_override"] = (child_origin_override.text or "").lower() == "true"
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyCorsConfig.origin_override required"
        )
    return out
