"""Generated from Smithy shape ``com.amazonaws.iot#ListPrincipalPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.marker
    import capo_iot.types.page_size
    import capo_iot.types.principal


class ListPrincipalPoliciesRequest(TypedDict, closed=True):
    principal: "capo_iot.types.principal.Principal"
    """<p>The principal. Valid principals are CertificateArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:cert/<i>certificateId</i>), thingGroupArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:thinggroup/<i>groupName</i>) and CognitoId (<i>region</i>:<i>id</i>).</p>"""
    marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    page_size: NotRequired["capo_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p>Specifies the order for results. If true, results are returned in ascending creation order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrincipalPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPrincipalPoliciesRequest:
    out: ListPrincipalPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
