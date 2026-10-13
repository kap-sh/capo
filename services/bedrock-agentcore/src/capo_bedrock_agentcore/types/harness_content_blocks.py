"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlocks``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_content_block

HarnessContentBlocks: TypeAlias = list[
    "capo_bedrock_agentcore.types.harness_content_block.HarnessContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlocks) -> list:
    import capo_bedrock_agentcore.types.harness_content_block

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.harness_content_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarnessContentBlocks:
    import capo_bedrock_agentcore.types.harness_content_block

    out: HarnessContentBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.harness_content_block.deserialize_json(item)
        )
    return out


def redact_sensitive(value: HarnessContentBlocks) -> list[Any]:
    import capo_bedrock_agentcore.types.harness_content_block

    return [
        capo_bedrock_agentcore.types.harness_content_block.redact_sensitive(item)
        for item in value
    ]
