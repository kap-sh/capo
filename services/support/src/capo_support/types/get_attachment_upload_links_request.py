"""Generated from Smithy shape ``com.amazonaws.support#GetAttachmentUploadLinksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.file_name
    import capo_support.types.file_size
    import capo_support.types.nullable_boolean_type
    import capo_support.types.upload_id
    import capo_support.types.upload_range


class GetAttachmentUploadLinksRequest(TypedDict, closed=True):
    file_name: "capo_support.types.file_name.FileName"
    """<p>The name of the file to upload, including the file extension. This value is required when you initiate a new upload.</p>"""
    file_size_bytes: NotRequired["capo_support.types.file_size.FileSize"]
    """<p>The total size of the file in bytes. The service uses this value to calculate the total number of parts and the size of each part. Required when you initiate a new upload (when <code>uploadId</code> isn't provided). Valid range: 1 to 157,286,400 bytes (approximately 150 MB).</p>"""
    upload_id: NotRequired["capo_support.types.upload_id.UploadId"]
    """<p>The unique identifier of an in-progress multipart upload, returned by a previous call to <code>GetAttachmentUploadLinks</code>. Specify <code>uploadId</code> to retrieve additional presigned upload URLs for an upload that has already been initiated. Required when <code>fileSizeBytes</code> isn't provided. Length: 1 to 2,048 characters.</p>"""
    upload_range: NotRequired["capo_support.types.upload_range.UploadRange"]
    """<p>The range of part indexes for which to return presigned upload URLs. Use this parameter to page through the upload URLs for a large file across multiple calls. If you omit this parameter, the service determines the range to return.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually generating upload URLs. When set to <code>true</code>, the request is validated but no URLs are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAttachmentUploadLinksRequest) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    if "file_size_bytes" in value:
        out["fileSizeBytes"] = value["file_size_bytes"]
    if "upload_id" in value:
        out["uploadId"] = value["upload_id"]
    if "upload_range" in value:
        import capo_support.types.upload_range

        out["uploadRange"] = capo_support.types.upload_range.serialize_aws_json_1_1(
            value["upload_range"]
        )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAttachmentUploadLinksRequest:
    out: GetAttachmentUploadLinksRequest = {}  # type: ignore[typeddict-item]
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    if data.get("fileSizeBytes") is not None:
        out["file_size_bytes"] = data["fileSizeBytes"]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    if data.get("uploadRange") is not None:
        import capo_support.types.upload_range

        out["upload_range"] = capo_support.types.upload_range.deserialize_aws_json_1_1(
            data["uploadRange"]
        )
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
