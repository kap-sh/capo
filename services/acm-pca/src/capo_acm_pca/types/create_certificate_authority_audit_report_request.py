"""Generated from Smithy shape ``com.amazonaws.acmpca#CreateCertificateAuthorityAuditReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.audit_report_response_format
    import capo_acm_pca.types.s3_bucket_name


class CreateCertificateAuthorityAuditReportRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the CA to be audited. This is of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>.</p>"""
    s3_bucket_name: "capo_acm_pca.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket that will contain the audit report.</p>"""
    audit_report_response_format: (
        "capo_acm_pca.types.audit_report_response_format.AuditReportResponseFormat"
    )
    """<p>The format in which to create the report. This can be either <b>JSON</b> or <b>CSV</b>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCertificateAuthorityAuditReportRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    out["S3BucketName"] = value["s3_bucket_name"]
    import capo_acm_pca.types.audit_report_response_format

    out["AuditReportResponseFormat"] = (
        capo_acm_pca.types.audit_report_response_format.serialize_aws_json_1_1(
            value["audit_report_response_format"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateCertificateAuthorityAuditReportRequest:
    out: CreateCertificateAuthorityAuditReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        out["certificate_authority_arn"] = ""
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        out["s3_bucket_name"] = ""
    if data.get("AuditReportResponseFormat") is not None:
        import capo_acm_pca.types.audit_report_response_format

        out["audit_report_response_format"] = (
            capo_acm_pca.types.audit_report_response_format.deserialize_aws_json_1_1(
                data["AuditReportResponseFormat"]
            )
        )
    else:
        import typing

        out["audit_report_response_format"] = typing.cast(
            "capo_acm_pca.types.audit_report_response_format.AuditReportResponseFormat",
            "",
        )
    return out
