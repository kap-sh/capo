"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceConditions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_trace_condition

FlowTraceConditions: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.flow_trace_condition.FlowTraceCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceConditions) -> list:
    import capo_bedrock_agent_runtime.types.flow_trace_condition

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FlowTraceConditions:
    import capo_bedrock_agent_runtime.types.flow_trace_condition

    out: FlowTraceConditions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_condition.deserialize_json(item)
        )
    return out


def redact_sensitive(value: FlowTraceConditions) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
