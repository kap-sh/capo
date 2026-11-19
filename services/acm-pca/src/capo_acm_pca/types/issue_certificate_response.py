"""Generated from Smithy shape ``com.amazonaws.acmpca#IssueCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.arn


class IssueCertificateResponse(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_acm_pca.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the issued certificate and the certificate serial number. This is of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i>/certificate/<i>286535153982981100925020015808220737245</i> </code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IssueCertificateResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IssueCertificateResponse:
    out: IssueCertificateResponse = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IssueCertificateResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_cbor(data: dict) -> IssueCertificateResponse:
    out: IssueCertificateResponse = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    return out
