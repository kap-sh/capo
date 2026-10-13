"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_validation

FlowValidations: TypeAlias = list[
    "capo_bedrock_agent.types.flow_validation.FlowValidation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowValidations) -> list:
    import capo_bedrock_agent.types.flow_validation

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.flow_validation.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowValidations:
    import capo_bedrock_agent.types.flow_validation

    out: FlowValidations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.flow_validation.deserialize_json(item))
    return out


def redact_sensitive(value: FlowValidations) -> list[Any]:
    import capo_bedrock_agent.types.flow_validation

    return [
        capo_bedrock_agent.types.flow_validation.redact_sensitive(item)
        for item in value
    ]
