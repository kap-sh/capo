"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginCustomHeader``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.sensitive_string_type
    import capo_cloudfront.types.string


class OriginCustomHeader(TypedDict, closed=True):
    header_name: "capo_cloudfront.types.string.string"
    """<p>The name of a header that you want CloudFront to send to your origin. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html">Adding Custom Headers to Origin Requests</a> in the <i> Amazon CloudFront Developer Guide</i>.</p>"""
    header_value: "capo_cloudfront.types.sensitive_string_type.sensitiveStringType"
    """<p>The value for the header that you specified in the <code>HeaderName</code> field.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginCustomHeader, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HeaderName").text = str(value["header_name"])
    SubElement(el, "HeaderValue").text = str(value["header_value"])


def deserialize_xml(el: Element) -> OriginCustomHeader:
    out: OriginCustomHeader = {}  # type: ignore[typeddict-item]
    child_header_name = el.find("HeaderName")
    if child_header_name is not None:
        out["header_name"] = str(child_header_name.text or "")
    else:
        out["header_name"] = ""
    child_header_value = el.find("HeaderValue")
    if child_header_value is not None:
        out["header_value"] = str(child_header_value.text or "")
    else:
        out["header_value"] = ""
    return out


def redact_sensitive(value: OriginCustomHeader) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "header_value" in value:
        out["header_value"] = "*** Sensitive Data Redacted ***"
    return out
