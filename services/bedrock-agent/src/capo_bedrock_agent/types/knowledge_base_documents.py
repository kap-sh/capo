"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseDocuments``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.knowledge_base_document

KnowledgeBaseDocuments: TypeAlias = list[
    "capo_bedrock_agent.types.knowledge_base_document.KnowledgeBaseDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseDocuments) -> list:
    import capo_bedrock_agent.types.knowledge_base_document

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.knowledge_base_document.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KnowledgeBaseDocuments:
    import capo_bedrock_agent.types.knowledge_base_document

    out: KnowledgeBaseDocuments = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.knowledge_base_document.deserialize_json(item)
        )
    return out


def redact_sensitive(value: KnowledgeBaseDocuments) -> list[Any]:
    import capo_bedrock_agent.types.knowledge_base_document

    return [
        capo_bedrock_agent.types.knowledge_base_document.redact_sensitive(item)
        for item in value
    ]
