"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessTools``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_tool

HarnessTools: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.harness_tool.HarnessTool"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTools) -> list:
    import capo_bedrock_agentcore_control.types.harness_tool

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.harness_tool.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarnessTools:
    import capo_bedrock_agentcore_control.types.harness_tool

    out: HarnessTools = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.harness_tool.deserialize_json(item)
        )
    return out


def redact_sensitive(value: HarnessTools) -> list[Any]:
    import capo_bedrock_agentcore_control.types.harness_tool

    return [
        capo_bedrock_agentcore_control.types.harness_tool.redact_sensitive(item)
        for item in value
    ]
