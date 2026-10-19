"""Generated from Smithy shape ``com.amazonaws.iot#AcceptCertificateTransferRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_id
    import capo_iot.types.set_as_active


class AcceptCertificateTransferRequest(TypedDict, closed=True):
    certificate_id: "capo_iot.types.certificate_id.CertificateId"
    """<p>The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)</p>"""
    set_as_active: NotRequired["capo_iot.types.set_as_active.SetAsActive"]
    """<p>Specifies whether the certificate is active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptCertificateTransferRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AcceptCertificateTransferRequest:
    out: AcceptCertificateTransferRequest = {}  # type: ignore[typeddict-item]
    return out
