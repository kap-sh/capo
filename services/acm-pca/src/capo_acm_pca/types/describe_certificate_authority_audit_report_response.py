"""Generated from Smithy shape ``com.amazonaws.acmpca#DescribeCertificateAuthorityAuditReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.audit_report_status
    import capo_acm_pca.types.s3_bucket_name
    import capo_acm_pca.types.s3_key
    import capo_acm_pca.types.t_stamp


class DescribeCertificateAuthorityAuditReportResponse(TypedDict, closed=True):
    audit_report_status: NotRequired[
        "capo_acm_pca.types.audit_report_status.AuditReportStatus"
    ]
    """<p>Specifies whether report creation is in progress, has succeeded, or has failed.</p>"""
    s3_bucket_name: NotRequired["capo_acm_pca.types.s3_bucket_name.S3BucketName"]
    """<p>Name of the S3 bucket that contains the report.</p>"""
    s3_key: NotRequired["capo_acm_pca.types.s3_key.S3Key"]
    """<p>S3 <b>key</b> that uniquely identifies the report file in your S3 bucket.</p>"""
    created_at: NotRequired["capo_acm_pca.types.t_stamp.TStamp"]
    """<p>The date and time at which the report was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeCertificateAuthorityAuditReportResponse,
) -> dict:
    out: dict = {}
    if "audit_report_status" in value:
        import capo_acm_pca.types.audit_report_status

        out["AuditReportStatus"] = (
            capo_acm_pca.types.audit_report_status.serialize_aws_json_1_1(
                value["audit_report_status"]
            )
        )
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    if "created_at" in value:
        import capo_acm_pca.types.t_stamp

        out["CreatedAt"] = capo_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeCertificateAuthorityAuditReportResponse:
    out: DescribeCertificateAuthorityAuditReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("AuditReportStatus") is not None:
        import capo_acm_pca.types.audit_report_status

        out["audit_report_status"] = (
            capo_acm_pca.types.audit_report_status.deserialize_aws_json_1_1(
                data["AuditReportStatus"]
            )
        )
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    if data.get("S3Key") is not None:
        out["s3_key"] = data["S3Key"]
    if data.get("CreatedAt") is not None:
        import capo_acm_pca.types.t_stamp

        out["created_at"] = capo_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeCertificateAuthorityAuditReportResponse) -> dict:
    out: dict = {}
    if "audit_report_status" in value:
        import capo_acm_pca.types.audit_report_status

        out["AuditReportStatus"] = (
            capo_acm_pca.types.audit_report_status.serialize_cbor(
                value["audit_report_status"]
            )
        )
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    if "created_at" in value:
        import capo_acm_pca.types.t_stamp

        out["CreatedAt"] = capo_acm_pca.types.t_stamp.serialize_cbor(
            value["created_at"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeCertificateAuthorityAuditReportResponse:
    out: DescribeCertificateAuthorityAuditReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("AuditReportStatus") is not None:
        import capo_acm_pca.types.audit_report_status

        out["audit_report_status"] = (
            capo_acm_pca.types.audit_report_status.deserialize_cbor(
                data["AuditReportStatus"]
            )
        )
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    if data.get("S3Key") is not None:
        out["s3_key"] = data["S3Key"]
    if data.get("CreatedAt") is not None:
        import capo_acm_pca.types.t_stamp

        out["created_at"] = capo_acm_pca.types.t_stamp.deserialize_cbor(
            data["CreatedAt"]
        )
    return out
