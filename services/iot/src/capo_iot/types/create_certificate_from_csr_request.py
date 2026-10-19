"""Generated from Smithy shape ``com.amazonaws.iot#CreateCertificateFromCsrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.certificate_signing_request
    import capo_iot.types.set_as_active


class CreateCertificateFromCsrRequest(TypedDict, closed=True):
    certificate_signing_request: (
        "capo_iot.types.certificate_signing_request.CertificateSigningRequest"
    )
    """<p>The certificate signing request (CSR).</p>"""
    set_as_active: NotRequired["capo_iot.types.set_as_active.SetAsActive"]
    """<p>Specifies whether the certificate is active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCertificateFromCsrRequest) -> dict:
    out: dict = {}
    out["certificateSigningRequest"] = value["certificate_signing_request"]
    return out


def deserialize_json(data: dict) -> CreateCertificateFromCsrRequest:
    out: CreateCertificateFromCsrRequest = {}  # type: ignore[typeddict-item]
    if data.get("certificateSigningRequest") is not None:
        out["certificate_signing_request"] = data["certificateSigningRequest"]
    else:
        raise DeserializationError(
            "CreateCertificateFromCsrRequest.certificate_signing_request required"
        )
    return out
