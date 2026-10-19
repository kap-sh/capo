"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.response_headers_policy_cors_config
    import capo_cloudfront.types.response_headers_policy_custom_headers_config
    import capo_cloudfront.types.response_headers_policy_remove_headers_config
    import capo_cloudfront.types.response_headers_policy_security_headers_config
    import capo_cloudfront.types.response_headers_policy_server_timing_headers_config
    import capo_cloudfront.types.string


class ResponseHeadersPolicyConfig(TypedDict, closed=True):
    comment: NotRequired["capo_cloudfront.types.string.string"]
    """<p>A comment to describe the response headers policy.</p> <p>The comment cannot be longer than 128 characters.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>A name to identify the response headers policy.</p> <p>The name must be unique for response headers policies in this Amazon Web Services account.</p>"""
    cors_config: NotRequired[
        "capo_cloudfront.types.response_headers_policy_cors_config.ResponseHeadersPolicyCorsConfig"
    ]
    """<p>A configuration for a set of HTTP response headers that are used for cross-origin resource sharing (CORS).</p>"""
    security_headers_config: NotRequired[
        "capo_cloudfront.types.response_headers_policy_security_headers_config.ResponseHeadersPolicySecurityHeadersConfig"
    ]
    """<p>A configuration for a set of security-related HTTP response headers.</p>"""
    server_timing_headers_config: NotRequired[
        "capo_cloudfront.types.response_headers_policy_server_timing_headers_config.ResponseHeadersPolicyServerTimingHeadersConfig"
    ]
    """<p>A configuration for enabling the <code>Server-Timing</code> header in HTTP responses sent from CloudFront.</p>"""
    custom_headers_config: NotRequired[
        "capo_cloudfront.types.response_headers_policy_custom_headers_config.ResponseHeadersPolicyCustomHeadersConfig"
    ]
    """<p>A configuration for a set of custom HTTP response headers.</p>"""
    remove_headers_config: NotRequired[
        "capo_cloudfront.types.response_headers_policy_remove_headers_config.ResponseHeadersPolicyRemoveHeadersConfig"
    ]
    """<p>A configuration for a set of HTTP headers to remove from the HTTP response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    SubElement(el, "Name").text = str(value["name"])
    if "cors_config" in value:
        import capo_cloudfront.types.response_headers_policy_cors_config

        capo_cloudfront.types.response_headers_policy_cors_config.serialize_xml(
            value["cors_config"], el, "CorsConfig"
        )
    if "security_headers_config" in value:
        import capo_cloudfront.types.response_headers_policy_security_headers_config

        capo_cloudfront.types.response_headers_policy_security_headers_config.serialize_xml(
            value["security_headers_config"], el, "SecurityHeadersConfig"
        )
    if "server_timing_headers_config" in value:
        import capo_cloudfront.types.response_headers_policy_server_timing_headers_config

        capo_cloudfront.types.response_headers_policy_server_timing_headers_config.serialize_xml(
            value["server_timing_headers_config"], el, "ServerTimingHeadersConfig"
        )
    if "custom_headers_config" in value:
        import capo_cloudfront.types.response_headers_policy_custom_headers_config

        capo_cloudfront.types.response_headers_policy_custom_headers_config.serialize_xml(
            value["custom_headers_config"], el, "CustomHeadersConfig"
        )
    if "remove_headers_config" in value:
        import capo_cloudfront.types.response_headers_policy_remove_headers_config

        capo_cloudfront.types.response_headers_policy_remove_headers_config.serialize_xml(
            value["remove_headers_config"], el, "RemoveHeadersConfig"
        )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyConfig:
    out: ResponseHeadersPolicyConfig = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_cors_config = el.find("CorsConfig")
    if child_cors_config is not None:
        import capo_cloudfront.types.response_headers_policy_cors_config

        out["cors_config"] = (
            capo_cloudfront.types.response_headers_policy_cors_config.deserialize_xml(
                child_cors_config
            )
        )
    child_security_headers_config = el.find("SecurityHeadersConfig")
    if child_security_headers_config is not None:
        import capo_cloudfront.types.response_headers_policy_security_headers_config

        out["security_headers_config"] = (
            capo_cloudfront.types.response_headers_policy_security_headers_config.deserialize_xml(
                child_security_headers_config
            )
        )
    child_server_timing_headers_config = el.find("ServerTimingHeadersConfig")
    if child_server_timing_headers_config is not None:
        import capo_cloudfront.types.response_headers_policy_server_timing_headers_config

        out["server_timing_headers_config"] = (
            capo_cloudfront.types.response_headers_policy_server_timing_headers_config.deserialize_xml(
                child_server_timing_headers_config
            )
        )
    child_custom_headers_config = el.find("CustomHeadersConfig")
    if child_custom_headers_config is not None:
        import capo_cloudfront.types.response_headers_policy_custom_headers_config

        out["custom_headers_config"] = (
            capo_cloudfront.types.response_headers_policy_custom_headers_config.deserialize_xml(
                child_custom_headers_config
            )
        )
    child_remove_headers_config = el.find("RemoveHeadersConfig")
    if child_remove_headers_config is not None:
        import capo_cloudfront.types.response_headers_policy_remove_headers_config

        out["remove_headers_config"] = (
            capo_cloudfront.types.response_headers_policy_remove_headers_config.deserialize_xml(
                child_remove_headers_config
            )
        )
    return out
