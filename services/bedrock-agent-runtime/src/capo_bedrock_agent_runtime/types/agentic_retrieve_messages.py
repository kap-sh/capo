"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMessages``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message

AgenticRetrieveMessages: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_message.AgenticRetrieveMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMessages) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_message.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveMessages:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message

    out: AgenticRetrieveMessages = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_message.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AgenticRetrieveMessages) -> list[Any]:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message

    return [
        capo_bedrock_agent_runtime.types.agentic_retrieve_message.redact_sensitive(item)
        for item in value
    ]
