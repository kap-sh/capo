"""Generated from Smithy shape ``com.amazonaws.acmpca#CrlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.boolean
    import capo_acm_pca.types.cname_string
    import capo_acm_pca.types.crl_distribution_point_extension_configuration
    import capo_acm_pca.types.crl_path_string
    import capo_acm_pca.types.crl_type
    import capo_acm_pca.types.integer1_to5000
    import capo_acm_pca.types.s3_bucket_name3_to255
    import capo_acm_pca.types.s3_object_acl


class CrlConfiguration(TypedDict, closed=True):
    enabled: "capo_acm_pca.types.boolean.Boolean"
    """<p>Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action or for an existing CA when you call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html">UpdateCertificateAuthority</a> action. </p>"""
    expiration_in_days: NotRequired["capo_acm_pca.types.integer1_to5000.Integer1To5000"]
    """<p>Validity period of the CRL in days.</p>"""
    custom_cname: NotRequired["capo_acm_pca.types.cname_string.CnameString"]
    """<p>Name inserted into the certificate <b>CRL Distribution Points</b> extension that enables the use of an alias for the CRL distribution point. Use this value if you don't want the name of your S3 bucket to be public.</p> <note> <p>The content of a Canonical Name (CNAME) record must conform to <a href="https://www.ietf.org/rfc/rfc2396.txt">RFC2396</a> restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".</p> </note>"""
    s3_bucket_name: NotRequired[
        "capo_acm_pca.types.s3_bucket_name3_to255.S3BucketName3To255"
    ]
    """<p>Name of the S3 bucket that contains the CRL. If you do not provide a value for the <b>CustomCname</b> argument, the name of your S3 bucket is placed into the <b>CRL Distribution Points</b> extension of the issued certificate. You can change the name of your bucket by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html">UpdateCertificateAuthority</a> operation. You must specify a <a href="https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies">bucket policy</a> that allows Amazon Web Services Private CA to write the CRL to your bucket.</p> <note> <p>The <code>S3BucketName</code> parameter must conform to the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html">S3 bucket naming rules</a>.</p> </note>"""
    s3_object_acl: NotRequired["capo_acm_pca.types.s3_object_acl.S3ObjectAcl"]
    """<p>Determines whether the CRL will be publicly readable or privately held in the CRL Amazon S3 bucket. If you choose PUBLIC_READ, the CRL will be accessible over the public internet. If you choose BUCKET_OWNER_FULL_CONTROL, only the owner of the CRL S3 bucket can access the CRL, and your PKI clients may need an alternative method of access. </p> <p>If no value is specified, the default is <code>PUBLIC_READ</code>.</p> <p> <i>Note:</i> This default can cause CA creation to fail in some circumstances. If you have have enabled the Block Public Access (BPA) feature in your S3 account, then you must specify the value of this parameter as <code>BUCKET_OWNER_FULL_CONTROL</code>, and not doing so results in an error. If you have disabled BPA in S3, then you can specify either <code>BUCKET_OWNER_FULL_CONTROL</code> or <code>PUBLIC_READ</code> as the value.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-bpa">Blocking public access to the S3 bucket</a>.</p>"""
    crl_distribution_point_extension_configuration: NotRequired[
        "capo_acm_pca.types.crl_distribution_point_extension_configuration.CrlDistributionPointExtensionConfiguration"
    ]
    """<p>Configures the behavior of the CRL Distribution Point extension for certificates issued by your certificate authority. If this field is not provided, then the CRl Distribution Point Extension will be present and contain the default CRL URL.</p>"""
    crl_type: NotRequired["capo_acm_pca.types.crl_type.CrlType"]
    """<p>Specifies whether to create a complete or partitioned CRL. This setting determines the maximum number of certificates that the certificate authority can issue and revoke. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/pca.html#limits_pca">Amazon Web Services Private CA quotas</a>.</p> <ul> <li> <p> <code>COMPLETE</code> - The default setting. Amazon Web Services Private CA maintains a single CRL ﬁle for all unexpired certiﬁcates issued by a CA that have been revoked for any reason. Each certiﬁcate that Amazon Web Services Private CA issues is bound to a speciﬁc CRL through its CRL distribution point (CDP) extension, deﬁned in <a href="https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.9"> RFC 5280</a>.</p> </li> <li> <p> <code>PARTITIONED</code> - Compared to complete CRLs, partitioned CRLs dramatically increase the number of certiﬁcates your private CA can issue. </p> <important> <p> When using partitioned CRLs, you must validate that the CRL's associated issuing distribution point (IDP) URI matches the certiﬁcate's CDP URI to ensure the right CRL has been fetched. Amazon Web Services Private CA marks the IDP extension as critical, which your client must be able to process. </p> </important> </li> </ul>"""
    custom_path: NotRequired["capo_acm_pca.types.crl_path_string.CrlPathString"]
    """<p>Designates a custom ﬁle path in S3 for CRL(s). For example, <code>http://&lt;CustomName&gt;/ &lt;CustomPath&gt;/&lt;CrlPartition_GUID&gt;.crl</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrlConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "expiration_in_days" in value:
        out["ExpirationInDays"] = value["expiration_in_days"]
    if "custom_cname" in value:
        out["CustomCname"] = value["custom_cname"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_object_acl" in value:
        import capo_acm_pca.types.s3_object_acl

        out["S3ObjectAcl"] = capo_acm_pca.types.s3_object_acl.serialize_aws_json_1_1(
            value["s3_object_acl"]
        )
    if "crl_distribution_point_extension_configuration" in value:
        import capo_acm_pca.types.crl_distribution_point_extension_configuration

        out["CrlDistributionPointExtensionConfiguration"] = (
            capo_acm_pca.types.crl_distribution_point_extension_configuration.serialize_aws_json_1_1(
                value["crl_distribution_point_extension_configuration"]
            )
        )
    if "crl_type" in value:
        import capo_acm_pca.types.crl_type

        out["CrlType"] = capo_acm_pca.types.crl_type.serialize_aws_json_1_1(
            value["crl_type"]
        )
    if "custom_path" in value:
        out["CustomPath"] = value["custom_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CrlConfiguration:
    out: CrlConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("CrlConfiguration.enabled required")
    if data.get("ExpirationInDays") is not None:
        out["expiration_in_days"] = data["ExpirationInDays"]
    if data.get("CustomCname") is not None:
        out["custom_cname"] = data["CustomCname"]
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    if data.get("S3ObjectAcl") is not None:
        import capo_acm_pca.types.s3_object_acl

        out["s3_object_acl"] = (
            capo_acm_pca.types.s3_object_acl.deserialize_aws_json_1_1(
                data["S3ObjectAcl"]
            )
        )
    if data.get("CrlDistributionPointExtensionConfiguration") is not None:
        import capo_acm_pca.types.crl_distribution_point_extension_configuration

        out["crl_distribution_point_extension_configuration"] = (
            capo_acm_pca.types.crl_distribution_point_extension_configuration.deserialize_aws_json_1_1(
                data["CrlDistributionPointExtensionConfiguration"]
            )
        )
    if data.get("CrlType") is not None:
        import capo_acm_pca.types.crl_type

        out["crl_type"] = capo_acm_pca.types.crl_type.deserialize_aws_json_1_1(
            data["CrlType"]
        )
    if data.get("CustomPath") is not None:
        out["custom_path"] = data["CustomPath"]
    return out
