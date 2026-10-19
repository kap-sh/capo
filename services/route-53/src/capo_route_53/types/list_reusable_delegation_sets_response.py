"""Generated from Smithy shape ``com.amazonaws.route53#ListReusableDelegationSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.delegation_sets
    import capo_route_53.types.page_marker
    import capo_route_53.types.page_truncated


class ListReusableDelegationSetsResponse(TypedDict, closed=True):
    delegation_sets: "capo_route_53.types.delegation_sets.DelegationSets"
    """<p>A complex type that contains one <code>DelegationSet</code> element for each reusable delegation set that was created by the current Amazon Web Services account.</p>"""
    marker: "capo_route_53.types.page_marker.PageMarker"
    """<p>For the second and subsequent calls to <code>ListReusableDelegationSets</code>, <code>Marker</code> is the value that you specified for the <code>marker</code> parameter in the request that produced the current response.</p>"""
    is_truncated: "capo_route_53.types.page_truncated.PageTruncated"
    """<p>A flag that indicates whether there are more reusable delegation sets to be listed.</p>"""
    next_marker: NotRequired["capo_route_53.types.page_marker.PageMarker"]
    """<p>If <code>IsTruncated</code> is <code>true</code>, the value of <code>NextMarker</code> identifies the next reusable delegation set that Amazon Route 53 will return if you submit another <code>ListReusableDelegationSets</code> request and specify the value of <code>NextMarker</code> in the <code>marker</code> parameter.</p>"""
    max_items: "int"
    """<p>The value that you specified for the <code>maxitems</code> parameter in the call to <code>ListReusableDelegationSets</code> that produced the current response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListReusableDelegationSetsResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.delegation_sets

    capo_route_53.types.delegation_sets.serialize_xml(
        value["delegation_sets"], el, "DelegationSets"
    )
    SubElement(el, "Marker").text = str(value["marker"])
    SubElement(el, "IsTruncated").text = (
        "true" if value.get("is_truncated", False) else "false"
    )
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListReusableDelegationSetsResponse:
    out: ListReusableDelegationSetsResponse = {}  # type: ignore[typeddict-item]
    child_delegation_sets = el.find("DelegationSets")
    if child_delegation_sets is not None:
        import capo_route_53.types.delegation_sets

        out["delegation_sets"] = capo_route_53.types.delegation_sets.deserialize_xml(
            child_delegation_sets
        )
    else:
        out["delegation_sets"] = []
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    else:
        out["marker"] = ""
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        out["max_items"] = 0
    return out
