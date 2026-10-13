"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseConfigurations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_configuration

KnowledgeBaseConfigurations: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfigurations) -> list:
    import capo_bedrock_agent_runtime.types.knowledge_base_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.knowledge_base_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> KnowledgeBaseConfigurations:
    import capo_bedrock_agent_runtime.types.knowledge_base_configuration

    out: KnowledgeBaseConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.knowledge_base_configuration.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: KnowledgeBaseConfigurations) -> list[Any]:
    import capo_bedrock_agent_runtime.types.knowledge_base_configuration

    return [
        capo_bedrock_agent_runtime.types.knowledge_base_configuration.redact_sensitive(
            item
        )
        for item in value
    ]
