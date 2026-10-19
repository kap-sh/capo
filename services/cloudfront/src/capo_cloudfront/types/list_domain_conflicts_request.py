"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDomainConflictsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_resource_id
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class ListDomainConflictsRequest(TypedDict, closed=True):
    domain: "capo_cloudfront.types.string.string"
    """<p>The domain to check for conflicts.</p>"""
    domain_control_validation_resource: (
        "capo_cloudfront.types.distribution_resource_id.DistributionResourceId"
    )
    """<p>The distribution resource identifier. This can be the standard distribution or distribution tenant that has a valid certificate, which covers the domain that you specify.</p>"""
    max_items: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The maximum number of domain conflicts to return.</p>"""
    marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The marker for the next set of domain conflicts.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListDomainConflictsRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])
    import capo_cloudfront.types.distribution_resource_id

    capo_cloudfront.types.distribution_resource_id.serialize_xml(
        value["domain_control_validation_resource"],
        el,
        "DomainControlValidationResource",
    )
    if "max_items" in value:
        SubElement(el, "MaxItems").text = str(value["max_items"])
    if "marker" in value:
        SubElement(el, "Marker").text = str(value["marker"])


def deserialize_xml(el: Element) -> ListDomainConflictsRequest:
    out: ListDomainConflictsRequest = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        out["domain"] = ""
    child_domain_control_validation_resource = el.find(
        "DomainControlValidationResource"
    )
    if child_domain_control_validation_resource is not None:
        import capo_cloudfront.types.distribution_resource_id

        out["domain_control_validation_resource"] = (
            capo_cloudfront.types.distribution_resource_id.deserialize_xml(
                child_domain_control_validation_resource
            )
        )
    else:
        raise DeserializationError(
            "ListDomainConflictsRequest.domain_control_validation_resource required"
        )
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
