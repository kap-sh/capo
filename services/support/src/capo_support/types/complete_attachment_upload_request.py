"""Generated from Smithy shape ``com.amazonaws.support#CompleteAttachmentUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.completed_upload_list
    import capo_support.types.nullable_boolean_type
    import capo_support.types.upload_id


class CompleteAttachmentUploadRequest(TypedDict, closed=True):
    upload_id: "capo_support.types.upload_id.UploadId"
    """<p>The identifier associated with the upload to complete.</p>"""
    completed_uploads: "capo_support.types.completed_upload_list.CompletedUploadList"
    """<p>The list of parts being reported as completed in this call. Each entry must contain the <code>partIndex</code> of an uploaded part and the <code>ETag</code> returned by Amazon S3 when that part was uploaded.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually completing the upload. When set to <code>true</code>, the request is validated but the upload isn't finalized, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompleteAttachmentUploadRequest) -> dict:
    out: dict = {}
    out["uploadId"] = value["upload_id"]
    import capo_support.types.completed_upload_list

    out["completedUploads"] = (
        capo_support.types.completed_upload_list.serialize_aws_json_1_1(
            value["completed_uploads"]
        )
    )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CompleteAttachmentUploadRequest:
    out: CompleteAttachmentUploadRequest = {}  # type: ignore[typeddict-item]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        out["upload_id"] = ""
    if data.get("completedUploads") is not None:
        import capo_support.types.completed_upload_list

        out["completed_uploads"] = (
            capo_support.types.completed_upload_list.deserialize_aws_json_1_1(
                data["completedUploads"]
            )
        )
    else:
        out["completed_uploads"] = []
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
