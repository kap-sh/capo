"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetDocumentContentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.presigned_url


class GetDocumentContentResponse(TypedDict, closed=True):
    mime_type: "str"
    """<p>The MIME type of the document content. For <code>RAW</code> format, this is the original file type (for example, <code>application/pdf</code>). For <code>EXTRACTED</code> format, this is always <code>application/json</code>.</p>"""
    presigned_url: "capo_bedrock_agent_runtime.types.presigned_url.PresignedUrl"
    """<p>A pre-signed URL for downloading the document content. The URL expires after 5 minutes.</p>"""
    document_content_length: NotRequired["int"]
    """<p>The size of the document content in bytes available at the pre-signed URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentContentResponse) -> dict:
    out: dict = {}
    out["mimeType"] = value["mime_type"]
    out["presignedUrl"] = value["presigned_url"]
    if "document_content_length" in value:
        out["documentContentLength"] = value["document_content_length"]
    return out


def deserialize_json(data: dict) -> GetDocumentContentResponse:
    out: GetDocumentContentResponse = {}  # type: ignore[typeddict-item]
    if data.get("mimeType") is not None:
        out["mime_type"] = data["mimeType"]
    else:
        raise DeserializationError("GetDocumentContentResponse.mime_type required")
    if data.get("presignedUrl") is not None:
        out["presigned_url"] = data["presignedUrl"]
    else:
        raise DeserializationError("GetDocumentContentResponse.presigned_url required")
    if data.get("documentContentLength") is not None:
        out["document_content_length"] = data["documentContentLength"]
    return out


def redact_sensitive(value: GetDocumentContentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "presigned_url" in value:
        out["presigned_url"] = "*** Sensitive Data Redacted ***"
    return out
