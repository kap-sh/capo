"""Generated from Smithy shape ``com.amazonaws.acmpca#UpdateCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.certificate_authority_status
    import capo_acm_pca.types.revocation_configuration


class UpdateCertificateAuthorityRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>"""
    revocation_configuration: NotRequired[
        "capo_acm_pca.types.revocation_configuration.RevocationConfiguration"
    ]
    """<p>Contains information to enable support for Online Certificate Status Protocol (OCSP), certificate revocation list (CRL), both protocols, or neither. If you don't supply this parameter, existing capibilites remain unchanged. For more information, see the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_OcspConfiguration.html">OcspConfiguration</a> and <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html">CrlConfiguration</a> types.</p> <p>The following requirements apply to revocation configurations.</p> <ul> <li> <p>A configuration disabling CRLs or OCSP must contain only the <code>Enabled=False</code> parameter, and will fail if other parameters such as <code>CustomCname</code> or <code>ExpirationInDays</code> are included.</p> </li> <li> <p>In a CRL configuration, the <code>S3BucketName</code> parameter must conform to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html">Amazon S3 bucket naming rules</a>.</p> </li> <li> <p>A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to <a href="https://www.ietf.org/rfc/rfc2396.txt">RFC2396</a> restrictions on the use of special characters in a CNAME. </p> </li> <li> <p>In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".</p> </li> </ul> <important> <p> If you update the <code>S3BucketName</code> of <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html">CrlConfiguration</a>, you can break revocation for existing certificates. In other words, if you call <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html">UpdateCertificateAuthority</a> to update the CRL configuration's S3 bucket name, Amazon Web Services Private CA only writes CRLs to the new S3 bucket. Certificates issued prior to this point will have the old S3 bucket name in your CRL Distribution Point (CDP) extension, essentially breaking revocation. If you must update the S3 bucket, you'll need to reissue old certificates to keep the revocation working. Alternatively, you can use a <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html#privateca-Type-CrlConfiguration-CustomCname">CustomCname</a> in your CRL configuration if you might need to change the S3 bucket name in the future.</p> </important>"""
    status: NotRequired[
        "capo_acm_pca.types.certificate_authority_status.CertificateAuthorityStatus"
    ]
    """<p>Status of your private CA.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCertificateAuthorityRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "revocation_configuration" in value:
        import capo_acm_pca.types.revocation_configuration

        out["RevocationConfiguration"] = (
            capo_acm_pca.types.revocation_configuration.serialize_aws_json_1_1(
                value["revocation_configuration"]
            )
        )
    if "status" in value:
        import capo_acm_pca.types.certificate_authority_status

        out["Status"] = (
            capo_acm_pca.types.certificate_authority_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCertificateAuthorityRequest:
    out: UpdateCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "UpdateCertificateAuthorityRequest.certificate_authority_arn required"
        )
    if data.get("RevocationConfiguration") is not None:
        import capo_acm_pca.types.revocation_configuration

        out["revocation_configuration"] = (
            capo_acm_pca.types.revocation_configuration.deserialize_aws_json_1_1(
                data["RevocationConfiguration"]
            )
        )
    if data.get("Status") is not None:
        import capo_acm_pca.types.certificate_authority_status

        out["status"] = (
            capo_acm_pca.types.certificate_authority_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
