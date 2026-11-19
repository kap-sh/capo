"""Generated from Smithy shape ``com.amazonaws.wellarchitected#SendAgentOrganizationalReportDataToS3Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_report_format
    import capo_wellarchitected.types.s3_bucket_arn
    import capo_wellarchitected.types.s3_object_key
    import capo_wellarchitected.types.uuid


class SendAgentOrganizationalReportDataToS3Request(TypedDict, closed=True):
    report_id: "capo_wellarchitected.types.uuid.UUID"
    """<p>Identifier of the report whose data is being delivered.</p>"""
    format: "capo_wellarchitected.types.organizational_report_format.OrganizationalReportFormat"
    """<p>Format of the delivered artifact (CSV, JSON, or PARQUET).</p>"""
    bucket_arn: "capo_wellarchitected.types.s3_bucket_arn.S3BucketArn"
    """<p>ARN of the caller-owned S3 bucket that will receive the artifact.</p>"""
    object_key: "capo_wellarchitected.types.s3_object_key.S3ObjectKey"
    """<p>S3 object key under bucketArn where the artifact will be written.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendAgentOrganizationalReportDataToS3Request) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.organizational_report_format

    out["format"] = (
        capo_wellarchitected.types.organizational_report_format.serialize_json(
            value["format"]
        )
    )
    out["bucketArn"] = value["bucket_arn"]
    out["objectKey"] = value["object_key"]
    return out


def deserialize_json(data: dict) -> SendAgentOrganizationalReportDataToS3Request:
    out: SendAgentOrganizationalReportDataToS3Request = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_wellarchitected.types.organizational_report_format

        out["format"] = (
            capo_wellarchitected.types.organizational_report_format.deserialize_json(
                data["format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_wellarchitected.types.organizational_report_format.OrganizationalReportFormat",
            "",
        )
    if data.get("bucketArn") is not None:
        out["bucket_arn"] = data["bucketArn"]
    else:
        out["bucket_arn"] = ""
    if data.get("objectKey") is not None:
        out["object_key"] = data["objectKey"]
    else:
        out["object_key"] = ""
    return out
