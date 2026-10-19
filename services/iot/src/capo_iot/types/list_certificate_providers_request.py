"""Generated from Smithy shape ``com.amazonaws.iot#ListCertificateProvidersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.marker


class ListCertificateProvidersRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The token for the next set of results, or <code>null</code> if there are no more results.</p>"""
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p>Returns the list of certificate providers in ascending alphabetical order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCertificateProvidersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCertificateProvidersRequest:
    out: ListCertificateProvidersRequest = {}  # type: ignore[typeddict-item]
    return out
