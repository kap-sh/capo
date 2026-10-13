"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodeInputs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_input

FlowNodeInputs: TypeAlias = list[
    "capo_bedrock_agent.types.flow_node_input.FlowNodeInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodeInputs) -> list:
    import capo_bedrock_agent.types.flow_node_input

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.flow_node_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowNodeInputs:
    import capo_bedrock_agent.types.flow_node_input

    out: FlowNodeInputs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.flow_node_input.deserialize_json(item))
    return out


def redact_sensitive(value: FlowNodeInputs) -> list[Any]:
    import capo_bedrock_agent.types.flow_node_input

    return [
        capo_bedrock_agent.types.flow_node_input.redact_sensitive(item)
        for item in value
    ]
