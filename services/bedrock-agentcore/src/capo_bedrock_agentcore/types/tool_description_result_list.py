"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionResultList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.tool_description_output

ToolDescriptionResultList: TypeAlias = list[
    "capo_bedrock_agentcore.types.tool_description_output.ToolDescriptionOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionResultList) -> list:
    import capo_bedrock_agentcore.types.tool_description_output

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.tool_description_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ToolDescriptionResultList:
    import capo_bedrock_agentcore.types.tool_description_output

    out: ToolDescriptionResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.tool_description_output.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ToolDescriptionResultList) -> list[Any]:
    import capo_bedrock_agentcore.types.tool_description_output

    return [
        capo_bedrock_agentcore.types.tool_description_output.redact_sensitive(item)
        for item in value
    ]
