"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessSystemPrompt``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_system_content_block

HarnessSystemPrompt: TypeAlias = list[
    "capo_bedrock_agentcore.types.harness_system_content_block.HarnessSystemContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSystemPrompt) -> list:
    import capo_bedrock_agentcore.types.harness_system_content_block

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.harness_system_content_block.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HarnessSystemPrompt:
    import capo_bedrock_agentcore.types.harness_system_content_block

    out: HarnessSystemPrompt = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.harness_system_content_block.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: HarnessSystemPrompt) -> list[Any]:
    import capo_bedrock_agentcore.types.harness_system_content_block

    return [
        capo_bedrock_agentcore.types.harness_system_content_block.redact_sensitive(item)
        for item in value
    ]
