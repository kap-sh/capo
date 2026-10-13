"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanCitation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.arn
    import capo_qconnect.types.sensitive_string
    import capo_qconnect.types.uuid


class SpanCitation(TypedDict, closed=True):
    content_id: NotRequired["capo_qconnect.types.uuid.Uuid"]
    """<p>The identifier of the content being cited in the span.</p>"""
    title: NotRequired["capo_qconnect.types.sensitive_string.SensitiveString"]
    """<p>The title of the content being cited in the span.</p>"""
    knowledge_base_id: NotRequired["capo_qconnect.types.uuid.Uuid"]
    """<p>The identifier of the knowledge base containing the cited content.</p>"""
    knowledge_base_arn: NotRequired["capo_qconnect.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the knowledge base containing the cited content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanCitation) -> dict:
    out: dict = {}
    if "content_id" in value:
        out["contentId"] = value["content_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "knowledge_base_id" in value:
        out["knowledgeBaseId"] = value["knowledge_base_id"]
    if "knowledge_base_arn" in value:
        out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> SpanCitation:
    out: SpanCitation = {}  # type: ignore[typeddict-item]
    if data.get("contentId") is not None:
        out["content_id"] = data["contentId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    return out


def redact_sensitive(value: SpanCitation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    return out
