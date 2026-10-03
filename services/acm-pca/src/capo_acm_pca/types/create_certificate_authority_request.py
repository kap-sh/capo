"""Generated from Smithy shape ``com.amazonaws.acmpca#CreateCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.certificate_authority_configuration
    import capo_acm_pca.types.certificate_authority_type
    import capo_acm_pca.types.certificate_authority_usage_mode
    import capo_acm_pca.types.idempotency_token
    import capo_acm_pca.types.key_storage_security_standard
    import capo_acm_pca.types.revocation_configuration
    import capo_acm_pca.types.tag_list


class CreateCertificateAuthorityRequest(TypedDict, closed=True):
    certificate_authority_configuration: "capo_acm_pca.types.certificate_authority_configuration.CertificateAuthorityConfiguration"
    """<p>Name and bit size of the private key algorithm, the name of the signing algorithm, and X.500 certificate subject information.</p>"""
    revocation_configuration: NotRequired[
        "capo_acm_pca.types.revocation_configuration.RevocationConfiguration"
    ]
    """<p>Contains information to enable support for Online Certificate Status Protocol (OCSP), certificate revocation list (CRL), both protocols, or neither. By default, both certificate validation mechanisms are disabled.</p> <p>The following requirements apply to revocation configurations.</p> <ul> <li> <p>A configuration disabling CRLs or OCSP must contain only the <code>Enabled=False</code> parameter, and will fail if other parameters such as <code>CustomCname</code> or <code>ExpirationInDays</code> are included.</p> </li> <li> <p>In a CRL configuration, the <code>S3BucketName</code> parameter must conform to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html">Amazon S3 bucket naming rules</a>.</p> </li> <li> <p>A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to <a href="https://www.ietf.org/rfc/rfc2396.txt">RFC2396</a> restrictions on the use of special characters in a CNAME. </p> </li> <li> <p>In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".</p> </li> </ul> <p> For more information, see the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_OcspConfiguration.html">OcspConfiguration</a> and <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html">CrlConfiguration</a> types.</p>"""
    certificate_authority_type: (
        "capo_acm_pca.types.certificate_authority_type.CertificateAuthorityType"
    )
    """<p>The type of the certificate authority.</p>"""
    idempotency_token: NotRequired[
        "capo_acm_pca.types.idempotency_token.IdempotencyToken"
    ]
    """<p>Custom string that can be used to distinguish between calls to the <b>CreateCertificateAuthority</b> action. Idempotency tokens for <b>CreateCertificateAuthority</b> time out after five minutes. Therefore, if you call <b>CreateCertificateAuthority</b> multiple times with the same idempotency token within five minutes, Amazon Web Services Private CA recognizes that you are requesting only certificate authority and will issue only one. If you change the idempotency token for each call, Amazon Web Services Private CA recognizes that you are requesting multiple certificate authorities.</p>"""
    key_storage_security_standard: NotRequired[
        "capo_acm_pca.types.key_storage_security_standard.KeyStorageSecurityStandard"
    ]
    """<p>Specifies a cryptographic key management compliance standard for handling and protecting CA keys.</p> <p>Default: FIPS_140_2_LEVEL_3_OR_HIGHER</p> <note> <p>Some Amazon Web Services Regions don't support the default value. When you create a CA in these Regions, you must use <code>CCPC_LEVEL_1_OR_HIGHER</code> for the <code>KeyStorageSecurityStandard</code> parameter. If you don't, the operation returns an <code>InvalidArgsException</code> with this message: "A certificate authority cannot be created in this region with the specified security standard."</p> <p>For information about security standard support in different Amazon Web Services Regions, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html#private-keys">Storage and security compliance of Amazon Web Services Private CA private keys</a>.</p> </note>"""
    tags: NotRequired["capo_acm_pca.types.tag_list.TagList"]
    """<p>Key-value pairs that will be attached to the new private CA. You can associate up to 50 tags with a private CA. For information using tags with IAM to manage permissions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html">Controlling Access Using IAM Tags</a>.</p>"""
    usage_mode: NotRequired[
        "capo_acm_pca.types.certificate_authority_usage_mode.CertificateAuthorityUsageMode"
    ]
    """<p>Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days.</p> <p>The default value is GENERAL_PURPOSE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCertificateAuthorityRequest) -> dict:
    out: dict = {}
    import capo_acm_pca.types.certificate_authority_configuration

    out["CertificateAuthorityConfiguration"] = (
        capo_acm_pca.types.certificate_authority_configuration.serialize_aws_json_1_1(
            value["certificate_authority_configuration"]
        )
    )
    if "revocation_configuration" in value:
        import capo_acm_pca.types.revocation_configuration

        out["RevocationConfiguration"] = (
            capo_acm_pca.types.revocation_configuration.serialize_aws_json_1_1(
                value["revocation_configuration"]
            )
        )
    import capo_acm_pca.types.certificate_authority_type

    out["CertificateAuthorityType"] = (
        capo_acm_pca.types.certificate_authority_type.serialize_aws_json_1_1(
            value["certificate_authority_type"]
        )
    )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "key_storage_security_standard" in value:
        import capo_acm_pca.types.key_storage_security_standard

        out["KeyStorageSecurityStandard"] = (
            capo_acm_pca.types.key_storage_security_standard.serialize_aws_json_1_1(
                value["key_storage_security_standard"]
            )
        )
    if "tags" in value:
        import capo_acm_pca.types.tag_list

        out["Tags"] = capo_acm_pca.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "usage_mode" in value:
        import capo_acm_pca.types.certificate_authority_usage_mode

        out["UsageMode"] = (
            capo_acm_pca.types.certificate_authority_usage_mode.serialize_aws_json_1_1(
                value["usage_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCertificateAuthorityRequest:
    out: CreateCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityConfiguration") is not None:
        import capo_acm_pca.types.certificate_authority_configuration

        out["certificate_authority_configuration"] = (
            capo_acm_pca.types.certificate_authority_configuration.deserialize_aws_json_1_1(
                data["CertificateAuthorityConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCertificateAuthorityRequest.certificate_authority_configuration required"
        )
    if data.get("RevocationConfiguration") is not None:
        import capo_acm_pca.types.revocation_configuration

        out["revocation_configuration"] = (
            capo_acm_pca.types.revocation_configuration.deserialize_aws_json_1_1(
                data["RevocationConfiguration"]
            )
        )
    if data.get("CertificateAuthorityType") is not None:
        import capo_acm_pca.types.certificate_authority_type

        out["certificate_authority_type"] = (
            capo_acm_pca.types.certificate_authority_type.deserialize_aws_json_1_1(
                data["CertificateAuthorityType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCertificateAuthorityRequest.certificate_authority_type required"
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("KeyStorageSecurityStandard") is not None:
        import capo_acm_pca.types.key_storage_security_standard

        out["key_storage_security_standard"] = (
            capo_acm_pca.types.key_storage_security_standard.deserialize_aws_json_1_1(
                data["KeyStorageSecurityStandard"]
            )
        )
    if data.get("Tags") is not None:
        import capo_acm_pca.types.tag_list

        out["tags"] = capo_acm_pca.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("UsageMode") is not None:
        import capo_acm_pca.types.certificate_authority_usage_mode

        out["usage_mode"] = (
            capo_acm_pca.types.certificate_authority_usage_mode.deserialize_aws_json_1_1(
                data["UsageMode"]
            )
        )
    return out
