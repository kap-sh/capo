"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetDocumentContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.string


class GetDocumentContentResponse(TypedDict, closed=True):
    presigned_url: "capo_qbusiness.types.string.String"
    """<p>A pre-signed URL that provides temporary access to download the document content directly from Amazon Q Business. The URL expires after 5 minutes for security purposes. This URL is generated only after successful ACL validation.</p>"""
    mime_type: "capo_qbusiness.types.string.String"
    """<p>The MIME type of the document content. When outputFormat is RAW, this corresponds to the original document's MIME type (e.g., application/pdf, text/plain, application/vnd.openxmlformats-officedocument.wordprocessingml.document). When outputFormat is EXTRACTED, the MIME type is always application/json.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentContentResponse) -> dict:
    out: dict = {}
    out["presignedUrl"] = value["presigned_url"]
    out["mimeType"] = value["mime_type"]
    return out


def deserialize_json(data: dict) -> GetDocumentContentResponse:
    out: GetDocumentContentResponse = {}  # type: ignore[typeddict-item]
    if data.get("presignedUrl") is not None:
        out["presigned_url"] = data["presignedUrl"]
    else:
        out["presigned_url"] = ""
    if data.get("mimeType") is not None:
        out["mime_type"] = data["mimeType"]
    else:
        out["mime_type"] = ""
    return out
