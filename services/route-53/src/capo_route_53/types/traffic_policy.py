"""Generated from Smithy shape ``com.amazonaws.route53#TrafficPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.rr_type
    import capo_route_53.types.traffic_policy_comment
    import capo_route_53.types.traffic_policy_document
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_name
    import capo_route_53.types.traffic_policy_version


class TrafficPolicy(TypedDict, closed=True):
    id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The ID that Amazon Route 53 assigned to a traffic policy when you created it.</p>"""
    version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    """<p>The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of <code>Version</code> is always 1.</p>"""
    name: "capo_route_53.types.traffic_policy_name.TrafficPolicyName"
    """<p>The name that you specified when you created the traffic policy.</p>"""
    type: "capo_route_53.types.rr_type.RRType"
    """<p>The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.</p>"""
    document: "capo_route_53.types.traffic_policy_document.TrafficPolicyDocument"
    """<p>The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the <code>CreateTrafficPolicy</code> request. For more information about the JSON format, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html">Traffic Policy Document Format</a>.</p>"""
    comment: NotRequired[
        "capo_route_53.types.traffic_policy_comment.TrafficPolicyComment"
    ]
    """<p>The comment that you specify in the <code>CreateTrafficPolicy</code> request, if any.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TrafficPolicy, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Version").text = str(value["version"])
    SubElement(el, "Name").text = str(value["name"])
    import capo_route_53.types.rr_type

    capo_route_53.types.rr_type.serialize_xml(value["type"], el, "Type")
    SubElement(el, "Document").text = str(value["document"])
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> TrafficPolicy:
    out: TrafficPolicy = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("TrafficPolicy.id required")
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = int(child_version.text or "")
    else:
        raise DeserializationError("TrafficPolicy.version required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("TrafficPolicy.name required")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_route_53.types.rr_type

        out["type"] = capo_route_53.types.rr_type.deserialize_xml(child_type)
    else:
        raise DeserializationError("TrafficPolicy.type required")
    child_document = el.find("Document")
    if child_document is not None:
        out["document"] = str(child_document.text or "")
    else:
        raise DeserializationError("TrafficPolicy.document required")
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
