"""Generated from Smithy shape ``com.amazonaws.route53#UpdateTrafficPolicyInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_instance_id
    import capo_route_53.types.traffic_policy_version
    import capo_route_53.types.ttl


class UpdateTrafficPolicyInstanceRequest(TypedDict, closed=True):
    id: "capo_route_53.types.traffic_policy_instance_id.TrafficPolicyInstanceId"
    """<p>The ID of the traffic policy instance that you want to update.</p>"""
    ttl: "capo_route_53.types.ttl.TTL"
    """<p>The TTL that you want Amazon Route 53 to assign to all of the updated resource record sets.</p>"""
    traffic_policy_id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The ID of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.</p>"""
    traffic_policy_version: (
        "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    )
    """<p>The version of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateTrafficPolicyInstanceRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "TTL").text = str(value["ttl"])
    SubElement(el, "TrafficPolicyId").text = str(value["traffic_policy_id"])
    SubElement(el, "TrafficPolicyVersion").text = str(value["traffic_policy_version"])


def deserialize_xml(el: Element) -> UpdateTrafficPolicyInstanceRequest:
    out: UpdateTrafficPolicyInstanceRequest = {}  # type: ignore[typeddict-item]
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
