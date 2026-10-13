"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentTraces``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.trace_part

AgentTraces: TypeAlias = list["capo_bedrock_agent_runtime.types.trace_part.TracePart"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentTraces) -> list:
    import capo_bedrock_agent_runtime.types.trace_part

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.trace_part.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentTraces:
    import capo_bedrock_agent_runtime.types.trace_part

    out: AgentTraces = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.trace_part.deserialize_json(item))
    return out


def redact_sensitive(value: AgentTraces) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
