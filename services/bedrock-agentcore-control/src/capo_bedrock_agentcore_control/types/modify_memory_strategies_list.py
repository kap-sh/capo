"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyMemoryStrategiesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.modify_memory_strategy_input

ModifyMemoryStrategiesList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.modify_memory_strategy_input.ModifyMemoryStrategyInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModifyMemoryStrategiesList) -> list:
    import capo_bedrock_agentcore_control.types.modify_memory_strategy_input

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.modify_memory_strategy_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ModifyMemoryStrategiesList:
    import capo_bedrock_agentcore_control.types.modify_memory_strategy_input

    out: ModifyMemoryStrategiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.modify_memory_strategy_input.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ModifyMemoryStrategiesList) -> list[Any]:
    import capo_bedrock_agentcore_control.types.modify_memory_strategy_input

    return [
        capo_bedrock_agentcore_control.types.modify_memory_strategy_input.redact_sensitive(
            item
        )
        for item in value
    ]
