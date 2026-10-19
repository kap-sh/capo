"""Generated from Smithy shape ``com.amazonaws.support#DescribeAttachmentUploadStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.file_name
    import capo_support.types.upload_progress
    import capo_support.types.upload_status


class DescribeAttachmentUploadStatusResponse(TypedDict, closed=True):
    upload_status: "capo_support.types.upload_status.UploadStatus"
    """<p>The current status of the multipart upload. Valid values: <code>attachment-ready</code>, <code>attachment-not-ready</code>, and <code>failed</code>.</p>"""
    file_name: "capo_support.types.file_name.FileName"
    """<p>The name of the file being uploaded, including the file extension.</p>"""
    upload_progress: NotRequired["capo_support.types.upload_progress.UploadProgress"]
    """<p>The progress of the multipart upload, including the total number of parts and the number of parts that have been successfully uploaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttachmentUploadStatusResponse) -> dict:
    out: dict = {}
    import capo_support.types.upload_status

    out["uploadStatus"] = capo_support.types.upload_status.serialize_aws_json_1_1(
        value["upload_status"]
    )
    out["fileName"] = value["file_name"]
    if "upload_progress" in value:
        import capo_support.types.upload_progress

        out["uploadProgress"] = (
            capo_support.types.upload_progress.serialize_aws_json_1_1(
                value["upload_progress"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttachmentUploadStatusResponse:
    out: DescribeAttachmentUploadStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("uploadStatus") is not None:
        import capo_support.types.upload_status

        out["upload_status"] = (
            capo_support.types.upload_status.deserialize_aws_json_1_1(
                data["uploadStatus"]
            )
        )
    else:
        import typing

        out["upload_status"] = typing.cast(
            "capo_support.types.upload_status.UploadStatus", ""
        )
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    if data.get("uploadProgress") is not None:
        import capo_support.types.upload_progress

        out["upload_progress"] = (
            capo_support.types.upload_progress.deserialize_aws_json_1_1(
                data["uploadProgress"]
            )
        )
    return out
