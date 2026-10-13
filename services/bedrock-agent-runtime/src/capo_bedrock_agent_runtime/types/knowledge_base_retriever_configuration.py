"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseRetrieverConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_id
    import capo_bedrock_agent_runtime.types.retrieval_overrides


class KnowledgeBaseRetrieverConfiguration(TypedDict, closed=True):
    knowledge_base_id: (
        "capo_bedrock_agent_runtime.types.knowledge_base_id.KnowledgeBaseId"
    )
    """<p>The unique identifier of the knowledge base.</p>"""
    retrieval_overrides: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_overrides.RetrievalOverrides"
    ]
    """<p>Overrides for retrieval behavior such as filters and result limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseRetrieverConfiguration) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    if "retrieval_overrides" in value:
        import capo_bedrock_agent_runtime.types.retrieval_overrides

        out["retrievalOverrides"] = (
            capo_bedrock_agent_runtime.types.retrieval_overrides.serialize_json(
                value["retrieval_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseRetrieverConfiguration:
    out: KnowledgeBaseRetrieverConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "KnowledgeBaseRetrieverConfiguration.knowledge_base_id required"
        )
    if data.get("retrievalOverrides") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_overrides

        out["retrieval_overrides"] = (
            capo_bedrock_agent_runtime.types.retrieval_overrides.deserialize_json(
                data["retrievalOverrides"]
            )
        )
    return out


def redact_sensitive(value: KnowledgeBaseRetrieverConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "retrieval_overrides" in value:
        import capo_bedrock_agent_runtime.types.retrieval_overrides

        out["retrieval_overrides"] = (
            capo_bedrock_agent_runtime.types.retrieval_overrides.redact_sensitive(
                value["retrieval_overrides"]
            )
        )
    return out
