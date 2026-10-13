"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionEvents``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_execution_event

FlowExecutionEvents: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.flow_execution_event.FlowExecutionEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionEvents) -> list:
    import capo_bedrock_agent_runtime.types.flow_execution_event

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.flow_execution_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FlowExecutionEvents:
    import capo_bedrock_agent_runtime.types.flow_execution_event

    out: FlowExecutionEvents = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.flow_execution_event.deserialize_json(item)
        )
    return out


def redact_sensitive(value: FlowExecutionEvents) -> list[Any]:
    import capo_bedrock_agent_runtime.types.flow_execution_event

    return [
        capo_bedrock_agent_runtime.types.flow_execution_event.redact_sensitive(item)
        for item in value
    ]
