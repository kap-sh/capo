"""Generated from Smithy shape ``com.amazonaws.support#DescribeAttachmentUploadStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.nullable_boolean_type
    import capo_support.types.upload_id


class DescribeAttachmentUploadStatusRequest(TypedDict, closed=True):
    upload_id: "capo_support.types.upload_id.UploadId"
    """<p>The unique identifier for the upload. The <code>uploadId</code> is returned by <a>GetAttachmentUploadLinks</a> when you initiate the upload.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually returning upload status. When set to <code>true</code>, the request is validated but no status is returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttachmentUploadStatusRequest) -> dict:
    out: dict = {}
    out["uploadId"] = value["upload_id"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttachmentUploadStatusRequest:
    out: DescribeAttachmentUploadStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        out["upload_id"] = ""
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
