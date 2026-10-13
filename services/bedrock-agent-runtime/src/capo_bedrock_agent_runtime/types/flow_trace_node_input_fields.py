"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputFields``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_field

FlowTraceNodeInputFields: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.flow_trace_node_input_field.FlowTraceNodeInputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputFields) -> list:
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_field

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_node_input_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FlowTraceNodeInputFields:
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_field

    out: FlowTraceNodeInputFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_node_input_field.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: FlowTraceNodeInputFields) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
