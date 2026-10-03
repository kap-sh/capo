"""Generated from Smithy shape ``com.amazonaws.acm#CertificateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.certificate_export
    import capo_acm.types.certificate_key_pair_origin
    import capo_acm.types.certificate_managed_by
    import capo_acm.types.certificate_status
    import capo_acm.types.certificate_type
    import capo_acm.types.domain_list
    import capo_acm.types.domain_name_string
    import capo_acm.types.extended_key_usage_names
    import capo_acm.types.key_algorithm
    import capo_acm.types.key_usage_names
    import capo_acm.types.nullable_boolean
    import capo_acm.types.renewal_eligibility
    import capo_acm.types.t_stamp


class CertificateSummary(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_acm.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the certificate. This is of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>"""
    domain_name: NotRequired["capo_acm.types.domain_name_string.DomainNameString"]
    """<p>Fully qualified domain name (FQDN), such as www.example.com or example.com, for the certificate.</p>"""
    subject_alternative_name_summaries: NotRequired[
        "capo_acm.types.domain_list.DomainList"
    ]
    """<p>One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website. </p> <p>When called by <a href="https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html">ListCertificates</a>, this parameter will only return the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use <a href="https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html">DescribeCertificate</a>.</p>"""
    has_additional_subject_alternative_names: NotRequired[
        "capo_acm.types.nullable_boolean.NullableBoolean"
    ]
    """<p>When called by <a href="https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html">ListCertificates</a>, indicates whether the full list of subject alternative names has been included in the response. If false, the response includes all of the subject alternative names included in the certificate. If true, the response only includes the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use <a href="https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html">DescribeCertificate</a>.</p>"""
    status: NotRequired["capo_acm.types.certificate_status.CertificateStatus"]
    """<p>The status of the certificate.</p> <p>A certificate enters status PENDING_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic <a href="https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html">Certificate request fails</a>. ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION_TIMED_OUT, delete the request, correct the issue with <a href="https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html">DNS validation</a> or <a href="https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html">Email validation</a>, and try again. If validation succeeds, the certificate enters status ISSUED. </p>"""
    type: NotRequired["capo_acm.types.certificate_type.CertificateType"]
    """<p>The source of the certificate. For certificates provided by ACM, this value is <code>AMAZON_ISSUED</code>. For certificates that you imported with <a>ImportCertificate</a>, this value is <code>IMPORTED</code>. ACM does not provide <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html">managed renewal</a> for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html">Importing Certificates</a> in the <i>Certificate Manager User Guide</i>. </p>"""
    key_algorithm: NotRequired["capo_acm.types.key_algorithm.KeyAlgorithm"]
    """<p>The algorithm that was used to generate the public-private key pair.</p>"""
    key_usages: NotRequired["capo_acm.types.key_usage_names.KeyUsageNames"]
    """<p>A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.</p>"""
    extended_key_usages: NotRequired[
        "capo_acm.types.extended_key_usage_names.ExtendedKeyUsageNames"
    ]
    """<p>Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID). </p>"""
    export_option: NotRequired["capo_acm.types.certificate_export.CertificateExport"]
    """<p>Indicates if export is enabled for the certificate.</p>"""
    in_use: NotRequired["capo_acm.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether the certificate is currently in use by any Amazon Web Services resources.</p>"""
    exported: NotRequired["capo_acm.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether the certificate has been exported.</p>"""
    renewal_eligibility: NotRequired[
        "capo_acm.types.renewal_eligibility.RenewalEligibility"
    ]
    """<p>Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the <a>RenewCertificate</a> command.</p>"""
    not_before: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time before which the certificate is not valid.</p>"""
    not_after: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time after which the certificate is not valid.</p>"""
    created_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was requested.</p>"""
    issued_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was issued. This value exists only when the certificate type is <code>AMAZON_ISSUED</code>. </p>"""
    imported_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The date and time when the certificate was imported. This value exists only when the certificate type is <code>IMPORTED</code>. </p>"""
    revoked_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was revoked. This value exists only when the certificate status is <code>REVOKED</code>. </p>"""
    managed_by: NotRequired[
        "capo_acm.types.certificate_managed_by.CertificateManagedBy"
    ]
    """<p>Identifies the Amazon Web Services service that manages the certificate issued by ACM.</p>"""
    certificate_key_pair_origin: NotRequired[
        "capo_acm.types.certificate_key_pair_origin.CertificateKeyPairOrigin"
    ]
    """<p>The origin of the certificate's key pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateSummary) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "subject_alternative_name_summaries" in value:
        import capo_acm.types.domain_list

        out["SubjectAlternativeNameSummaries"] = (
            capo_acm.types.domain_list.serialize_aws_json_1_1(
                value["subject_alternative_name_summaries"]
            )
        )
    if "has_additional_subject_alternative_names" in value:
        out["HasAdditionalSubjectAlternativeNames"] = value[
            "has_additional_subject_alternative_names"
        ]
    if "status" in value:
        import capo_acm.types.certificate_status

        out["Status"] = capo_acm.types.certificate_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "type" in value:
        import capo_acm.types.certificate_type

        out["Type"] = capo_acm.types.certificate_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "key_algorithm" in value:
        import capo_acm.types.key_algorithm

        out["KeyAlgorithm"] = capo_acm.types.key_algorithm.serialize_aws_json_1_1(
            value["key_algorithm"]
        )
    if "key_usages" in value:
        import capo_acm.types.key_usage_names

        out["KeyUsages"] = capo_acm.types.key_usage_names.serialize_aws_json_1_1(
            value["key_usages"]
        )
    if "extended_key_usages" in value:
        import capo_acm.types.extended_key_usage_names

        out["ExtendedKeyUsages"] = (
            capo_acm.types.extended_key_usage_names.serialize_aws_json_1_1(
                value["extended_key_usages"]
            )
        )
    if "export_option" in value:
        import capo_acm.types.certificate_export

        out["ExportOption"] = capo_acm.types.certificate_export.serialize_aws_json_1_1(
            value["export_option"]
        )
    if "in_use" in value:
        out["InUse"] = value["in_use"]
    if "exported" in value:
        out["Exported"] = value["exported"]
    if "renewal_eligibility" in value:
        import capo_acm.types.renewal_eligibility

        out["RenewalEligibility"] = (
            capo_acm.types.renewal_eligibility.serialize_aws_json_1_1(
                value["renewal_eligibility"]
            )
        )
    if "not_before" in value:
        import capo_acm.types.t_stamp

        out["NotBefore"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["not_before"]
        )
    if "not_after" in value:
        import capo_acm.types.t_stamp

        out["NotAfter"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["not_after"]
        )
    if "created_at" in value:
        import capo_acm.types.t_stamp

        out["CreatedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "issued_at" in value:
        import capo_acm.types.t_stamp

        out["IssuedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["issued_at"]
        )
    if "imported_at" in value:
        import capo_acm.types.t_stamp

        out["ImportedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["imported_at"]
        )
    if "revoked_at" in value:
        import capo_acm.types.t_stamp

        out["RevokedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["revoked_at"]
        )
    if "managed_by" in value:
        import capo_acm.types.certificate_managed_by

        out["ManagedBy"] = capo_acm.types.certificate_managed_by.serialize_aws_json_1_1(
            value["managed_by"]
        )
    if "certificate_key_pair_origin" in value:
        import capo_acm.types.certificate_key_pair_origin

        out["CertificateKeyPairOrigin"] = (
            capo_acm.types.certificate_key_pair_origin.serialize_aws_json_1_1(
                value["certificate_key_pair_origin"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateSummary:
    out: CertificateSummary = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("SubjectAlternativeNameSummaries") is not None:
        import capo_acm.types.domain_list

        out["subject_alternative_name_summaries"] = (
            capo_acm.types.domain_list.deserialize_aws_json_1_1(
                data["SubjectAlternativeNameSummaries"]
            )
        )
    if data.get("HasAdditionalSubjectAlternativeNames") is not None:
        out["has_additional_subject_alternative_names"] = data[
            "HasAdditionalSubjectAlternativeNames"
        ]
    if data.get("Status") is not None:
        import capo_acm.types.certificate_status

        out["status"] = capo_acm.types.certificate_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Type") is not None:
        import capo_acm.types.certificate_type

        out["type"] = capo_acm.types.certificate_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("KeyAlgorithm") is not None:
        import capo_acm.types.key_algorithm

        out["key_algorithm"] = capo_acm.types.key_algorithm.deserialize_aws_json_1_1(
            data["KeyAlgorithm"]
        )
    if data.get("KeyUsages") is not None:
        import capo_acm.types.key_usage_names

        out["key_usages"] = capo_acm.types.key_usage_names.deserialize_aws_json_1_1(
            data["KeyUsages"]
        )
    if data.get("ExtendedKeyUsages") is not None:
        import capo_acm.types.extended_key_usage_names

        out["extended_key_usages"] = (
            capo_acm.types.extended_key_usage_names.deserialize_aws_json_1_1(
                data["ExtendedKeyUsages"]
            )
        )
    if data.get("ExportOption") is not None:
        import capo_acm.types.certificate_export

        out["export_option"] = (
            capo_acm.types.certificate_export.deserialize_aws_json_1_1(
                data["ExportOption"]
            )
        )
    if data.get("InUse") is not None:
        out["in_use"] = data["InUse"]
    if data.get("Exported") is not None:
        out["exported"] = data["Exported"]
    if data.get("RenewalEligibility") is not None:
        import capo_acm.types.renewal_eligibility

        out["renewal_eligibility"] = (
            capo_acm.types.renewal_eligibility.deserialize_aws_json_1_1(
                data["RenewalEligibility"]
            )
        )
    if data.get("NotBefore") is not None:
        import capo_acm.types.t_stamp

        out["not_before"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["NotBefore"]
        )
    if data.get("NotAfter") is not None:
        import capo_acm.types.t_stamp

        out["not_after"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["NotAfter"]
        )
    if data.get("CreatedAt") is not None:
        import capo_acm.types.t_stamp

        out["created_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("IssuedAt") is not None:
        import capo_acm.types.t_stamp

        out["issued_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["IssuedAt"]
        )
    if data.get("ImportedAt") is not None:
        import capo_acm.types.t_stamp

        out["imported_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["ImportedAt"]
        )
    if data.get("RevokedAt") is not None:
        import capo_acm.types.t_stamp

        out["revoked_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["RevokedAt"]
        )
    if data.get("ManagedBy") is not None:
        import capo_acm.types.certificate_managed_by

        out["managed_by"] = (
            capo_acm.types.certificate_managed_by.deserialize_aws_json_1_1(
                data["ManagedBy"]
            )
        )
    if data.get("CertificateKeyPairOrigin") is not None:
        import capo_acm.types.certificate_key_pair_origin

        out["certificate_key_pair_origin"] = (
            capo_acm.types.certificate_key_pair_origin.deserialize_aws_json_1_1(
                data["CertificateKeyPairOrigin"]
            )
        )
    return out
