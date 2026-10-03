"""Generated from Smithy shape ``com.amazonaws.acm#AcmCertificateMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_account_id
    import capo_acm.types.arn
    import capo_acm.types.certificate_export
    import capo_acm.types.certificate_key_pair_origin
    import capo_acm.types.certificate_managed_by
    import capo_acm.types.certificate_status
    import capo_acm.types.certificate_type
    import capo_acm.types.nullable_boolean
    import capo_acm.types.renewal_eligibility
    import capo_acm.types.renewal_status
    import capo_acm.types.t_stamp
    import capo_acm.types.validation_method


class AcmCertificateMetadata(TypedDict, closed=True):
    created_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was requested.</p>"""
    exported: NotRequired["capo_acm.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether the certificate has been exported.</p>"""
    imported_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The date and time when the certificate was imported. This value exists only when the certificate type is <code>IMPORTED</code>. </p>"""
    in_use: NotRequired["capo_acm.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether the certificate is currently in use by an Amazon Web Services service.</p>"""
    issued_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was issued. This value exists only when the certificate type is <code>AMAZON_ISSUED</code>. </p>"""
    renewal_eligibility: NotRequired[
        "capo_acm.types.renewal_eligibility.RenewalEligibility"
    ]
    """<p>Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the <a>RenewCertificate</a> command.</p>"""
    revoked_at: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was revoked. This value exists only when the certificate status is <code>REVOKED</code>. </p>"""
    status: NotRequired["capo_acm.types.certificate_status.CertificateStatus"]
    """<p>The status of the certificate.</p> <p>A certificate enters status PENDING_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic <a href="https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html">Certificate request fails</a>. ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION_TIMED_OUT, delete the request, correct the issue with <a href="https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html">DNS validation</a> or <a href="https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html">Email validation</a>, and try again. If validation succeeds, the certificate enters status ISSUED. </p>"""
    renewal_status: NotRequired["capo_acm.types.renewal_status.RenewalStatus"]
    """<p>The renewal status of the certificate.</p>"""
    type: NotRequired["capo_acm.types.certificate_type.CertificateType"]
    """<p>The source of the certificate. For certificates provided by ACM, this value is <code>AMAZON_ISSUED</code>. For certificates that you imported with <a>ImportCertificate</a>, this value is <code>IMPORTED</code>. ACM does not provide <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html">managed renewal</a> for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html">Importing Certificates</a> in the <i>Certificate Manager User Guide</i>. </p>"""
    export_option: NotRequired["capo_acm.types.certificate_export.CertificateExport"]
    """<p>Indicates whether the certificate can be exported.</p>"""
    managed_by: NotRequired[
        "capo_acm.types.certificate_managed_by.CertificateManagedBy"
    ]
    """<p>Identifies the Amazon Web Services service that manages the certificate issued by ACM.</p>"""
    validation_method: NotRequired["capo_acm.types.validation_method.ValidationMethod"]
    """<p>Specifies the domain validation method.</p>"""
    certificate_key_pair_origin: NotRequired[
        "capo_acm.types.certificate_key_pair_origin.CertificateKeyPairOrigin"
    ]
    """<p>The origin of the certificate's key pair.</p>"""
    acme_endpoint_arn: NotRequired["capo_acm.types.arn.Arn"]
    """<p>The ARN of the ACME endpoint used to issue the certificate.</p>"""
    acme_account_id: NotRequired["capo_acm.types.acme_account_id.AcmeAccountId"]
    """<p>The ACME account identifier associated with the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmCertificateMetadata) -> dict:
    out: dict = {}
    if "created_at" in value:
        import capo_acm.types.t_stamp

        out["CreatedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "exported" in value:
        out["Exported"] = value["exported"]
    if "imported_at" in value:
        import capo_acm.types.t_stamp

        out["ImportedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["imported_at"]
        )
    if "in_use" in value:
        out["InUse"] = value["in_use"]
    if "issued_at" in value:
        import capo_acm.types.t_stamp

        out["IssuedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["issued_at"]
        )
    if "renewal_eligibility" in value:
        import capo_acm.types.renewal_eligibility

        out["RenewalEligibility"] = (
            capo_acm.types.renewal_eligibility.serialize_aws_json_1_1(
                value["renewal_eligibility"]
            )
        )
    if "revoked_at" in value:
        import capo_acm.types.t_stamp

        out["RevokedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["revoked_at"]
        )
    if "status" in value:
        import capo_acm.types.certificate_status

        out["Status"] = capo_acm.types.certificate_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "renewal_status" in value:
        import capo_acm.types.renewal_status

        out["RenewalStatus"] = capo_acm.types.renewal_status.serialize_aws_json_1_1(
            value["renewal_status"]
        )
    if "type" in value:
        import capo_acm.types.certificate_type

        out["Type"] = capo_acm.types.certificate_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "export_option" in value:
        import capo_acm.types.certificate_export

        out["ExportOption"] = capo_acm.types.certificate_export.serialize_aws_json_1_1(
            value["export_option"]
        )
    if "managed_by" in value:
        import capo_acm.types.certificate_managed_by

        out["ManagedBy"] = capo_acm.types.certificate_managed_by.serialize_aws_json_1_1(
            value["managed_by"]
        )
    if "validation_method" in value:
        import capo_acm.types.validation_method

        out["ValidationMethod"] = (
            capo_acm.types.validation_method.serialize_aws_json_1_1(
                value["validation_method"]
            )
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


def deserialize_aws_json_1_1(data: dict) -> AcmCertificateMetadata:
    out: AcmCertificateMetadata = {}  # type: ignore[typeddict-item]
    if data.get("CreatedAt") is not None:
        import capo_acm.types.t_stamp

        out["created_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("Exported") is not None:
        out["exported"] = data["Exported"]
    if data.get("ImportedAt") is not None:
        import capo_acm.types.t_stamp

        out["imported_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["ImportedAt"]
        )
    if data.get("InUse") is not None:
        out["in_use"] = data["InUse"]
    if data.get("IssuedAt") is not None:
        import capo_acm.types.t_stamp

        out["issued_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["IssuedAt"]
        )
    if data.get("RenewalEligibility") is not None:
        import capo_acm.types.renewal_eligibility

        out["renewal_eligibility"] = (
            capo_acm.types.renewal_eligibility.deserialize_aws_json_1_1(
                data["RenewalEligibility"]
            )
        )
    if data.get("RevokedAt") is not None:
        import capo_acm.types.t_stamp

        out["revoked_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["RevokedAt"]
        )
    if data.get("Status") is not None:
        import capo_acm.types.certificate_status

        out["status"] = capo_acm.types.certificate_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("RenewalStatus") is not None:
        import capo_acm.types.renewal_status

        out["renewal_status"] = capo_acm.types.renewal_status.deserialize_aws_json_1_1(
            data["RenewalStatus"]
        )
    if data.get("Type") is not None:
        import capo_acm.types.certificate_type

        out["type"] = capo_acm.types.certificate_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("ExportOption") is not None:
        import capo_acm.types.certificate_export

        out["export_option"] = (
            capo_acm.types.certificate_export.deserialize_aws_json_1_1(
                data["ExportOption"]
            )
        )
    if data.get("ManagedBy") is not None:
        import capo_acm.types.certificate_managed_by

        out["managed_by"] = (
            capo_acm.types.certificate_managed_by.deserialize_aws_json_1_1(
                data["ManagedBy"]
            )
        )
    if data.get("ValidationMethod") is not None:
        import capo_acm.types.validation_method

        out["validation_method"] = (
            capo_acm.types.validation_method.deserialize_aws_json_1_1(
                data["ValidationMethod"]
            )
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
