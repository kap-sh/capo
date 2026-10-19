"""Generated from Smithy shape ``com.amazonaws.iot#RegisterCertificateWithoutCARequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_pem
    import capo_iot.types.certificate_status


class RegisterCertificateWithoutCARequest(TypedDict, closed=True):
    certificate_pem: "capo_iot.types.certificate_pem.CertificatePem"
    """<p>The certificate data, in PEM format.</p>"""
    status: NotRequired["capo_iot.types.certificate_status.CertificateStatus"]
    """<p>The status of the register certificate request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCertificateWithoutCARequest) -> dict:
    out: dict = {}
    out["certificatePem"] = value["certificate_pem"]
    if "status" in value:
        import capo_iot.types.certificate_status

        out["status"] = capo_iot.types.certificate_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> RegisterCertificateWithoutCARequest:
    out: RegisterCertificateWithoutCARequest = {}  # type: ignore[typeddict-item]
    if data.get("certificatePem") is not None:
        out["certificate_pem"] = data["certificatePem"]
    else:
        out["certificate_pem"] = ""
    if data.get("status") is not None:
        import capo_iot.types.certificate_status

        out["status"] = capo_iot.types.certificate_status.deserialize_json(
            data["status"]
        )
    return out
