"""Generated from Smithy shape ``com.amazonaws.route53#ListTrafficPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.page_truncated
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_summaries


class ListTrafficPoliciesResponse(TypedDict, closed=True):
    traffic_policy_summaries: (
        "capo_route_53.types.traffic_policy_summaries.TrafficPolicySummaries"
    )
    """<p>A list that contains one <code>TrafficPolicySummary</code> element for each traffic policy that was created by the current Amazon Web Services account.</p>"""
    is_truncated: "capo_route_53.types.page_truncated.PageTruncated"
    """<p>A flag that indicates whether there are more traffic policies to be listed. If the response was truncated, you can get the next group of traffic policies by submitting another <code>ListTrafficPolicies</code> request and specifying the value of <code>TrafficPolicyIdMarker</code> in the <code>TrafficPolicyIdMarker</code> request parameter.</p>"""
    traffic_policy_id_marker: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>If the value of <code>IsTruncated</code> is <code>true</code>, <code>TrafficPolicyIdMarker</code> is the ID of the first traffic policy in the next group of <code>MaxItems</code> traffic policies.</p>"""
    max_items: "int"
    """<p>The value that you specified for the <code>MaxItems</code> parameter in the <code>ListTrafficPolicies</code> request that produced the current response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTrafficPoliciesResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.traffic_policy_summaries

    capo_route_53.types.traffic_policy_summaries.serialize_xml(
        value["traffic_policy_summaries"], el, "TrafficPolicySummaries"
    )
    SubElement(el, "IsTruncated").text = (
        "true" if value.get("is_truncated", False) else "false"
    )
    SubElement(el, "TrafficPolicyIdMarker").text = str(
        value["traffic_policy_id_marker"]
    )
    SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListTrafficPoliciesResponse:
    out: ListTrafficPoliciesResponse = {}  # type: ignore[typeddict-item]
    child_traffic_policy_summaries = el.find("TrafficPolicySummaries")
    if child_traffic_policy_summaries is not None:
        import capo_route_53.types.traffic_policy_summaries

        out["traffic_policy_summaries"] = (
            capo_route_53.types.traffic_policy_summaries.deserialize_xml(
                child_traffic_policy_summaries
            )
        )
    else:
        out["traffic_policy_summaries"] = []
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_traffic_policy_id_marker = el.find("TrafficPolicyIdMarker")
    if child_traffic_policy_id_marker is not None:
        out["traffic_policy_id_marker"] = str(child_traffic_policy_id_marker.text or "")
    else:
        out["traffic_policy_id_marker"] = ""
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        out["max_items"] = 0
    return out
