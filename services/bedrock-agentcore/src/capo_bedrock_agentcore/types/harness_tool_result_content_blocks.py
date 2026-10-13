"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultContentBlocks``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_tool_result_content_block

HarnessToolResultContentBlocks: TypeAlias = list[
    "capo_bedrock_agentcore.types.harness_tool_result_content_block.HarnessToolResultContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultContentBlocks) -> list:
    import capo_bedrock_agentcore.types.harness_tool_result_content_block

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.harness_tool_result_content_block.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HarnessToolResultContentBlocks:
    import capo_bedrock_agentcore.types.harness_tool_result_content_block

    out: HarnessToolResultContentBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.harness_tool_result_content_block.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: HarnessToolResultContentBlocks) -> list[Any]:
    import capo_bedrock_agentcore.types.harness_tool_result_content_block

    return [
        capo_bedrock_agentcore.types.harness_tool_result_content_block.redact_sensitive(
            item
        )
        for item in value
    ]
