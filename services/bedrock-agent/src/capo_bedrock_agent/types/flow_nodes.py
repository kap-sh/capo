"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node

FlowNodes: TypeAlias = list["capo_bedrock_agent.types.flow_node.FlowNode"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodes) -> list:
    import capo_bedrock_agent.types.flow_node

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.flow_node.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowNodes:
    import capo_bedrock_agent.types.flow_node

    out: FlowNodes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.flow_node.deserialize_json(item))
    return out


def redact_sensitive(value: FlowNodes) -> list[Any]:
    import capo_bedrock_agent.types.flow_node

    return [capo_bedrock_agent.types.flow_node.redact_sensitive(item) for item in value]
