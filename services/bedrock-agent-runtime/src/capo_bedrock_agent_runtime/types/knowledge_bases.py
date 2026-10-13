"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBases``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base

KnowledgeBases: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.knowledge_base.KnowledgeBase"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBases) -> list:
    import capo_bedrock_agent_runtime.types.knowledge_base

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.knowledge_base.serialize_json(item))
    return out


def deserialize_json(data: list) -> KnowledgeBases:
    import capo_bedrock_agent_runtime.types.knowledge_base

    out: KnowledgeBases = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.knowledge_base.deserialize_json(item)
        )
    return out


def redact_sensitive(value: KnowledgeBases) -> list[Any]:
    import capo_bedrock_agent_runtime.types.knowledge_base

    return [
        capo_bedrock_agent_runtime.types.knowledge_base.redact_sensitive(item)
        for item in value
    ]
