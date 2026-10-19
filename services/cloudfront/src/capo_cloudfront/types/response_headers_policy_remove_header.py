"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyRemoveHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class ResponseHeadersPolicyRemoveHeader(TypedDict, closed=True):
    header: "capo_cloudfront.types.string.string"
    """<p>The HTTP header name.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyRemoveHeader, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Header").text = str(value["header"])


def deserialize_xml(el: Element) -> ResponseHeadersPolicyRemoveHeader:
    out: ResponseHeadersPolicyRemoveHeader = {}  # type: ignore[typeddict-item]
    child_header = el.find("Header")
    if child_header is not None:
        out["header"] = str(child_header.text or "")
    else:
        out["header"] = ""
    return out
