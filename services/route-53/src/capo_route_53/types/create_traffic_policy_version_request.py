"""Generated from Smithy shape ``com.amazonaws.route53#CreateTrafficPolicyVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.traffic_policy_comment
    import capo_route_53.types.traffic_policy_document
    import capo_route_53.types.traffic_policy_id


class CreateTrafficPolicyVersionRequest(TypedDict, closed=True):
    id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The ID of the traffic policy for which you want to create a new version.</p>"""
    document: "capo_route_53.types.traffic_policy_document.TrafficPolicyDocument"
    """<p>The definition of this version of the traffic policy, in JSON format. You specified the JSON in the <code>CreateTrafficPolicyVersion</code> request. For more information about the JSON format, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicy.html">CreateTrafficPolicy</a>.</p>"""
    comment: NotRequired[
        "capo_route_53.types.traffic_policy_comment.TrafficPolicyComment"
    ]
    """<p>The comment that you specified in the <code>CreateTrafficPolicyVersion</code> request, if any.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateTrafficPolicyVersionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Document").text = str(value["document"])
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> CreateTrafficPolicyVersionRequest:
    out: CreateTrafficPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    child_document = el.find("Document")
    if child_document is not None:
        out["document"] = str(child_document.text or "")
    else:
        raise DeserializationError(
            "CreateTrafficPolicyVersionRequest.document required"
        )
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
