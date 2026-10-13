"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime

AgentRuntimes: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.agent_runtime.AgentRuntime"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimes) -> list:
    import capo_bedrock_agentcore_control.types.agent_runtime

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.agent_runtime.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentRuntimes:
    import capo_bedrock_agentcore_control.types.agent_runtime

    out: AgentRuntimes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.agent_runtime.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AgentRuntimes) -> list[Any]:
    import capo_bedrock_agentcore_control.types.agent_runtime

    return [
        capo_bedrock_agentcore_control.types.agent_runtime.redact_sensitive(item)
        for item in value
    ]
