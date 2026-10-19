"""Generated from Smithy shape ``com.amazonaws.cloudfront#ValidationTokenDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class ValidationTokenDetail(TypedDict, closed=True):
    domain: "capo_cloudfront.types.string.string"
    """<p>The domain name.</p>"""
    redirect_to: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The domain to redirect to.</p>"""
    redirect_from: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The domain to redirect from.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ValidationTokenDetail, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])
    if "redirect_to" in value:
        SubElement(el, "RedirectTo").text = str(value["redirect_to"])
    if "redirect_from" in value:
        SubElement(el, "RedirectFrom").text = str(value["redirect_from"])


def deserialize_xml(el: Element) -> ValidationTokenDetail:
    out: ValidationTokenDetail = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        out["domain"] = ""
    child_redirect_to = el.find("RedirectTo")
    if child_redirect_to is not None:
        out["redirect_to"] = str(child_redirect_to.text or "")
    child_redirect_from = el.find("RedirectFrom")
    if child_redirect_from is not None:
        out["redirect_from"] = str(child_redirect_from.text or "")
    return out
