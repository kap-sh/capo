"""Generated from Smithy shape ``com.amazonaws.acmpca#ImportCertificateAuthorityCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.certificate_body_blob
    import capo_acm_pca.types.certificate_chain_blob


class ImportCertificateAuthorityCertificateRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>"""
    certificate: "capo_acm_pca.types.certificate_body_blob.CertificateBodyBlob"
    """<p>The PEM-encoded certificate for a private CA. This may be a self-signed certificate in the case of a root CA, or it may be signed by another CA that you control.</p>"""
    certificate_chain: NotRequired[
        "capo_acm_pca.types.certificate_chain_blob.CertificateChainBlob"
    ]
    """<p>A PEM-encoded file that contains all of your certificates, other than the certificate you're importing, chaining up to your root CA. Your Amazon Web Services Private CA-hosted or on-premises root certificate is the last in the chain, and each certificate in the chain signs the one preceding. </p> <p>This parameter must be supplied when you import a subordinate CA. When you import a root CA, there is no chain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCertificateAuthorityCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    import capo_acm_pca.types.certificate_body_blob

    out["Certificate"] = (
        capo_acm_pca.types.certificate_body_blob.serialize_aws_json_1_1(
            value["certificate"]
        )
    )
    if "certificate_chain" in value:
        import capo_acm_pca.types.certificate_chain_blob

        out["CertificateChain"] = (
            capo_acm_pca.types.certificate_chain_blob.serialize_aws_json_1_1(
                value["certificate_chain"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ImportCertificateAuthorityCertificateRequest:
    out: ImportCertificateAuthorityCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "ImportCertificateAuthorityCertificateRequest.certificate_authority_arn required"
        )
    if data.get("Certificate") is not None:
        import capo_acm_pca.types.certificate_body_blob

        out["certificate"] = (
            capo_acm_pca.types.certificate_body_blob.deserialize_aws_json_1_1(
                data["Certificate"]
            )
        )
    else:
        raise DeserializationError(
            "ImportCertificateAuthorityCertificateRequest.certificate required"
        )
    if data.get("CertificateChain") is not None:
        import capo_acm_pca.types.certificate_chain_blob

        out["certificate_chain"] = (
            capo_acm_pca.types.certificate_chain_blob.deserialize_aws_json_1_1(
                data["CertificateChain"]
            )
        )
    return out
