"""Generated from Smithy shape ``com.amazonaws.acm#CertificateDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_account_id
    import capo_acm.types.arn
    import capo_acm.types.certificate_key_pair_origin
    import capo_acm.types.certificate_managed_by
    import capo_acm.types.certificate_options
    import capo_acm.types.certificate_status
    import capo_acm.types.certificate_type
    import capo_acm.types.domain_list
    import capo_acm.types.domain_name_string
    import capo_acm.types.domain_validation_list
    import capo_acm.types.extended_key_usage_list
    import capo_acm.types.failure_reason
    import capo_acm.types.in_use_list
    import capo_acm.types.key_algorithm
    import capo_acm.types.key_usage_list
    import capo_acm.types.renewal_eligibility
    import capo_acm.types.renewal_summary
    import capo_acm.types.revocation_reason
    import capo_acm.types.string
    import capo_acm.types.t_stamp
    import capo_acm.types.update_summary


class CertificateDetail(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_acm.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    domain_name: NotRequired["capo_acm.types.domain_name_string.DomainNameString"]
    """<p>The fully qualified domain name for the certificate, such as www.example.com or example.com.</p>"""
    subject_alternative_names: NotRequired["capo_acm.types.domain_list.DomainList"]
    """<p>One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website. </p>"""
    managed_by: NotRequired[
        "capo_acm.types.certificate_managed_by.CertificateManagedBy"
    ]
    """<p>Identifies the Amazon Web Services service that manages the certificate issued by ACM.</p>"""
    domain_validation_options: NotRequired[
        "capo_acm.types.domain_validation_list.DomainValidationList"
    ]
    """<p>Contains information about the initial validation of each domain name that occurs as a result of the <a>RequestCertificate</a> request. This field exists only when the certificate type is <code>AMAZON_ISSUED</code>. </p>"""
    serial: NotRequired["capo_acm.types.string.String"]
    """<p>The serial number of the certificate.</p>"""
    subject: NotRequired["capo_acm.types.string.String"]
    """<p>The name of the entity that is associated with the public key contained in the certificate.</p>"""
    issuer: NotRequired["capo_acm.types.string.String"]
    """<p>The name of the certificate authority that issued and signed the certificate.</p>"""
    created_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was requested.</p>"""
    issued_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was issued. This value exists only when the certificate type is <code>AMAZON_ISSUED</code>. </p>"""
    imported_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The date and time when the certificate was imported. This value exists only when the certificate type is <code>IMPORTED</code>. </p>"""
    status: NotRequired["capo_acm.types.certificate_status.CertificateStatus"]
    """<p>The status of the certificate.</p> <p>A certificate enters status PENDING_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic <a href="https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html">Certificate request fails</a>. ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION_TIMED_OUT, delete the request, correct the issue with <a href="https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html">DNS validation</a> or <a href="https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html">Email validation</a>, and try again. If validation succeeds, the certificate enters status ISSUED. </p>"""
    revoked_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was revoked. This value exists only when the certificate status is <code>REVOKED</code>. </p>"""
    revocation_reason: NotRequired["capo_acm.types.revocation_reason.RevocationReason"]
    """<p>The reason the certificate was revoked. This value exists only when the certificate status is <code>REVOKED</code>. </p>"""
    not_before: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time before which the certificate is not valid.</p>"""
    not_after: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time after which the certificate is not valid.</p>"""
    key_algorithm: NotRequired["capo_acm.types.key_algorithm.KeyAlgorithm"]
    """<p>The algorithm that was used to generate the public-private key pair.</p>"""
    signature_algorithm: NotRequired["capo_acm.types.string.String"]
    """<p>The algorithm that was used to sign the certificate.</p>"""
    in_use_by: NotRequired["capo_acm.types.in_use_list.InUseList"]
    """<p>A list of ARNs for the Amazon Web Services resources that are using the certificate. A certificate can be used by multiple Amazon Web Services resources. </p>"""
    failure_reason: NotRequired["capo_acm.types.failure_reason.FailureReason"]
    """<p>The reason the certificate request failed. This value exists only when the certificate status is <code>FAILED</code>. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting.html#troubleshooting-failed">Certificate Request Failed</a> in the <i>Certificate Manager User Guide</i>. </p>"""
    type: NotRequired["capo_acm.types.certificate_type.CertificateType"]
    """<p>The source of the certificate. For certificates provided by ACM, this value is <code>AMAZON_ISSUED</code>. For certificates that you imported with <a>ImportCertificate</a>, this value is <code>IMPORTED</code>. ACM does not provide <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html">managed renewal</a> for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html">Importing Certificates</a> in the <i>Certificate Manager User Guide</i>. </p>"""
    renewal_summary: NotRequired["capo_acm.types.renewal_summary.RenewalSummary"]
    """<p>Contains information about the status of ACM's <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html">managed renewal</a> for the certificate. This field exists only when the certificate type is <code>AMAZON_ISSUED</code>.</p>"""
    key_usages: NotRequired["capo_acm.types.key_usage_list.KeyUsageList"]
    """<p>A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.</p>"""
    extended_key_usages: NotRequired[
        "capo_acm.types.extended_key_usage_list.ExtendedKeyUsageList"
    ]
    """<p>Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID). </p>"""
    certificate_authority_arn: NotRequired["capo_acm.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the private certificate authority (CA) that issued the certificate. This has the following format: </p> <p> <code>arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012</code> </p>"""
    renewal_eligibility: NotRequired[
        "capo_acm.types.renewal_eligibility.RenewalEligibility"
    ]
    """<p>Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the <a>RenewCertificate</a> command.</p>"""
    options: NotRequired["capo_acm.types.certificate_options.CertificateOptions"]
    """<p>Contains the certificate options. Certificate transparency logging opt-out is no longer available. All public certificates are recorded in a certificate transparency log.</p>"""
    update_summary: NotRequired["capo_acm.types.update_summary.UpdateSummary"]
    """<p>Contains information about the most recent update to the certificate. This field exists only when the certificate type is <code>AMAZON_ISSUED</code> and a certificate update has been requested.</p>"""
    certificate_key_pair_origin: NotRequired[
        "capo_acm.types.certificate_key_pair_origin.CertificateKeyPairOrigin"
    ]
    """<p>The origin of the certificate's key pair.</p>"""
    acme_endpoint_arn: NotRequired["capo_acm.types.arn.Arn"]
    """<p>The ARN of the ACME endpoint used to issue the certificate.</p>"""
    acme_account_id: NotRequired["capo_acm.types.acme_account_id.AcmeAccountId"]
    """<p>The ACME account identifier associated with the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateDetail) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "subject_alternative_names" in value:
        import capo_acm.types.domain_list

        out["SubjectAlternativeNames"] = (
            capo_acm.types.domain_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "managed_by" in value:
        import capo_acm.types.certificate_managed_by

        out["ManagedBy"] = capo_acm.types.certificate_managed_by.serialize_aws_json_1_1(
            value["managed_by"]
        )
    if "domain_validation_options" in value:
        import capo_acm.types.domain_validation_list

        out["DomainValidationOptions"] = (
            capo_acm.types.domain_validation_list.serialize_aws_json_1_1(
                value["domain_validation_options"]
            )
        )
    if "serial" in value:
        out["Serial"] = value["serial"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
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
    if "status" in value:
        import capo_acm.types.certificate_status

        out["Status"] = capo_acm.types.certificate_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "revoked_at" in value:
        import capo_acm.types.t_stamp

        out["RevokedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["revoked_at"]
        )
    if "revocation_reason" in value:
        import capo_acm.types.revocation_reason

        out["RevocationReason"] = (
            capo_acm.types.revocation_reason.serialize_aws_json_1_1(
                value["revocation_reason"]
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
    if "key_algorithm" in value:
        import capo_acm.types.key_algorithm

        out["KeyAlgorithm"] = capo_acm.types.key_algorithm.serialize_aws_json_1_1(
            value["key_algorithm"]
        )
    if "signature_algorithm" in value:
        out["SignatureAlgorithm"] = value["signature_algorithm"]
    if "in_use_by" in value:
        import capo_acm.types.in_use_list

        out["InUseBy"] = capo_acm.types.in_use_list.serialize_aws_json_1_1(
            value["in_use_by"]
        )
    if "failure_reason" in value:
        import capo_acm.types.failure_reason

        out["FailureReason"] = capo_acm.types.failure_reason.serialize_aws_json_1_1(
            value["failure_reason"]
        )
    if "type" in value:
        import capo_acm.types.certificate_type

        out["Type"] = capo_acm.types.certificate_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "renewal_summary" in value:
        import capo_acm.types.renewal_summary

        out["RenewalSummary"] = capo_acm.types.renewal_summary.serialize_aws_json_1_1(
            value["renewal_summary"]
        )
    if "key_usages" in value:
        import capo_acm.types.key_usage_list

        out["KeyUsages"] = capo_acm.types.key_usage_list.serialize_aws_json_1_1(
            value["key_usages"]
        )
    if "extended_key_usages" in value:
        import capo_acm.types.extended_key_usage_list

        out["ExtendedKeyUsages"] = (
            capo_acm.types.extended_key_usage_list.serialize_aws_json_1_1(
                value["extended_key_usages"]
            )
        )
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "renewal_eligibility" in value:
        import capo_acm.types.renewal_eligibility

        out["RenewalEligibility"] = (
            capo_acm.types.renewal_eligibility.serialize_aws_json_1_1(
                value["renewal_eligibility"]
            )
        )
    if "options" in value:
        import capo_acm.types.certificate_options

        out["Options"] = capo_acm.types.certificate_options.serialize_aws_json_1_1(
            value["options"]
        )
    if "update_summary" in value:
        import capo_acm.types.update_summary

        out["UpdateSummary"] = capo_acm.types.update_summary.serialize_aws_json_1_1(
            value["update_summary"]
        )
    if "certificate_key_pair_origin" in value:
        import capo_acm.types.certificate_key_pair_origin

        out["CertificateKeyPairOrigin"] = (
            capo_acm.types.certificate_key_pair_origin.serialize_aws_json_1_1(
                value["certificate_key_pair_origin"]
            )
        )
    if "acme_endpoint_arn" in value:
        out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    if "acme_account_id" in value:
        out["AcmeAccountId"] = value["acme_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateDetail:
    out: CertificateDetail = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("SubjectAlternativeNames") is not None:
        import capo_acm.types.domain_list

        out["subject_alternative_names"] = (
            capo_acm.types.domain_list.deserialize_aws_json_1_1(
                data["SubjectAlternativeNames"]
            )
        )
    if data.get("ManagedBy") is not None:
        import capo_acm.types.certificate_managed_by

        out["managed_by"] = (
            capo_acm.types.certificate_managed_by.deserialize_aws_json_1_1(
                data["ManagedBy"]
            )
        )
    if data.get("DomainValidationOptions") is not None:
        import capo_acm.types.domain_validation_list

        out["domain_validation_options"] = (
            capo_acm.types.domain_validation_list.deserialize_aws_json_1_1(
                data["DomainValidationOptions"]
            )
        )
    if data.get("Serial") is not None:
        out["serial"] = data["Serial"]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    if data.get("Issuer") is not None:
        out["issuer"] = data["Issuer"]
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
    if data.get("Status") is not None:
        import capo_acm.types.certificate_status

        out["status"] = capo_acm.types.certificate_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("RevokedAt") is not None:
        import capo_acm.types.t_stamp

        out["revoked_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["RevokedAt"]
        )
    if data.get("RevocationReason") is not None:
        import capo_acm.types.revocation_reason

        out["revocation_reason"] = (
            capo_acm.types.revocation_reason.deserialize_aws_json_1_1(
                data["RevocationReason"]
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
    if data.get("KeyAlgorithm") is not None:
        import capo_acm.types.key_algorithm

        out["key_algorithm"] = capo_acm.types.key_algorithm.deserialize_aws_json_1_1(
            data["KeyAlgorithm"]
        )
    if data.get("SignatureAlgorithm") is not None:
        out["signature_algorithm"] = data["SignatureAlgorithm"]
    if data.get("InUseBy") is not None:
        import capo_acm.types.in_use_list

        out["in_use_by"] = capo_acm.types.in_use_list.deserialize_aws_json_1_1(
            data["InUseBy"]
        )
    if data.get("FailureReason") is not None:
        import capo_acm.types.failure_reason

        out["failure_reason"] = capo_acm.types.failure_reason.deserialize_aws_json_1_1(
            data["FailureReason"]
        )
    if data.get("Type") is not None:
        import capo_acm.types.certificate_type

        out["type"] = capo_acm.types.certificate_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("RenewalSummary") is not None:
        import capo_acm.types.renewal_summary

        out["renewal_summary"] = (
            capo_acm.types.renewal_summary.deserialize_aws_json_1_1(
                data["RenewalSummary"]
            )
        )
    if data.get("KeyUsages") is not None:
        import capo_acm.types.key_usage_list

        out["key_usages"] = capo_acm.types.key_usage_list.deserialize_aws_json_1_1(
            data["KeyUsages"]
        )
    if data.get("ExtendedKeyUsages") is not None:
        import capo_acm.types.extended_key_usage_list

        out["extended_key_usages"] = (
            capo_acm.types.extended_key_usage_list.deserialize_aws_json_1_1(
                data["ExtendedKeyUsages"]
            )
        )
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if data.get("RenewalEligibility") is not None:
        import capo_acm.types.renewal_eligibility

        out["renewal_eligibility"] = (
            capo_acm.types.renewal_eligibility.deserialize_aws_json_1_1(
                data["RenewalEligibility"]
            )
        )
    if data.get("Options") is not None:
        import capo_acm.types.certificate_options

        out["options"] = capo_acm.types.certificate_options.deserialize_aws_json_1_1(
            data["Options"]
        )
    if data.get("UpdateSummary") is not None:
        import capo_acm.types.update_summary

        out["update_summary"] = capo_acm.types.update_summary.deserialize_aws_json_1_1(
            data["UpdateSummary"]
        )
    if data.get("CertificateKeyPairOrigin") is not None:
        import capo_acm.types.certificate_key_pair_origin

        out["certificate_key_pair_origin"] = (
            capo_acm.types.certificate_key_pair_origin.deserialize_aws_json_1_1(
                data["CertificateKeyPairOrigin"]
            )
        )
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    if data.get("AcmeAccountId") is not None:
        out["acme_account_id"] = data["AcmeAccountId"]
    return out
