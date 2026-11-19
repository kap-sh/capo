"""Generated from Smithy shape ``com.amazonaws.acmpca#GetCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.certificate_body
    import capo_acm_pca.types.certificate_chain


class GetCertificateResponse(TypedDict, closed=True):
    certificate: NotRequired["capo_acm_pca.types.certificate_body.CertificateBody"]
    """<p>The base64 PEM-encoded certificate specified by the <code>CertificateArn</code> parameter.</p>"""
    certificate_chain: NotRequired[
        "capo_acm_pca.types.certificate_chain.CertificateChain"
    ]
    """<p>The base64 PEM-encoded certificate chain that chains up to the root CA certificate that you used to sign your private CA certificate. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCertificateResponse:
    out: GetCertificateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Certificate") is not None:
        out["certificate"] = data["Certificate"]
    if data.get("CertificateChain") is not None:
        out["certificate_chain"] = data["CertificateChain"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
    return out


def deserialize_cbor(data: dict) -> GetCertificateResponse:
    out: GetCertificateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Certificate") is not None:
        out["certificate"] = data["Certificate"]
    if data.get("CertificateChain") is not None:
        out["certificate_chain"] = data["CertificateChain"]
    return out
