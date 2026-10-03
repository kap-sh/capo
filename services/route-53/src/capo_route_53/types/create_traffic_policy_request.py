"""Generated from Smithy shape ``com.amazonaws.route53#CreateTrafficPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.traffic_policy_comment
    import capo_route_53.types.traffic_policy_document
    import capo_route_53.types.traffic_policy_name


class CreateTrafficPolicyRequest(TypedDict, closed=True):
    name: "capo_route_53.types.traffic_policy_name.TrafficPolicyName"
    """<p>The name of the traffic policy.</p>"""
    document: "capo_route_53.types.traffic_policy_document.TrafficPolicyDocument"
    """<p>The definition of this traffic policy in JSON format. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html">Traffic Policy Document Format</a>.</p>"""
    comment: NotRequired[
        "capo_route_53.types.traffic_policy_comment.TrafficPolicyComment"
    ]
    """<p>(Optional) Any comments that you want to include about the traffic policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateTrafficPolicyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Document").text = str(value["document"])
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> CreateTrafficPolicyRequest:
    out: CreateTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateTrafficPolicyRequest.name required")
    child_document = el.find("Document")
    if child_document is not None:
        out["document"] = str(child_document.text or "")
    else:
        raise DeserializationError("CreateTrafficPolicyRequest.document required")
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
