"""Generated from Smithy shape ``com.amazonaws.route53#ListTrafficPolicyInstancesByHostedZoneResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.page_truncated
    import capo_route_53.types.rr_type
    import capo_route_53.types.traffic_policy_instances


class ListTrafficPolicyInstancesByHostedZoneResponse(TypedDict, closed=True):
    traffic_policy_instances: (
        "capo_route_53.types.traffic_policy_instances.TrafficPolicyInstances"
    )
    """<p>A list that contains one <code>TrafficPolicyInstance</code> element for each traffic policy instance that matches the elements in the request. </p>"""
    traffic_policy_instance_name_marker: NotRequired[
        "capo_route_53.types.dns_name.DNSName"
    ]
    """<p>If <code>IsTruncated</code> is <code>true</code>, <code>TrafficPolicyInstanceNameMarker</code> is the name of the first traffic policy instance in the next group of traffic policy instances.</p>"""
    traffic_policy_instance_type_marker: NotRequired[
        "capo_route_53.types.rr_type.RRType"
    ]
    """<p>If <code>IsTruncated</code> is true, <code>TrafficPolicyInstanceTypeMarker</code> is the DNS type of the resource record sets that are associated with the first traffic policy instance in the next group of traffic policy instances.</p>"""
    is_truncated: "capo_route_53.types.page_truncated.PageTruncated"
    """<p>A flag that indicates whether there are more traffic policy instances to be listed. If the response was truncated, you can get the next group of traffic policy instances by submitting another <code>ListTrafficPolicyInstancesByHostedZone</code> request and specifying the values of <code>HostedZoneIdMarker</code>, <code>TrafficPolicyInstanceNameMarker</code>, and <code>TrafficPolicyInstanceTypeMarker</code> in the corresponding request parameters.</p>"""
    max_items: "int"
    """<p>The value that you specified for the <code>MaxItems</code> parameter in the <code>ListTrafficPolicyInstancesByHostedZone</code> request that produced the current response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTrafficPolicyInstancesByHostedZoneResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.traffic_policy_instances

    capo_route_53.types.traffic_policy_instances.serialize_xml(
        value["traffic_policy_instances"], el, "TrafficPolicyInstances"
    )
    if "traffic_policy_instance_name_marker" in value:
        SubElement(el, "TrafficPolicyInstanceNameMarker").text = str(
            value["traffic_policy_instance_name_marker"]
        )
    if "traffic_policy_instance_type_marker" in value:
        import capo_route_53.types.rr_type

        capo_route_53.types.rr_type.serialize_xml(
            value["traffic_policy_instance_type_marker"],
            el,
            "TrafficPolicyInstanceTypeMarker",
        )
    SubElement(el, "IsTruncated").text = (
        "true" if value.get("is_truncated", False) else "false"
    )
    SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListTrafficPolicyInstancesByHostedZoneResponse:
    out: ListTrafficPolicyInstancesByHostedZoneResponse = {}  # type: ignore[typeddict-item]
    child_traffic_policy_instances = el.find("TrafficPolicyInstances")
    if child_traffic_policy_instances is not None:
        import capo_route_53.types.traffic_policy_instances

        out["traffic_policy_instances"] = (
            capo_route_53.types.traffic_policy_instances.deserialize_xml(
                child_traffic_policy_instances
            )
        )
    else:
        out["traffic_policy_instances"] = []
    child_traffic_policy_instance_name_marker = el.find(
        "TrafficPolicyInstanceNameMarker"
    )
    if child_traffic_policy_instance_name_marker is not None:
        out["traffic_policy_instance_name_marker"] = str(
            child_traffic_policy_instance_name_marker.text or ""
        )
    child_traffic_policy_instance_type_marker = el.find(
        "TrafficPolicyInstanceTypeMarker"
    )
    if child_traffic_policy_instance_type_marker is not None:
        import capo_route_53.types.rr_type

        out["traffic_policy_instance_type_marker"] = (
            capo_route_53.types.rr_type.deserialize_xml(
                child_traffic_policy_instance_type_marker
            )
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        out["max_items"] = 0
    return out
