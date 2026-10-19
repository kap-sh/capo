"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetCertificateSigningRequestOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_signing_request_type


class GetCertificateSigningRequestOutput(TypedDict, closed=True):
    certificate_signing_request: "capo_payment_cryptography.types.certificate_signing_request_type.CertificateSigningRequestType"
    """<p>The certificate signing request generated using the key pair associated with the key identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCertificateSigningRequestOutput) -> dict:
    out: dict = {}
    out["CertificateSigningRequest"] = value["certificate_signing_request"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCertificateSigningRequestOutput:
    out: GetCertificateSigningRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("CertificateSigningRequest") is not None:
        out["certificate_signing_request"] = data["CertificateSigningRequest"]
    else:
        out["certificate_signing_request"] = ""
    return out


def redact_sensitive(value: GetCertificateSigningRequestOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "certificate_signing_request" in value:
        out["certificate_signing_request"] = "*** Sensitive Data Redacted ***"
    return out
