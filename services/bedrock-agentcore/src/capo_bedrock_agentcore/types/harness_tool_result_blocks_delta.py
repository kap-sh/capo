"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultBlocksDelta``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_tool_result_block_delta

HarnessToolResultBlocksDelta: TypeAlias = list[
    "capo_bedrock_agentcore.types.harness_tool_result_block_delta.HarnessToolResultBlockDelta"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultBlocksDelta) -> list:
    import capo_bedrock_agentcore.types.harness_tool_result_block_delta

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.harness_tool_result_block_delta.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HarnessToolResultBlocksDelta:
    import capo_bedrock_agentcore.types.harness_tool_result_block_delta

    out: HarnessToolResultBlocksDelta = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.harness_tool_result_block_delta.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: HarnessToolResultBlocksDelta) -> list[Any]:
    import capo_bedrock_agentcore.types.harness_tool_result_block_delta

    return [
        capo_bedrock_agentcore.types.harness_tool_result_block_delta.redact_sensitive(
            item
        )
        for item in value
    ]
