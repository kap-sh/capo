"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicySecurityHeadersConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.response_headers_policy_content_security_policy
    import capo_cloudfront.types.response_headers_policy_content_type_options
    import capo_cloudfront.types.response_headers_policy_frame_options
    import capo_cloudfront.types.response_headers_policy_referrer_policy
    import capo_cloudfront.types.response_headers_policy_strict_transport_security
    import capo_cloudfront.types.response_headers_policy_xss_protection


class ResponseHeadersPolicySecurityHeadersConfig(TypedDict, closed=True):
    xss_protection: NotRequired[
        "capo_cloudfront.types.response_headers_policy_xss_protection.ResponseHeadersPolicyXSSProtection"
    ]
    """<p>Determines whether CloudFront includes the <code>X-XSS-Protection</code> HTTP response header and the header's value.</p> <p>For more information about the <code>X-XSS-Protection</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection">X-XSS-Protection</a> in the MDN Web Docs.</p>"""
    frame_options: NotRequired[
        "capo_cloudfront.types.response_headers_policy_frame_options.ResponseHeadersPolicyFrameOptions"
    ]
    """<p>Determines whether CloudFront includes the <code>X-Frame-Options</code> HTTP response header and the header's value.</p> <p>For more information about the <code>X-Frame-Options</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options">X-Frame-Options</a> in the MDN Web Docs.</p>"""
    referrer_policy: NotRequired[
        "capo_cloudfront.types.response_headers_policy_referrer_policy.ResponseHeadersPolicyReferrerPolicy"
    ]
    """<p>Determines whether CloudFront includes the <code>Referrer-Policy</code> HTTP response header and the header's value.</p> <p>For more information about the <code>Referrer-Policy</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy">Referrer-Policy</a> in the MDN Web Docs.</p>"""
    content_security_policy: NotRequired[
        "capo_cloudfront.types.response_headers_policy_content_security_policy.ResponseHeadersPolicyContentSecurityPolicy"
    ]
    """<p>The policy directives and their values that CloudFront includes as values for the <code>Content-Security-Policy</code> HTTP response header.</p> <p>For more information about the <code>Content-Security-Policy</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy">Content-Security-Policy</a> in the MDN Web Docs.</p>"""
    content_type_options: NotRequired[
        "capo_cloudfront.types.response_headers_policy_content_type_options.ResponseHeadersPolicyContentTypeOptions"
    ]
    """<p>Determines whether CloudFront includes the <code>X-Content-Type-Options</code> HTTP response header with its value set to <code>nosniff</code>.</p> <p>For more information about the <code>X-Content-Type-Options</code> HTTP response header, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options">X-Content-Type-Options</a> in the MDN Web Docs.</p>"""
    strict_transport_security: NotRequired[
        "capo_cloudfront.types.response_headers_policy_strict_transport_security.ResponseHeadersPolicyStrictTransportSecurity"
    ]
    """<p>Determines whether CloudFront includes the <code>Strict-Transport-Security</code> HTTP response header and the header's value.</p> <p>For more information about the <code>Strict-Transport-Security</code> HTTP response header, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.html#understanding-response-headers-policies-security">Security headers</a> in the <i>Amazon CloudFront Developer Guide</i> and <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security">Strict-Transport-Security</a> in the MDN Web Docs.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicySecurityHeadersConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "xss_protection" in value:
        import capo_cloudfront.types.response_headers_policy_xss_protection

        capo_cloudfront.types.response_headers_policy_xss_protection.serialize_xml(
            value["xss_protection"], el, "XSSProtection"
        )
    if "frame_options" in value:
        import capo_cloudfront.types.response_headers_policy_frame_options

        capo_cloudfront.types.response_headers_policy_frame_options.serialize_xml(
            value["frame_options"], el, "FrameOptions"
        )
    if "referrer_policy" in value:
        import capo_cloudfront.types.response_headers_policy_referrer_policy

        capo_cloudfront.types.response_headers_policy_referrer_policy.serialize_xml(
            value["referrer_policy"], el, "ReferrerPolicy"
        )
    if "content_security_policy" in value:
        import capo_cloudfront.types.response_headers_policy_content_security_policy

        capo_cloudfront.types.response_headers_policy_content_security_policy.serialize_xml(
            value["content_security_policy"], el, "ContentSecurityPolicy"
        )
    if "content_type_options" in value:
        import capo_cloudfront.types.response_headers_policy_content_type_options

        capo_cloudfront.types.response_headers_policy_content_type_options.serialize_xml(
            value["content_type_options"], el, "ContentTypeOptions"
        )
    if "strict_transport_security" in value:
        import capo_cloudfront.types.response_headers_policy_strict_transport_security

        capo_cloudfront.types.response_headers_policy_strict_transport_security.serialize_xml(
            value["strict_transport_security"], el, "StrictTransportSecurity"
        )


def deserialize_xml(el: Element) -> ResponseHeadersPolicySecurityHeadersConfig:
    out: ResponseHeadersPolicySecurityHeadersConfig = {}  # type: ignore[typeddict-item]
    child_xss_protection = el.find("XSSProtection")
    if child_xss_protection is not None:
        import capo_cloudfront.types.response_headers_policy_xss_protection

        out["xss_protection"] = (
            capo_cloudfront.types.response_headers_policy_xss_protection.deserialize_xml(
                child_xss_protection
            )
        )
    child_frame_options = el.find("FrameOptions")
    if child_frame_options is not None:
        import capo_cloudfront.types.response_headers_policy_frame_options

        out["frame_options"] = (
            capo_cloudfront.types.response_headers_policy_frame_options.deserialize_xml(
                child_frame_options
            )
        )
    child_referrer_policy = el.find("ReferrerPolicy")
    if child_referrer_policy is not None:
        import capo_cloudfront.types.response_headers_policy_referrer_policy

        out["referrer_policy"] = (
            capo_cloudfront.types.response_headers_policy_referrer_policy.deserialize_xml(
                child_referrer_policy
            )
        )
    child_content_security_policy = el.find("ContentSecurityPolicy")
    if child_content_security_policy is not None:
        import capo_cloudfront.types.response_headers_policy_content_security_policy

        out["content_security_policy"] = (
            capo_cloudfront.types.response_headers_policy_content_security_policy.deserialize_xml(
                child_content_security_policy
            )
        )
    child_content_type_options = el.find("ContentTypeOptions")
    if child_content_type_options is not None:
        import capo_cloudfront.types.response_headers_policy_content_type_options

        out["content_type_options"] = (
            capo_cloudfront.types.response_headers_policy_content_type_options.deserialize_xml(
                child_content_type_options
            )
        )
    child_strict_transport_security = el.find("StrictTransportSecurity")
    if child_strict_transport_security is not None:
        import capo_cloudfront.types.response_headers_policy_strict_transport_security

        out["strict_transport_security"] = (
            capo_cloudfront.types.response_headers_policy_strict_transport_security.deserialize_xml(
                child_strict_transport_security
            )
        )
    return out
