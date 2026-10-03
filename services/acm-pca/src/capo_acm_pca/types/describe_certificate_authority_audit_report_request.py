"""Generated from Smithy shape ``com.amazonaws.acmpca#DescribeCertificateAuthorityAuditReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.audit_report_id


class DescribeCertificateAuthorityAuditReportRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the private CA. This must be of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>"""
    audit_report_id: "capo_acm_pca.types.audit_report_id.AuditReportId"
    """<p>The report ID returned by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html">CreateCertificateAuthorityAuditReport</a> action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeCertificateAuthorityAuditReportRequest,
) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    out["AuditReportId"] = value["audit_report_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeCertificateAuthorityAuditReportRequest:
    out: DescribeCertificateAuthorityAuditReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "DescribeCertificateAuthorityAuditReportRequest.certificate_authority_arn required"
        )
    if data.get("AuditReportId") is not None:
        out["audit_report_id"] = data["AuditReportId"]
    else:
        raise DeserializationError(
            "DescribeCertificateAuthorityAuditReportRequest.audit_report_id required"
        )
    return out
