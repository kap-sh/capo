"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentActionGroups``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_action_group

AgentActionGroups: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agent_action_group.AgentActionGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentActionGroups) -> list:
    import capo_bedrock_agent_runtime.types.agent_action_group

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agent_action_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentActionGroups:
    import capo_bedrock_agent_runtime.types.agent_action_group

    out: AgentActionGroups = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agent_action_group.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AgentActionGroups) -> list[Any]:
    import capo_bedrock_agent_runtime.types.agent_action_group

    return [
        capo_bedrock_agent_runtime.types.agent_action_group.redact_sensitive(item)
        for item in value
    ]
