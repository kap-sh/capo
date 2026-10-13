"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowOutputFields``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_output_field

FlowOutputFields: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.flow_output_field.FlowOutputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowOutputFields) -> list:
    import capo_bedrock_agent_runtime.types.flow_output_field

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.flow_output_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FlowOutputFields:
    import capo_bedrock_agent_runtime.types.flow_output_field

    out: FlowOutputFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.flow_output_field.deserialize_json(item)
        )
    return out


def redact_sensitive(value: FlowOutputFields) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
