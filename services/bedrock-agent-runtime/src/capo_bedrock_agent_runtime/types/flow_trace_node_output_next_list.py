"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputNextList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_next

FlowTraceNodeOutputNextList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.flow_trace_node_output_next.FlowTraceNodeOutputNext"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputNextList) -> list:
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_next

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_node_output_next.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FlowTraceNodeOutputNextList:
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_next

    out: FlowTraceNodeOutputNextList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_node_output_next.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: FlowTraceNodeOutputNextList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
