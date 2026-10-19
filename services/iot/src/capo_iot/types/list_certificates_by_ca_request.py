"""Generated from Smithy shape ``com.amazonaws.iot#ListCertificatesByCARequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.certificate_id
    import capo_iot.types.marker
    import capo_iot.types.page_size


class ListCertificatesByCARequest(TypedDict, closed=True):
    ca_certificate_id: "capo_iot.types.certificate_id.CertificateId"
    """<p>The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.</p>"""
    page_size: NotRequired["capo_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p>Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCertificatesByCARequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCertificatesByCARequest:
    out: ListCertificatesByCARequest = {}  # type: ignore[typeddict-item]
    return out
