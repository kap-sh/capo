"""Generated from Smithy shape ``com.amazonaws.cloudfront#DomainResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.domain_status
    import capo_cloudfront.types.string


class DomainResult(TypedDict, closed=True):
    domain: "capo_cloudfront.types.string.string"
    """<p>The specified domain.</p>"""
    status: NotRequired["capo_cloudfront.types.domain_status.DomainStatus"]
    """<p>Whether the domain is active or inactive.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DomainResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])
    if "status" in value:
        import capo_cloudfront.types.domain_status

        capo_cloudfront.types.domain_status.serialize_xml(value["status"], el, "Status")


def deserialize_xml(el: Element) -> DomainResult:
    out: DomainResult = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        out["domain"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudfront.types.domain_status

        out["status"] = capo_cloudfront.types.domain_status.deserialize_xml(
            child_status
        )
    return out
