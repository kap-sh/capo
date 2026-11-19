"""Generated from Smithy shape ``com.amazonaws.acmpca#GetCertificateAuthorityCsrResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.csr_body


class GetCertificateAuthorityCsrResponse(TypedDict, closed=True):
    csr: NotRequired["capo_acm_pca.types.csr_body.CsrBody"]
    """<p>The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCertificateAuthorityCsrResponse) -> dict:
    out: dict = {}
    if "csr" in value:
        out["Csr"] = value["csr"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCertificateAuthorityCsrResponse:
    out: GetCertificateAuthorityCsrResponse = {}  # type: ignore[typeddict-item]
    if data.get("Csr") is not None:
        out["csr"] = data["Csr"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCertificateAuthorityCsrResponse) -> dict:
    out: dict = {}
    if "csr" in value:
        out["Csr"] = value["csr"]
    return out


def deserialize_cbor(data: dict) -> GetCertificateAuthorityCsrResponse:
    out: GetCertificateAuthorityCsrResponse = {}  # type: ignore[typeddict-item]
    if data.get("Csr") is not None:
        out["csr"] = data["Csr"]
    return out
