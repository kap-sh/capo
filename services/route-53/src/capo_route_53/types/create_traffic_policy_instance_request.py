"""Generated from Smithy shape ``com.amazonaws.route53#CreateTrafficPolicyInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.resource_id
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_version
    import capo_route_53.types.ttl


class CreateTrafficPolicyInstanceRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that you want Amazon Route 53 to create resource record sets in by using the configuration in a traffic policy.</p>"""
    name: "capo_route_53.types.dns_name.DNSName"
    """<p>The domain name (such as example.com) or subdomain name (such as www.example.com) for which Amazon Route 53 responds to DNS queries by using the resource record sets that Route 53 creates for this traffic policy instance.</p>"""
    ttl: "capo_route_53.types.ttl.TTL"
    """<p>(Optional) The TTL that you want Amazon Route 53 to assign to all of the resource record sets that it creates in the specified hosted zone.</p>"""
    traffic_policy_id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The ID of the traffic policy that you want to use to create resource record sets in the specified hosted zone.</p>"""
    traffic_policy_version: (
        "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    )
    """<p>The version of the traffic policy that you want to use to create resource record sets in the specified hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateTrafficPolicyInstanceRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "TTL").text = str(value["ttl"])
    SubElement(el, "TrafficPolicyId").text = str(value["traffic_policy_id"])
    SubElement(el, "TrafficPolicyVersion").text = str(value["traffic_policy_version"])


def deserialize_xml(el: Element) -> CreateTrafficPolicyInstanceRequest:
    out: CreateTrafficPolicyInstanceRequest = {}  # type: ignore[typeddict-item]
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    else:
        out["hosted_zone_id"] = ""
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_ttl = el.find("TTL")
    if child_ttl is not None:
        out["ttl"] = int(child_ttl.text or "")
    else:
        out["ttl"] = 0
    child_traffic_policy_id = el.find("TrafficPolicyId")
    if child_traffic_policy_id is not None:
        out["traffic_policy_id"] = str(child_traffic_policy_id.text or "")
    else:
        out["traffic_policy_id"] = ""
    child_traffic_policy_version = el.find("TrafficPolicyVersion")
    if child_traffic_policy_version is not None:
        out["traffic_policy_version"] = int(child_traffic_policy_version.text or "")
    else:
        out["traffic_policy_version"] = 0
    return out
