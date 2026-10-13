"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ToolDefinitions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.tool_definition

ToolDefinitions: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.tool_definition.ToolDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolDefinitions) -> list:
    import capo_bedrock_agentcore_control.types.tool_definition

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.tool_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ToolDefinitions:
    import capo_bedrock_agentcore_control.types.tool_definition

    out: ToolDefinitions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.tool_definition.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ToolDefinitions) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
