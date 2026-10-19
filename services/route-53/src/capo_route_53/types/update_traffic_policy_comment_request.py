"""Generated from Smithy shape ``com.amazonaws.route53#UpdateTrafficPolicyCommentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.traffic_policy_comment
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_version


class UpdateTrafficPolicyCommentRequest(TypedDict, closed=True):
    id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The value of <code>Id</code> for the traffic policy that you want to update the comment for.</p>"""
    version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    """<p>The value of <code>Version</code> for the traffic policy that you want to update the comment for.</p>"""
    comment: "capo_route_53.types.traffic_policy_comment.TrafficPolicyComment"
    """<p>The new comment for the specified traffic policy and version.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateTrafficPolicyCommentRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> UpdateTrafficPolicyCommentRequest:
    out: UpdateTrafficPolicyCommentRequest = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        out["comment"] = ""
    return out
