"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputFields``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_field

FlowTraceNodeOutputFields: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.flow_trace_node_output_field.FlowTraceNodeOutputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputFields) -> list:
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_field

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_node_output_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FlowTraceNodeOutputFields:
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_field

    out: FlowTraceNodeOutputFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_node_output_field.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: FlowTraceNodeOutputFields) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
