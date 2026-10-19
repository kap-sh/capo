"""Generated from Smithy shape ``com.amazonaws.iot#ListCACertificatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.marker
    import capo_iot.types.page_size
    import capo_iot.types.template_name


class ListCACertificatesRequest(TypedDict, closed=True):
    page_size: NotRequired["capo_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p>Determines the order of the results.</p>"""
    template_name: NotRequired["capo_iot.types.template_name.TemplateName"]
    """<p>The name of the provisioning template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCACertificatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCACertificatesRequest:
    out: ListCACertificatesRequest = {}  # type: ignore[typeddict-item]
    return out
