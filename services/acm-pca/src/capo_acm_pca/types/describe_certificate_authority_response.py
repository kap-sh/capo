"""Generated from Smithy shape ``com.amazonaws.acmpca#DescribeCertificateAuthorityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.certificate_authority


class DescribeCertificateAuthorityResponse(TypedDict, closed=True):
    certificate_authority: NotRequired[
        "capo_acm_pca.types.certificate_authority.CertificateAuthority"
    ]
    """<p>A <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CertificateAuthority.html">CertificateAuthority</a> structure that contains information about your private CA.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateAuthorityResponse) -> dict:
    out: dict = {}
    if "certificate_authority" in value:
        import capo_acm_pca.types.certificate_authority

        out["CertificateAuthority"] = (
            capo_acm_pca.types.certificate_authority.serialize_aws_json_1_1(
                value["certificate_authority"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateAuthorityResponse:
    out: DescribeCertificateAuthorityResponse = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthority") is not None:
        import capo_acm_pca.types.certificate_authority

        out["certificate_authority"] = (
            capo_acm_pca.types.certificate_authority.deserialize_aws_json_1_1(
                data["CertificateAuthority"]
            )
        )
    return out
