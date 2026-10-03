"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyXSSProtection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.string


class ResponseHeadersPolicyXSSProtection(TypedDict, closed=True):
    override: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront overrides the <code>X-XSS-Protection</code> HTTP response header received from the origin with the one specified in this response headers policy.</p>"""
    protection: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines the value of the <code>X-XSS-Protection</code> HTTP response header. When this setting is <code>true</code>, the value of the <code>X-XSS-Protection</code> header is <code>1</code>. When this setting is <code>false</code>, the value of the <code>X-XSS-Protection</code> header is <code>0</code>.</p> <p>For more information about these settings, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection">X-XSS-Protection</a> in the MDN Web Docs.</p>"""
    mode_block: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>A Boolean that determines whether CloudFront includes the <code>mode=block</code> directive in the <code>X-XSS-Protection</code> header.</p> <p>For more information about this directive, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection">X-XSS-Protection</a> in the MDN Web Docs.</p>"""
    report_uri: NotRequired["capo_cloudfront.types.string.string"]
    """<p>A reporting URI, which CloudFront uses as the value of the <code>report</code> directive in the <code>X-XSS-Protection</code> header.</p> <p>You cannot specify a <code>ReportUri</code> when <code>ModeBlock</code> is <code>true</code>.</p> <p>For more information about using a reporting URL, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection">X-XSS-Protection</a> in the MDN Web Docs.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyXSSProtection, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Override").text = "true" if value["override"] else "false"
    SubElement(el, "Protection").text = "true" if value["protection"] else "false"
    if "mode_block" in value:
        SubElement(el, "ModeBlock").text = "true" if value["mode_block"] else "false"
    if "report_uri" in value:
        SubElement(el, "ReportUri").text = str(value["report_uri"])


def deserialize_xml(el: Element) -> ResponseHeadersPolicyXSSProtection:
    out: ResponseHeadersPolicyXSSProtection = {}  # type: ignore[typeddict-item]
    child_override = el.find("Override")
    if child_override is not None:
        out["override"] = (child_override.text or "").lower() == "true"
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyXSSProtection.override required"
        )
    child_protection = el.find("Protection")
    if child_protection is not None:
        out["protection"] = (child_protection.text or "").lower() == "true"
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyXSSProtection.protection required"
        )
    child_mode_block = el.find("ModeBlock")
    if child_mode_block is not None:
        out["mode_block"] = (child_mode_block.text or "").lower() == "true"
    child_report_uri = el.find("ReportUri")
    if child_report_uri is not None:
        out["report_uri"] = str(child_report_uri.text or "")
    return out
