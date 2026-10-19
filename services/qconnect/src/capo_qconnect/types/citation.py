"""Generated from Smithy shape ``com.amazonaws.qconnect#Citation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.citation_span
    import capo_qconnect.types.reference_type
    import capo_qconnect.types.sensitive_string
    import capo_qconnect.types.uuid


class Citation(TypedDict, closed=True):
    content_id: NotRequired["capo_qconnect.types.uuid.Uuid"]
    """<p>The identifier of the content being cited.</p>"""
    title: NotRequired["capo_qconnect.types.sensitive_string.SensitiveString"]
    """<p>The title of the cited content.</p>"""
    knowledge_base_id: NotRequired["capo_qconnect.types.uuid.Uuid"]
    """<p>The identifier of the knowledge base containing the cited content.</p>"""
    citation_span: "capo_qconnect.types.citation_span.CitationSpan"
    source_url: NotRequired["capo_qconnect.types.sensitive_string.SensitiveString"]
    """<p>The source URL for the citation.</p>"""
    reference_type: "capo_qconnect.types.reference_type.ReferenceType"
    """<p>A type to define the KB origin of a cited content</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Citation) -> dict:
    out: dict = {}
    if "content_id" in value:
        out["contentId"] = value["content_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "knowledge_base_id" in value:
        out["knowledgeBaseId"] = value["knowledge_base_id"]
    import capo_qconnect.types.citation_span

    out["citationSpan"] = capo_qconnect.types.citation_span.serialize_json(
        value["citation_span"]
    )
    if "source_url" in value:
        out["sourceURL"] = value["source_url"]
    out["referenceType"] = value["reference_type"]
    return out


def deserialize_json(data: dict) -> Citation:
    out: Citation = {}  # type: ignore[typeddict-item]
    if data.get("contentId") is not None:
        out["content_id"] = data["contentId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    if data.get("citationSpan") is not None:
        import capo_qconnect.types.citation_span

        out["citation_span"] = capo_qconnect.types.citation_span.deserialize_json(
            data["citationSpan"]
        )
    else:
        raise DeserializationError("Citation.citation_span required")
    if data.get("sourceURL") is not None:
        out["source_url"] = data["sourceURL"]
    if data.get("referenceType") is not None:
        out["reference_type"] = data["referenceType"]
    else:
        out["reference_type"] = ""
    return out


def redact_sensitive(value: Citation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "source_url" in value:
        out["source_url"] = "*** Sensitive Data Redacted ***"
    return out
