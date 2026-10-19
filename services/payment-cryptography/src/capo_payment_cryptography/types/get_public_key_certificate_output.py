"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetPublicKeyCertificateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_type


class GetPublicKeyCertificateOutput(TypedDict, closed=True):
    key_certificate: "capo_payment_cryptography.types.certificate_type.CertificateType"
    """<p>The public key component of the asymmetric key pair in a certificate PEM format (base64 encoded). It is signed by the root certificate authority (CA). The certificate is valid for 90 days from the time it is issued. The service returns a cached certificate if one exists with at least 30 days of remaining validity. Otherwise, a new 90-day certificate is issued.</p>"""
    key_certificate_chain: (
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The root certificate authority (CA) that signed the public key certificate in PEM format (base64 encoded) of the asymmetric key pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPublicKeyCertificateOutput) -> dict:
    out: dict = {}
    out["KeyCertificate"] = value["key_certificate"]
    out["KeyCertificateChain"] = value["key_certificate_chain"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPublicKeyCertificateOutput:
    out: GetPublicKeyCertificateOutput = {}  # type: ignore[typeddict-item]
    if data.get("KeyCertificate") is not None:
        out["key_certificate"] = data["KeyCertificate"]
    else:
        out["key_certificate"] = ""
    if data.get("KeyCertificateChain") is not None:
        out["key_certificate_chain"] = data["KeyCertificateChain"]
    else:
        out["key_certificate_chain"] = ""
    return out
