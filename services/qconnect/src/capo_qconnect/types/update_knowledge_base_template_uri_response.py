"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateKnowledgeBaseTemplateUriResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.knowledge_base_data


class UpdateKnowledgeBaseTemplateUriResponse(TypedDict, closed=True):
    knowledge_base: NotRequired[
        "capo_qconnect.types.knowledge_base_data.KnowledgeBaseData"
    ]
    """<p>The knowledge base to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKnowledgeBaseTemplateUriResponse) -> dict:
    out: dict = {}
    if "knowledge_base" in value:
        import capo_qconnect.types.knowledge_base_data

        out["knowledgeBase"] = capo_qconnect.types.knowledge_base_data.serialize_json(
            value["knowledge_base"]
        )
    return out


def deserialize_json(data: dict) -> UpdateKnowledgeBaseTemplateUriResponse:
    out: UpdateKnowledgeBaseTemplateUriResponse = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBase") is not None:
        import capo_qconnect.types.knowledge_base_data

        out["knowledge_base"] = (
            capo_qconnect.types.knowledge_base_data.deserialize_json(
                data["knowledgeBase"]
            )
        )
    return out


def redact_sensitive(value: UpdateKnowledgeBaseTemplateUriResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base" in value:
        import capo_qconnect.types.knowledge_base_data

        out["knowledge_base"] = (
            capo_qconnect.types.knowledge_base_data.redact_sensitive(
                value["knowledge_base"]
            )
        )
    return out
