"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyInputList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.memory_strategy_input

MemoryStrategyInputList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.memory_strategy_input.MemoryStrategyInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryStrategyInputList) -> list:
    import capo_bedrock_agentcore_control.types.memory_strategy_input

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.memory_strategy_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemoryStrategyInputList:
    import capo_bedrock_agentcore_control.types.memory_strategy_input

    out: MemoryStrategyInputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.memory_strategy_input.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: MemoryStrategyInputList) -> list[Any]:
    import capo_bedrock_agentcore_control.types.memory_strategy_input

    return [
        capo_bedrock_agentcore_control.types.memory_strategy_input.redact_sensitive(
            item
        )
        for item in value
    ]
