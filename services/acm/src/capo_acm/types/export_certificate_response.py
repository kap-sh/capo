"""Generated from Smithy shape ``com.amazonaws.acm#ExportCertificateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.certificate_body
    import capo_acm.types.certificate_chain
    import capo_acm.types.private_key


class ExportCertificateResponse(TypedDict, closed=True):
    certificate: NotRequired["capo_acm.types.certificate_body.CertificateBody"]
    """<p>The base64 PEM-encoded certificate.</p>"""
    certificate_chain: NotRequired["capo_acm.types.certificate_chain.CertificateChain"]
    """<p>The base64 PEM-encoded certificate chain. This does not include the certificate that you are exporting.</p>"""
    private_key: NotRequired["capo_acm.types.private_key.PrivateKey"]
    """<p>The encrypted private key associated with the public key in the certificate. The key is output in PKCS #8 format and is base64 PEM-encoded. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
    if "private_key" in value:
        out["PrivateKey"] = value["private_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportCertificateResponse:
    out: ExportCertificateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Certificate") is not None:
        out["certificate"] = data["Certificate"]
    if data.get("CertificateChain") is not None:
        out["certificate_chain"] = data["CertificateChain"]
    if data.get("PrivateKey") is not None:
        out["private_key"] = data["PrivateKey"]
    return out


def redact_sensitive(value: ExportCertificateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "private_key" in value:
        out["private_key"] = "*** Sensitive Data Redacted ***"
    return out
