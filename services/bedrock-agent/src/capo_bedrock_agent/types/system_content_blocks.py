"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SystemContentBlocks``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.system_content_block

SystemContentBlocks: TypeAlias = list[
    "capo_bedrock_agent.types.system_content_block.SystemContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: SystemContentBlocks) -> list:
    import capo_bedrock_agent.types.system_content_block

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.system_content_block.serialize_json(item))
    return out


def deserialize_json(data: list) -> SystemContentBlocks:
    import capo_bedrock_agent.types.system_content_block

    out: SystemContentBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.system_content_block.deserialize_json(item))
    return out


def redact_sensitive(value: SystemContentBlocks) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
