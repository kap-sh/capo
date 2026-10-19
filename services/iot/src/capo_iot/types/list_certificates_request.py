"""Generated from Smithy shape ``com.amazonaws.iot#ListCertificatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.marker
    import capo_iot.types.page_size


class ListCertificatesRequest(TypedDict, closed=True):
    page_size: NotRequired["capo_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p>Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCertificatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCertificatesRequest:
    out: ListCertificatesRequest = {}  # type: ignore[typeddict-item]
    return out
