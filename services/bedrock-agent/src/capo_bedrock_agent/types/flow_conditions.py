"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConditions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_condition

FlowConditions: TypeAlias = list[
    "capo_bedrock_agent.types.flow_condition.FlowCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowConditions) -> list:
    import capo_bedrock_agent.types.flow_condition

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.flow_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowConditions:
    import capo_bedrock_agent.types.flow_condition

    out: FlowConditions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.flow_condition.deserialize_json(item))
    return out


def redact_sensitive(value: FlowConditions) -> list[Any]:
    import capo_bedrock_agent.types.flow_condition

    return [
        capo_bedrock_agent.types.flow_condition.redact_sensitive(item) for item in value
    ]
