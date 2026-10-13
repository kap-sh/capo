"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultContentBlocks``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tool_result_content_block

ToolResultContentBlocks: TypeAlias = list[
    "capo_bedrock_runtime.types.tool_result_content_block.ToolResultContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultContentBlocks) -> list:
    import capo_bedrock_runtime.types.tool_result_content_block

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.tool_result_content_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ToolResultContentBlocks:
    import capo_bedrock_runtime.types.tool_result_content_block

    out: ToolResultContentBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.tool_result_content_block.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ToolResultContentBlocks) -> list[Any]:
    import capo_bedrock_runtime.types.tool_result_content_block

    return [
        capo_bedrock_runtime.types.tool_result_content_block.redact_sensitive(item)
        for item in value
    ]
