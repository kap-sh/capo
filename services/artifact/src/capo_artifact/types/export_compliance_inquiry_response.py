"""Generated from Smithy shape ``com.amazonaws.artifact#ExportComplianceInquiryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.presigned_url
    import capo_artifact.types.tags_map


class ExportComplianceInquiryResponse(TypedDict, closed=True):
    document_presigned_url: NotRequired[
        "capo_artifact.types.presigned_url.PresignedUrl"
    ]
    """<p>Presigned S3 URL to access the exported compliance inquiry report.</p>"""
    tags: NotRequired["capo_artifact.types.tags_map.TagsMap"]
    """<p>Tags associated with the compliance inquiry resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportComplianceInquiryResponse) -> dict:
    out: dict = {}
    if "document_presigned_url" in value:
        out["documentPresignedUrl"] = value["document_presigned_url"]
    if "tags" in value:
        import capo_artifact.types.tags_map

        out["tags"] = capo_artifact.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ExportComplianceInquiryResponse:
    out: ExportComplianceInquiryResponse = {}  # type: ignore[typeddict-item]
    if data.get("documentPresignedUrl") is not None:
        out["document_presigned_url"] = data["documentPresignedUrl"]
    if data.get("tags") is not None:
        import capo_artifact.types.tags_map

        out["tags"] = capo_artifact.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: ExportComplianceInquiryResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document_presigned_url" in value:
        out["document_presigned_url"] = "*** Sensitive Data Redacted ***"
    return out
