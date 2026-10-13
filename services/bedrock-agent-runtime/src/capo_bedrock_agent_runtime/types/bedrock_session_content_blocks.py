"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockSessionContentBlocks``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.bedrock_session_content_block

BedrockSessionContentBlocks: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.bedrock_session_content_block.BedrockSessionContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: BedrockSessionContentBlocks) -> list:
    import capo_bedrock_agent_runtime.types.bedrock_session_content_block

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.bedrock_session_content_block.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BedrockSessionContentBlocks:
    import capo_bedrock_agent_runtime.types.bedrock_session_content_block

    out: BedrockSessionContentBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.bedrock_session_content_block.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: BedrockSessionContentBlocks) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
