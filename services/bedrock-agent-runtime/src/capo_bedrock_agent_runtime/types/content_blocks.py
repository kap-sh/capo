"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ContentBlocks``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.content_block

ContentBlocks: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.content_block.ContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlocks) -> list:
    import capo_bedrock_agent_runtime.types.content_block

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.content_block.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContentBlocks:
    import capo_bedrock_agent_runtime.types.content_block

    out: ContentBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.content_block.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ContentBlocks) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
