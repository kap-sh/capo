"""Generated from Smithy shape ``com.amazonaws.cloudfront#CacheTagConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class CacheTagConfig(TypedDict, closed=True):
    header_name: "capo_cloudfront.types.string.string"
    """<p>The name of the HTTP header that your origin includes in responses. CloudFront uses this header to extract cache tags. The header value must contain comma-separated tag values (for example, <code>product:electronics, category:tv, brand:example</code>).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CacheTagConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HeaderName").text = str(value["header_name"])


def deserialize_xml(el: Element) -> CacheTagConfig:
    out: CacheTagConfig = {}  # type: ignore[typeddict-item]
    child_header_name = el.find("HeaderName")
    if child_header_name is not None:
        out["header_name"] = str(child_header_name.text or "")
    else:
        out["header_name"] = ""
    return out
