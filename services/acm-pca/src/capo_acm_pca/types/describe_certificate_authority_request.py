"""Generated from Smithy shape ``com.amazonaws.acmpca#DescribeCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.arn


class DescribeCertificateAuthorityRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateAuthorityRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateAuthorityRequest:
    out: DescribeCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "DescribeCertificateAuthorityRequest.certificate_authority_arn required"
        )
    return out
