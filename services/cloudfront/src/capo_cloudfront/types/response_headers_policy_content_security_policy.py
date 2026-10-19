"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyContentSecurityPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.string


class ResponseHeadersPolicyContentSecurityPolicy(TypedDict, closed=True):
    override: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront overrides the <code>Content-Security-Policy</code> HTTP response header received from the origin with the one specified in this response headers policy.</p>"""
    content_security_policy: "capo_cloudfront.types.string.string"
    """<p>The policy directives and their values that CloudFront includes as values for the <code>Content-Security-Policy</code> HTTP response header.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyContentSecurityPolicy, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Override").text = "true" if value["override"] else "false"
    SubElement(el, "ContentSecurityPolicy").text = str(value["content_security_policy"])


def deserialize_xml(el: Element) -> ResponseHeadersPolicyContentSecurityPolicy:
    out: ResponseHeadersPolicyContentSecurityPolicy = {}  # type: ignore[typeddict-item]
    child_override = el.find("Override")
    if child_override is not None:
        out["override"] = (child_override.text or "").lower() == "true"
    else:
        out["override"] = False
    child_content_security_policy = el.find("ContentSecurityPolicy")
    if child_content_security_policy is not None:
        out["content_security_policy"] = str(child_content_security_policy.text or "")
    else:
        out["content_security_policy"] = ""
    return out
