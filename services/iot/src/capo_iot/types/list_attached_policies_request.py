"""Generated from Smithy shape ``com.amazonaws.iot#ListAttachedPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.marker
    import capo_iot.types.page_size
    import capo_iot.types.policy_target
    import capo_iot.types.recursive


class ListAttachedPoliciesRequest(TypedDict, closed=True):
    target: "capo_iot.types.policy_target.PolicyTarget"
    """<p>The group or principal for which the policies will be listed. Valid principals are CertificateArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:cert/<i>certificateId</i>), thingGroupArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:thinggroup/<i>groupName</i>) and CognitoId (<i>region</i>:<i>id</i>).</p>"""
    recursive: NotRequired["capo_iot.types.recursive.Recursive"]
    """<p>When true, recursively list attached policies.</p>"""
    marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The token to retrieve the next set of results.</p>"""
    page_size: NotRequired["capo_iot.types.page_size.PageSize"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachedPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAttachedPoliciesRequest:
    out: ListAttachedPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
