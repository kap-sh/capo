"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeEndpoints``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint

AgentRuntimeEndpoints: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.agent_runtime_endpoint.AgentRuntimeEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeEndpoints) -> list:
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.agent_runtime_endpoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgentRuntimeEndpoints:
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint

    out: AgentRuntimeEndpoints = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.agent_runtime_endpoint.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AgentRuntimeEndpoints) -> list[Any]:
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint

    return [
        capo_bedrock_agentcore_control.types.agent_runtime_endpoint.redact_sensitive(
            item
        )
        for item in value
    ]
