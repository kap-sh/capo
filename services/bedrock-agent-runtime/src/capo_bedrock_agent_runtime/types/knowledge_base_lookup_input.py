"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseLookupInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_lookup_input_string
    import capo_bedrock_agent_runtime.types.trace_knowledge_base_id


class KnowledgeBaseLookupInput(TypedDict, closed=True):
    text: NotRequired[
        "capo_bedrock_agent_runtime.types.knowledge_base_lookup_input_string.KnowledgeBaseLookupInputString"
    ]
    """<p>The query made to the knowledge base.</p>"""
    knowledge_base_id: NotRequired[
        "capo_bedrock_agent_runtime.types.trace_knowledge_base_id.TraceKnowledgeBaseId"
    ]
    """<p>The unique identifier of the knowledge base to look up.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseLookupInput) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "knowledge_base_id" in value:
        out["knowledgeBaseId"] = value["knowledge_base_id"]
    return out


def deserialize_json(data: dict) -> KnowledgeBaseLookupInput:
    out: KnowledgeBaseLookupInput = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    return out


def redact_sensitive(value: KnowledgeBaseLookupInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "knowledge_base_id" in value:
        out["knowledge_base_id"] = "*** Sensitive Data Redacted ***"
    return out
