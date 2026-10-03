"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options
    import capo_securityhub.types.aws_certificate_manager_certificate_extended_key_usages
    import capo_securityhub.types.aws_certificate_manager_certificate_key_usages
    import capo_securityhub.types.aws_certificate_manager_certificate_options
    import capo_securityhub.types.aws_certificate_manager_certificate_renewal_summary
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class AwsCertificateManagerCertificateDetails(TypedDict, closed=True):
    certificate_authority_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the private certificate authority (CA) that will be used to issue the certificate.</p>"""
    created_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the certificate was requested.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    domain_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The fully qualified domain name (FQDN), such as www.example.com, that is secured by the certificate.</p>"""
    domain_validation_options: NotRequired[
        "capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options.AwsCertificateManagerCertificateDomainValidationOptions"
    ]
    """<p>Contains information about the initial validation of each domain name that occurs as a result of the <code>RequestCertificate</code> request.</p> <p>Only provided if the certificate type is <code>AMAZON_ISSUED</code>.</p>"""
    extended_key_usages: NotRequired[
        "capo_securityhub.types.aws_certificate_manager_certificate_extended_key_usages.AwsCertificateManagerCertificateExtendedKeyUsages"
    ]
    """<p>Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID).</p>"""
    failure_reason: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>For a failed certificate request, the reason for the failure.</p> <p>Valid values: <code>NO_AVAILABLE_CONTACTS</code> | <code>ADDITIONAL_VERIFICATION_REQUIRED</code> | <code>DOMAIN_NOT_ALLOWED</code> | <code>INVALID_PUBLIC_DOMAIN</code> | <code>DOMAIN_VALIDATION_DENIED</code> | <code>CAA_ERROR</code> | <code>PCA_LIMIT_EXCEEDED</code> | <code>PCA_INVALID_ARN</code> | <code>PCA_INVALID_STATE</code> | <code>PCA_REQUEST_FAILED</code> | <code>PCA_NAME_CONSTRAINTS_VALIDATION</code> | <code>PCA_RESOURCE_NOT_FOUND</code> | <code>PCA_INVALID_ARGS</code> | <code>PCA_INVALID_DURATION</code> | <code>PCA_ACCESS_DENIED</code> | <code>SLR_NOT_FOUND</code> | <code>OTHER</code> </p>"""
    imported_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the certificate was imported. Provided if the certificate type is <code>IMPORTED</code>.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    in_use_by: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The list of ARNs for the Amazon Web Services resources that use the certificate.</p>"""
    issued_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the certificate was issued. Provided if the certificate type is <code>AMAZON_ISSUED</code>.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    issuer: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the certificate authority that issued and signed the certificate.</p>"""
    key_algorithm: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The algorithm that was used to generate the public-private key pair.</p> <p>Valid values: <code>RSA_2048</code> | <code>RSA_1024</code> |<code> RSA_4096</code> | <code>EC_prime256v1</code> | <code>EC_secp384r1</code> | <code>EC_secp521r1</code> </p>"""
    key_usages: NotRequired[
        "capo_securityhub.types.aws_certificate_manager_certificate_key_usages.AwsCertificateManagerCertificateKeyUsages"
    ]
    """<p>A list of key usage X.509 v3 extension objects.</p>"""
    not_after: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The time after which the certificate becomes invalid.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    not_before: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The time before which the certificate is not valid.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    options: NotRequired[
        "capo_securityhub.types.aws_certificate_manager_certificate_options.AwsCertificateManagerCertificateOptions"
    ]
    """<p>Provides a value that specifies whether to add the certificate to a transparency log.</p>"""
    renewal_eligibility: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Whether the certificate is eligible for renewal.</p> <p>Valid values: <code>ELIGIBLE</code> | <code>INELIGIBLE</code> </p>"""
    renewal_summary: NotRequired[
        "capo_securityhub.types.aws_certificate_manager_certificate_renewal_summary.AwsCertificateManagerCertificateRenewalSummary"
    ]
    """<p>Information about the status of the Certificate Manager managed renewal for the certificate. Provided only when the certificate type is <code>AMAZON_ISSUED</code>.</p>"""
    serial: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The serial number of the certificate.</p>"""
    signature_algorithm: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The algorithm that was used to sign the certificate.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the certificate.</p> <p>Valid values: <code>PENDING_VALIDATION</code> | <code>ISSUED</code> | <code>INACTIVE</code> | <code>EXPIRED</code> | <code>VALIDATION_TIMED_OUT</code> | <code>REVOKED</code> | <code>FAILED</code> </p>"""
    subject: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the entity that is associated with the public key contained in the certificate.</p>"""
    subject_alternative_names: NotRequired[
        "capo_securityhub.types.string_list.StringList"
    ]
    """<p>One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate.</p> <p>The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.</p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source of the certificate. For certificates that Certificate Manager provides, <code>Type</code> is <code>AMAZON_ISSUED</code>. For certificates that are imported with <code>ImportCertificate</code>, <code>Type</code> is <code>IMPORTED</code>.</p> <p>Valid values: <code>IMPORTED</code> | <code>AMAZON_ISSUED</code> | <code>PRIVATE</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCertificateManagerCertificateDetails) -> dict:
    out: dict = {}
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "domain_validation_options" in value:
        import capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options

        out["DomainValidationOptions"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options.serialize_json(
                value["domain_validation_options"]
            )
        )
    if "extended_key_usages" in value:
        import capo_securityhub.types.aws_certificate_manager_certificate_extended_key_usages

        out["ExtendedKeyUsages"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_extended_key_usages.serialize_json(
                value["extended_key_usages"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "imported_at" in value:
        out["ImportedAt"] = value["imported_at"]
    if "in_use_by" in value:
        import capo_securityhub.types.string_list

        out["InUseBy"] = capo_securityhub.types.string_list.serialize_json(
            value["in_use_by"]
        )
    if "issued_at" in value:
        out["IssuedAt"] = value["issued_at"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    if "key_algorithm" in value:
        out["KeyAlgorithm"] = value["key_algorithm"]
    if "key_usages" in value:
        import capo_securityhub.types.aws_certificate_manager_certificate_key_usages

        out["KeyUsages"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_key_usages.serialize_json(
                value["key_usages"]
            )
        )
    if "not_after" in value:
        out["NotAfter"] = value["not_after"]
    if "not_before" in value:
        out["NotBefore"] = value["not_before"]
    if "options" in value:
        import capo_securityhub.types.aws_certificate_manager_certificate_options

        out["Options"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_options.serialize_json(
                value["options"]
            )
        )
    if "renewal_eligibility" in value:
        out["RenewalEligibility"] = value["renewal_eligibility"]
    if "renewal_summary" in value:
        import capo_securityhub.types.aws_certificate_manager_certificate_renewal_summary

        out["RenewalSummary"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_renewal_summary.serialize_json(
                value["renewal_summary"]
            )
        )
    if "serial" in value:
        out["Serial"] = value["serial"]
    if "signature_algorithm" in value:
        out["SignatureAlgorithm"] = value["signature_algorithm"]
    if "status" in value:
        out["Status"] = value["status"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "subject_alternative_names" in value:
        import capo_securityhub.types.string_list

        out["SubjectAlternativeNames"] = (
            capo_securityhub.types.string_list.serialize_json(
                value["subject_alternative_names"]
            )
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsCertificateManagerCertificateDetails:
    out: AwsCertificateManagerCertificateDetails = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if data.get("CreatedAt") is not None:
        out["created_at"] = data["CreatedAt"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("DomainValidationOptions") is not None:
        import capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options

        out["domain_validation_options"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options.deserialize_json(
                data["DomainValidationOptions"]
            )
        )
    if data.get("ExtendedKeyUsages") is not None:
        import capo_securityhub.types.aws_certificate_manager_certificate_extended_key_usages

        out["extended_key_usages"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_extended_key_usages.deserialize_json(
                data["ExtendedKeyUsages"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("ImportedAt") is not None:
        out["imported_at"] = data["ImportedAt"]
    if data.get("InUseBy") is not None:
        import capo_securityhub.types.string_list

        out["in_use_by"] = capo_securityhub.types.string_list.deserialize_json(
            data["InUseBy"]
        )
    if data.get("IssuedAt") is not None:
        out["issued_at"] = data["IssuedAt"]
    if data.get("Issuer") is not None:
        out["issuer"] = data["Issuer"]
    if data.get("KeyAlgorithm") is not None:
        out["key_algorithm"] = data["KeyAlgorithm"]
    if data.get("KeyUsages") is not None:
        import capo_securityhub.types.aws_certificate_manager_certificate_key_usages

        out["key_usages"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_key_usages.deserialize_json(
                data["KeyUsages"]
            )
        )
    if data.get("NotAfter") is not None:
        out["not_after"] = data["NotAfter"]
    if data.get("NotBefore") is not None:
        out["not_before"] = data["NotBefore"]
    if data.get("Options") is not None:
        import capo_securityhub.types.aws_certificate_manager_certificate_options

        out["options"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_options.deserialize_json(
                data["Options"]
            )
        )
    if data.get("RenewalEligibility") is not None:
        out["renewal_eligibility"] = data["RenewalEligibility"]
    if data.get("RenewalSummary") is not None:
        import capo_securityhub.types.aws_certificate_manager_certificate_renewal_summary

        out["renewal_summary"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_renewal_summary.deserialize_json(
                data["RenewalSummary"]
            )
        )
    if data.get("Serial") is not None:
        out["serial"] = data["Serial"]
    if data.get("SignatureAlgorithm") is not None:
        out["signature_algorithm"] = data["SignatureAlgorithm"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    if data.get("SubjectAlternativeNames") is not None:
        import capo_securityhub.types.string_list

        out["subject_alternative_names"] = (
            capo_securityhub.types.string_list.deserialize_json(
                data["SubjectAlternativeNames"]
            )
        )
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
