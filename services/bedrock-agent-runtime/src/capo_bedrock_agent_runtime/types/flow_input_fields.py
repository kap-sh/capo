"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInputFields``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_input_field

FlowInputFields: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.flow_input_field.FlowInputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowInputFields) -> list:
    import capo_bedrock_agent_runtime.types.flow_input_field

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.flow_input_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FlowInputFields:
    import capo_bedrock_agent_runtime.types.flow_input_field

    out: FlowInputFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.flow_input_field.deserialize_json(item)
        )
    return out


def redact_sensitive(value: FlowInputFields) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
