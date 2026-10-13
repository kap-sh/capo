"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInputs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_input

FlowInputs: TypeAlias = list["capo_bedrock_agent_runtime.types.flow_input.FlowInput"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowInputs) -> list:
    import capo_bedrock_agent_runtime.types.flow_input

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.flow_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowInputs:
    import capo_bedrock_agent_runtime.types.flow_input

    out: FlowInputs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.flow_input.deserialize_json(item))
    return out


def redact_sensitive(value: FlowInputs) -> list[Any]:
    import capo_bedrock_agent_runtime.types.flow_input

    return [
        capo_bedrock_agent_runtime.types.flow_input.redact_sensitive(item)
        for item in value
    ]
