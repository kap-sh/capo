"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyMemoryStrategies``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.delete_memory_strategies_list
    import capo_bedrock_agentcore_control.types.memory_strategy_input_list
    import capo_bedrock_agentcore_control.types.modify_memory_strategies_list


class ModifyMemoryStrategies(TypedDict, closed=True):
    add_memory_strategies: NotRequired[
        "capo_bedrock_agentcore_control.types.memory_strategy_input_list.MemoryStrategyInputList"
    ]
    """<p>The list of memory strategies to add.</p>"""
    modify_memory_strategies: NotRequired[
        "capo_bedrock_agentcore_control.types.modify_memory_strategies_list.ModifyMemoryStrategiesList"
    ]
    """<p>The list of memory strategies to modify.</p>"""
    delete_memory_strategies: NotRequired[
        "capo_bedrock_agentcore_control.types.delete_memory_strategies_list.DeleteMemoryStrategiesList"
    ]
    """<p>The list of memory strategies to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifyMemoryStrategies) -> dict:
    out: dict = {}
    if "add_memory_strategies" in value:
        import capo_bedrock_agentcore_control.types.memory_strategy_input_list

        out["addMemoryStrategies"] = (
            capo_bedrock_agentcore_control.types.memory_strategy_input_list.serialize_json(
                value["add_memory_strategies"]
            )
        )
    if "modify_memory_strategies" in value:
        import capo_bedrock_agentcore_control.types.modify_memory_strategies_list

        out["modifyMemoryStrategies"] = (
            capo_bedrock_agentcore_control.types.modify_memory_strategies_list.serialize_json(
                value["modify_memory_strategies"]
            )
        )
    if "delete_memory_strategies" in value:
        import capo_bedrock_agentcore_control.types.delete_memory_strategies_list

        out["deleteMemoryStrategies"] = (
            capo_bedrock_agentcore_control.types.delete_memory_strategies_list.serialize_json(
                value["delete_memory_strategies"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModifyMemoryStrategies:
    out: ModifyMemoryStrategies = {}  # type: ignore[typeddict-item]
    if data.get("addMemoryStrategies") is not None:
        import capo_bedrock_agentcore_control.types.memory_strategy_input_list

        out["add_memory_strategies"] = (
            capo_bedrock_agentcore_control.types.memory_strategy_input_list.deserialize_json(
                data["addMemoryStrategies"]
            )
        )
    if data.get("modifyMemoryStrategies") is not None:
        import capo_bedrock_agentcore_control.types.modify_memory_strategies_list

        out["modify_memory_strategies"] = (
            capo_bedrock_agentcore_control.types.modify_memory_strategies_list.deserialize_json(
                data["modifyMemoryStrategies"]
            )
        )
    if data.get("deleteMemoryStrategies") is not None:
        import capo_bedrock_agentcore_control.types.delete_memory_strategies_list

        out["delete_memory_strategies"] = (
            capo_bedrock_agentcore_control.types.delete_memory_strategies_list.deserialize_json(
                data["deleteMemoryStrategies"]
            )
        )
    return out


def redact_sensitive(value: ModifyMemoryStrategies) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "add_memory_strategies" in value:
        import capo_bedrock_agentcore_control.types.memory_strategy_input_list

        out["add_memory_strategies"] = (
            capo_bedrock_agentcore_control.types.memory_strategy_input_list.redact_sensitive(
                value["add_memory_strategies"]
            )
        )
    if "modify_memory_strategies" in value:
        import capo_bedrock_agentcore_control.types.modify_memory_strategies_list

        out["modify_memory_strategies"] = (
            capo_bedrock_agentcore_control.types.modify_memory_strategies_list.redact_sensitive(
                value["modify_memory_strategies"]
            )
        )
    return out
