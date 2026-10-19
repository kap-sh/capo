"""Generated from Smithy shape ``com.amazonaws.cloudfront#DomainItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DomainItem(TypedDict, closed=True):
    domain: "capo_cloudfront.types.string.string"
    """<p>The domain name.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DomainItem, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])


def deserialize_xml(el: Element) -> DomainItem:
    out: DomainItem = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        out["domain"] = ""
    return out
