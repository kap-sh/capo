"""Generated from Smithy shape ``com.amazonaws.route53#ListHostedZonesByNameResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.hosted_zones
    import capo_route_53.types.page_truncated
    import capo_route_53.types.resource_id


class ListHostedZonesByNameResponse(TypedDict, closed=True):
    hosted_zones: "capo_route_53.types.hosted_zones.HostedZones"
    """<p>A complex type that contains general information about the hosted zone.</p>"""
    dns_name: NotRequired["capo_route_53.types.dns_name.DNSName"]
    """<p>For the second and subsequent calls to <code>ListHostedZonesByName</code>, <code>DNSName</code> is the value that you specified for the <code>dnsname</code> parameter in the request that produced the current response.</p>"""
    hosted_zone_id: NotRequired["capo_route_53.types.resource_id.ResourceId"]
    """<p>The ID that Amazon Route 53 assigned to the hosted zone when you created it.</p>"""
    is_truncated: "capo_route_53.types.page_truncated.PageTruncated"
    """<p>A flag that indicates whether there are more hosted zones to be listed. If the response was truncated, you can get the next group of <code>maxitems</code> hosted zones by calling <code>ListHostedZonesByName</code> again and specifying the values of <code>NextDNSName</code> and <code>NextHostedZoneId</code> elements in the <code>dnsname</code> and <code>hostedzoneid</code> parameters.</p>"""
    next_dns_name: NotRequired["capo_route_53.types.dns_name.DNSName"]
    """<p>If <code>IsTruncated</code> is true, the value of <code>NextDNSName</code> is the name of the first hosted zone in the next group of <code>maxitems</code> hosted zones. Call <code>ListHostedZonesByName</code> again and specify the value of <code>NextDNSName</code> and <code>NextHostedZoneId</code> in the <code>dnsname</code> and <code>hostedzoneid</code> parameters, respectively.</p> <p>This element is present only if <code>IsTruncated</code> is <code>true</code>.</p>"""
    next_hosted_zone_id: NotRequired["capo_route_53.types.resource_id.ResourceId"]
    """<p>If <code>IsTruncated</code> is <code>true</code>, the value of <code>NextHostedZoneId</code> identifies the first hosted zone in the next group of <code>maxitems</code> hosted zones. Call <code>ListHostedZonesByName</code> again and specify the value of <code>NextDNSName</code> and <code>NextHostedZoneId</code> in the <code>dnsname</code> and <code>hostedzoneid</code> parameters, respectively.</p> <p>This element is present only if <code>IsTruncated</code> is <code>true</code>.</p>"""
    max_items: "int"
    """<p>The value that you specified for the <code>maxitems</code> parameter in the call to <code>ListHostedZonesByName</code> that produced the current response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListHostedZonesByNameResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.hosted_zones

    capo_route_53.types.hosted_zones.serialize_xml(
        value["hosted_zones"], el, "HostedZones"
    )
    if "dns_name" in value:
        SubElement(el, "DNSName").text = str(value["dns_name"])
    if "hosted_zone_id" in value:
        SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])
    SubElement(el, "IsTruncated").text = (
        "true" if value.get("is_truncated", False) else "false"
    )
    if "next_dns_name" in value:
        SubElement(el, "NextDNSName").text = str(value["next_dns_name"])
    if "next_hosted_zone_id" in value:
        SubElement(el, "NextHostedZoneId").text = str(value["next_hosted_zone_id"])
    SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListHostedZonesByNameResponse:
    out: ListHostedZonesByNameResponse = {}  # type: ignore[typeddict-item]
    child_hosted_zones = el.find("HostedZones")
    if child_hosted_zones is not None:
        import capo_route_53.types.hosted_zones

        out["hosted_zones"] = capo_route_53.types.hosted_zones.deserialize_xml(
            child_hosted_zones
        )
    else:
        out["hosted_zones"] = []
    child_dns_name = el.find("DNSName")
    if child_dns_name is not None:
        out["dns_name"] = str(child_dns_name.text or "")
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_next_dns_name = el.find("NextDNSName")
    if child_next_dns_name is not None:
        out["next_dns_name"] = str(child_next_dns_name.text or "")
    child_next_hosted_zone_id = el.find("NextHostedZoneId")
    if child_next_hosted_zone_id is not None:
        out["next_hosted_zone_id"] = str(child_next_hosted_zone_id.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        out["max_items"] = 0
    return out
