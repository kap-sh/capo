"""Generated from Smithy shape ``com.amazonaws.iot#ListPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.marker
    import capo_iot.types.page_size


class ListPoliciesRequest(TypedDict, closed=True):
    marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    page_size: NotRequired["capo_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p>Specifies the order for results. If true, the results are returned in ascending creation order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPoliciesRequest:
    out: ListPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
