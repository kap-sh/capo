"""Generated from Smithy shape ``com.amazonaws.acmpca#GetCertificateAuthorityCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.certificate_body
    import capo_acm_pca.types.certificate_chain


class GetCertificateAuthorityCertificateResponse(TypedDict, closed=True):
    certificate: NotRequired["capo_acm_pca.types.certificate_body.CertificateBody"]
    """<p>Base64-encoded certificate authority (CA) certificate.</p>"""
    certificate_chain: NotRequired[
        "capo_acm_pca.types.certificate_chain.CertificateChain"
    ]
    """<p>Base64-encoded certificate chain that includes any intermediate certificates and chains up to root certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. If this is a root CA, the value will be null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCertificateAuthorityCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCertificateAuthorityCertificateResponse:
    out: GetCertificateAuthorityCertificateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Certificate") is not None:
        out["certificate"] = data["Certificate"]
    if data.get("CertificateChain") is not None:
        out["certificate_chain"] = data["CertificateChain"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCertificateAuthorityCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
    return out


def deserialize_cbor(data: dict) -> GetCertificateAuthorityCertificateResponse:
    out: GetCertificateAuthorityCertificateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Certificate") is not None:
        out["certificate"] = data["Certificate"]
    if data.get("CertificateChain") is not None:
        out["certificate_chain"] = data["CertificateChain"]
    return out
