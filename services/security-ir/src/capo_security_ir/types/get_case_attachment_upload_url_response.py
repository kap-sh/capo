"""Generated from Smithy shape ``com.amazonaws.securityir#GetCaseAttachmentUploadUrlResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.url


class GetCaseAttachmentUploadUrlResponse(TypedDict, closed=True):
    attachment_presigned_url: "capo_security_ir.types.url.Url"
    """<p>Response element providing the Amazon S3 presigned URL to upload the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseAttachmentUploadUrlResponse) -> dict:
    out: dict = {}
    out["attachmentPresignedUrl"] = value["attachment_presigned_url"]
    return out


def deserialize_json(data: dict) -> GetCaseAttachmentUploadUrlResponse:
    out: GetCaseAttachmentUploadUrlResponse = {}  # type: ignore[typeddict-item]
    if data.get("attachmentPresignedUrl") is not None:
        out["attachment_presigned_url"] = data["attachmentPresignedUrl"]
    else:
        raise DeserializationError(
            "GetCaseAttachmentUploadUrlResponse.attachment_presigned_url required"
        )
    return out


def redact_sensitive(value: GetCaseAttachmentUploadUrlResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attachment_presigned_url" in value:
        out["attachment_presigned_url"] = "*** Sensitive Data Redacted ***"
    return out
