"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.tool_description_input

ToolDescriptionList: TypeAlias = list[
    "capo_bedrock_agentcore.types.tool_description_input.ToolDescriptionInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionList) -> list:
    import capo_bedrock_agentcore.types.tool_description_input

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.tool_description_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ToolDescriptionList:
    import capo_bedrock_agentcore.types.tool_description_input

    out: ToolDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.tool_description_input.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ToolDescriptionList) -> list[Any]:
    import capo_bedrock_agentcore.types.tool_description_input

    return [
        capo_bedrock_agentcore.types.tool_description_input.redact_sensitive(item)
        for item in value
    ]
