"""Generated from Smithy shape ``com.amazonaws.iot#ListAuthorizersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.authorizer_status
    import capo_iot.types.marker
    import capo_iot.types.page_size


class ListAuthorizersRequest(TypedDict, closed=True):
    page_size: NotRequired["capo_iot.types.page_size.PageSize"]
    """<p>The maximum number of results to return at one time.</p>"""
    marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>A marker used to get the next set of results.</p>"""
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p>Return the list of authorizers in ascending alphabetical order.</p>"""
    status: NotRequired["capo_iot.types.authorizer_status.AuthorizerStatus"]
    """<p>The status of the list authorizers request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuthorizersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAuthorizersRequest:
    out: ListAuthorizersRequest = {}  # type: ignore[typeddict-item]
    return out
