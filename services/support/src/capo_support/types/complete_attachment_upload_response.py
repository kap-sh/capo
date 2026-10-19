"""Generated from Smithy shape ``com.amazonaws.support#CompleteAttachmentUploadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.upload_status


class CompleteAttachmentUploadResponse(TypedDict, closed=True):
    upload_status: "capo_support.types.upload_status.UploadStatus"
    """<p>The status of the multipart upload after the operation finalizes the attachment. Valid values: <code>attachment-ready</code>, <code>attachment-not-ready</code>, and <code>failed</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompleteAttachmentUploadResponse) -> dict:
    out: dict = {}
    import capo_support.types.upload_status

    out["uploadStatus"] = capo_support.types.upload_status.serialize_aws_json_1_1(
        value["upload_status"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompleteAttachmentUploadResponse:
    out: CompleteAttachmentUploadResponse = {}  # type: ignore[typeddict-item]
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
    return out
