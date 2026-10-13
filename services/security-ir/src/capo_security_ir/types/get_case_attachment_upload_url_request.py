"""Generated from Smithy shape ``com.amazonaws.securityir#GetCaseAttachmentUploadUrlRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.case_id
    import capo_security_ir.types.content_length
    import capo_security_ir.types.file_name


class GetCaseAttachmentUploadUrlRequest(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Required element for GetCaseAttachmentUploadUrl to identify the case ID for uploading an attachment. </p>"""
    file_name: "capo_security_ir.types.file_name.FileName"
    """<p>Required element for GetCaseAttachmentUploadUrl to identify the file name of the attachment to upload. </p>"""
    content_length: "capo_security_ir.types.content_length.ContentLength"
    """<p>Required element for GetCaseAttachmentUploadUrl to identify the size of the file attachment.</p>"""
    client_token: NotRequired["str"]
    """<note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseAttachmentUploadUrlRequest) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    out["contentLength"] = value["content_length"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> GetCaseAttachmentUploadUrlRequest:
    out: GetCaseAttachmentUploadUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError(
            "GetCaseAttachmentUploadUrlRequest.file_name required"
        )
    if data.get("contentLength") is not None:
        out["content_length"] = data["contentLength"]
    else:
        raise DeserializationError(
            "GetCaseAttachmentUploadUrlRequest.content_length required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: GetCaseAttachmentUploadUrlRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_name" in value:
        out["file_name"] = "*** Sensitive Data Redacted ***"
    return out
