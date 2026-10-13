"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Functions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.function_definition

Functions: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.function_definition.FunctionDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: Functions) -> list:
    import capo_bedrock_agent_runtime.types.function_definition

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.function_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Functions:
    import capo_bedrock_agent_runtime.types.function_definition

    out: Functions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.function_definition.deserialize_json(item)
        )
    return out


def redact_sensitive(value: Functions) -> list[Any]:
    import capo_bedrock_agent_runtime.types.function_definition

    return [
        capo_bedrock_agent_runtime.types.function_definition.redact_sensitive(item)
        for item in value
    ]
