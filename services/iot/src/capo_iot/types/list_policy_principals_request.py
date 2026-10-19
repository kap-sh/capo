"""Generated from Smithy shape ``com.amazonaws.iot#ListPolicyPrincipalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.marker
    import capo_iot.types.page_size
    import capo_iot.types.policy_name


class ListPolicyPrincipalsRequest(TypedDict, closed=True):
    policy_name: "capo_iot.types.policy_name.PolicyName"
    """<p>The policy name.</p>"""
    marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    page_size: NotRequired["capo_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p>Specifies the order for results. If true, the results are returned in ascending creation order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyPrincipalsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyPrincipalsRequest:
    out: ListPolicyPrincipalsRequest = {}  # type: ignore[typeddict-item]
    return out
