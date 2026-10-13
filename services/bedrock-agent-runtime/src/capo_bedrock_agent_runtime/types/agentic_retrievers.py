"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrievers``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retriever

AgenticRetrievers: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retriever.AgenticRetriever"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrievers) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retriever

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retriever.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgenticRetrievers:
    import capo_bedrock_agent_runtime.types.agentic_retriever

    out: AgenticRetrievers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retriever.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AgenticRetrievers) -> list[Any]:
    import capo_bedrock_agent_runtime.types.agentic_retriever

    return [
        capo_bedrock_agent_runtime.types.agentic_retriever.redact_sensitive(item)
        for item in value
    ]
