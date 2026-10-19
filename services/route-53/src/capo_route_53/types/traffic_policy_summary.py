"""Generated from Smithy shape ``com.amazonaws.route53#TrafficPolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.rr_type
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_name
    import capo_route_53.types.traffic_policy_version


class TrafficPolicySummary(TypedDict, closed=True):
    id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The ID that Amazon Route 53 assigned to the traffic policy when you created it.</p>"""
    name: "capo_route_53.types.traffic_policy_name.TrafficPolicyName"
    """<p>The name that you specified for the traffic policy when you created it.</p>"""
    type: "capo_route_53.types.rr_type.RRType"
    """<p>The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.</p>"""
    latest_version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    """<p>The version number of the latest version of the traffic policy.</p>"""
    traffic_policy_count: (
        "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    )
    """<p>The number of traffic policies that are associated with the current Amazon Web Services account.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TrafficPolicySummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Name").text = str(value["name"])
    import capo_route_53.types.rr_type

    capo_route_53.types.rr_type.serialize_xml(value["type"], el, "Type")
    SubElement(el, "LatestVersion").text = str(value["latest_version"])
    SubElement(el, "TrafficPolicyCount").text = str(value["traffic_policy_count"])


def deserialize_xml(el: Element) -> TrafficPolicySummary:
    out: TrafficPolicySummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_type = el.find("Type")
    if child_type is not None:
        import capo_route_53.types.rr_type

        out["type"] = capo_route_53.types.rr_type.deserialize_xml(child_type)
    else:
        import typing

        out["type"] = typing.cast("capo_route_53.types.rr_type.RRType", "")
    child_latest_version = el.find("LatestVersion")
    if child_latest_version is not None:
        out["latest_version"] = int(child_latest_version.text or "")
    else:
        out["latest_version"] = 0
    child_traffic_policy_count = el.find("TrafficPolicyCount")
    if child_traffic_policy_count is not None:
        out["traffic_policy_count"] = int(child_traffic_policy_count.text or "")
    else:
        out["traffic_policy_count"] = 0
    return out
