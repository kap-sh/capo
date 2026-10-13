"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveActions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_action

AgenticRetrieveActions: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_action.AgenticRetrieveAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveActions) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_action

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_action.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveActions:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_action

    out: AgenticRetrieveActions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_action.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AgenticRetrieveActions) -> list[Any]:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_action

    return [
        capo_bedrock_agent_runtime.types.agentic_retrieve_action.redact_sensitive(item)
        for item in value
    ]
