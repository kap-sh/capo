"""Generated from Smithy shape ``com.amazonaws.route53#ListHostedZonesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.hosted_zones
    import capo_route_53.types.page_marker
    import capo_route_53.types.page_truncated


class ListHostedZonesResponse(TypedDict, closed=True):
    hosted_zones: "capo_route_53.types.hosted_zones.HostedZones"
    """<p>A complex type that contains general information about the hosted zone.</p>"""
    marker: "capo_route_53.types.page_marker.PageMarker"
    """<p>For the second and subsequent calls to <code>ListHostedZones</code>, <code>Marker</code> is the value that you specified for the <code>marker</code> parameter in the request that produced the current response.</p>"""
    is_truncated: "capo_route_53.types.page_truncated.PageTruncated"
    """<p>A flag indicating whether there are more hosted zones to be listed. If the response was truncated, you can get more hosted zones by submitting another <code>ListHostedZones</code> request and specifying the value of <code>NextMarker</code> in the <code>marker</code> parameter.</p>"""
    next_marker: NotRequired["capo_route_53.types.page_marker.PageMarker"]
    """<p>If <code>IsTruncated</code> is <code>true</code>, the value of <code>NextMarker</code> identifies the first hosted zone in the next group of hosted zones. Submit another <code>ListHostedZones</code> request, and specify the value of <code>NextMarker</code> from the response in the <code>marker</code> parameter.</p> <p>This element is present only if <code>IsTruncated</code> is <code>true</code>.</p>"""
    max_items: "int"
    """<p>The value that you specified for the <code>maxitems</code> parameter in the call to <code>ListHostedZones</code> that produced the current response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListHostedZonesResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.hosted_zones

    capo_route_53.types.hosted_zones.serialize_xml(
        value["hosted_zones"], el, "HostedZones"
    )
    SubElement(el, "Marker").text = str(value["marker"])
    SubElement(el, "IsTruncated").text = (
        "true" if value.get("is_truncated", False) else "false"
    )
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListHostedZonesResponse:
    out: ListHostedZonesResponse = {}  # type: ignore[typeddict-item]
    child_hosted_zones = el.find("HostedZones")
    if child_hosted_zones is not None:
        import capo_route_53.types.hosted_zones

        out["hosted_zones"] = capo_route_53.types.hosted_zones.deserialize_xml(
            child_hosted_zones
        )
    else:
        out["hosted_zones"] = []
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
