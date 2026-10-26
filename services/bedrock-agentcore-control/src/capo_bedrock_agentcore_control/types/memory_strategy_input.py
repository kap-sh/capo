"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_memory_strategy_input
    import capo_bedrock_agentcore_control.types.episodic_memory_strategy_input
    import capo_bedrock_agentcore_control.types.semantic_memory_strategy_input
    import capo_bedrock_agentcore_control.types.summary_memory_strategy_input
    import capo_bedrock_agentcore_control.types.user_preference_memory_strategy_input


class _MemoryStrategyInput_semanticMemoryStrategy(TypedDict, closed=True):
    semanticMemoryStrategy: "capo_bedrock_agentcore_control.types.semantic_memory_strategy_input.SemanticMemoryStrategyInput"


class _MemoryStrategyInput_summaryMemoryStrategy(TypedDict, closed=True):
    summaryMemoryStrategy: "capo_bedrock_agentcore_control.types.summary_memory_strategy_input.SummaryMemoryStrategyInput"


class _MemoryStrategyInput_userPreferenceMemoryStrategy(TypedDict, closed=True):
    userPreferenceMemoryStrategy: "capo_bedrock_agentcore_control.types.user_preference_memory_strategy_input.UserPreferenceMemoryStrategyInput"


class _MemoryStrategyInput_customMemoryStrategy(TypedDict, closed=True):
    customMemoryStrategy: "capo_bedrock_agentcore_control.types.custom_memory_strategy_input.CustomMemoryStrategyInput"


class _MemoryStrategyInput_episodicMemoryStrategy(TypedDict, closed=True):
    episodicMemoryStrategy: "capo_bedrock_agentcore_control.types.episodic_memory_strategy_input.EpisodicMemoryStrategyInput"


MemoryStrategyInput: TypeAlias = (
    _MemoryStrategyInput_semanticMemoryStrategy
    | _MemoryStrategyInput_summaryMemoryStrategy
    | _MemoryStrategyInput_userPreferenceMemoryStrategy
    | _MemoryStrategyInput_customMemoryStrategy
    | _MemoryStrategyInput_episodicMemoryStrategy
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MemoryStrategyInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MemoryStrategyInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "semanticMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.semantic_memory_strategy_input

        return {
            "semanticMemoryStrategy": capo_bedrock_agentcore_control.types.semantic_memory_strategy_input.serialize_json(
                value["semanticMemoryStrategy"]
            )
        }
    elif "summaryMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.summary_memory_strategy_input

        return {
            "summaryMemoryStrategy": capo_bedrock_agentcore_control.types.summary_memory_strategy_input.serialize_json(
                value["summaryMemoryStrategy"]
            )
        }
    elif "userPreferenceMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.user_preference_memory_strategy_input

        return {
            "userPreferenceMemoryStrategy": capo_bedrock_agentcore_control.types.user_preference_memory_strategy_input.serialize_json(
                value["userPreferenceMemoryStrategy"]
            )
        }
    elif "customMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.custom_memory_strategy_input

        return {
            "customMemoryStrategy": capo_bedrock_agentcore_control.types.custom_memory_strategy_input.serialize_json(
                value["customMemoryStrategy"]
            )
        }
    elif "episodicMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.episodic_memory_strategy_input

        return {
            "episodicMemoryStrategy": capo_bedrock_agentcore_control.types.episodic_memory_strategy_input.serialize_json(
                value["episodicMemoryStrategy"]
            )
        }
    else:
        raise SerializationError("MemoryStrategyInput: no variant present")


def deserialize_json(data: dict) -> MemoryStrategyInput:
    if data.get("semanticMemoryStrategy") is not None:
        import capo_bedrock_agentcore_control.types.semantic_memory_strategy_input

        return {
            "semanticMemoryStrategy": capo_bedrock_agentcore_control.types.semantic_memory_strategy_input.deserialize_json(
                data["semanticMemoryStrategy"]
            )
        }
    elif data.get("summaryMemoryStrategy") is not None:
        import capo_bedrock_agentcore_control.types.summary_memory_strategy_input

        return {
            "summaryMemoryStrategy": capo_bedrock_agentcore_control.types.summary_memory_strategy_input.deserialize_json(
                data["summaryMemoryStrategy"]
            )
        }
    elif data.get("userPreferenceMemoryStrategy") is not None:
        import capo_bedrock_agentcore_control.types.user_preference_memory_strategy_input

        return {
            "userPreferenceMemoryStrategy": capo_bedrock_agentcore_control.types.user_preference_memory_strategy_input.deserialize_json(
                data["userPreferenceMemoryStrategy"]
            )
        }
    elif data.get("customMemoryStrategy") is not None:
        import capo_bedrock_agentcore_control.types.custom_memory_strategy_input

        return {
            "customMemoryStrategy": capo_bedrock_agentcore_control.types.custom_memory_strategy_input.deserialize_json(
                data["customMemoryStrategy"]
            )
        }
    elif data.get("episodicMemoryStrategy") is not None:
        import capo_bedrock_agentcore_control.types.episodic_memory_strategy_input

        return {
            "episodicMemoryStrategy": capo_bedrock_agentcore_control.types.episodic_memory_strategy_input.deserialize_json(
                data["episodicMemoryStrategy"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MemoryStrategyInput: no recognized variant key")


def redact_sensitive(value: MemoryStrategyInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "semanticMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.semantic_memory_strategy_input

        out["semanticMemoryStrategy"] = (
            capo_bedrock_agentcore_control.types.semantic_memory_strategy_input.redact_sensitive(
                value["semanticMemoryStrategy"]
            )
        )
    if "summaryMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.summary_memory_strategy_input

        out["summaryMemoryStrategy"] = (
            capo_bedrock_agentcore_control.types.summary_memory_strategy_input.redact_sensitive(
                value["summaryMemoryStrategy"]
            )
        )
    if "userPreferenceMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.user_preference_memory_strategy_input

        out["userPreferenceMemoryStrategy"] = (
            capo_bedrock_agentcore_control.types.user_preference_memory_strategy_input.redact_sensitive(
                value["userPreferenceMemoryStrategy"]
            )
        )
    if "customMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.custom_memory_strategy_input

        out["customMemoryStrategy"] = (
            capo_bedrock_agentcore_control.types.custom_memory_strategy_input.redact_sensitive(
                value["customMemoryStrategy"]
            )
        )
    if "episodicMemoryStrategy" in value:
        import capo_bedrock_agentcore_control.types.episodic_memory_strategy_input

        out["episodicMemoryStrategy"] = (
            capo_bedrock_agentcore_control.types.episodic_memory_strategy_input.redact_sensitive(
                value["episodicMemoryStrategy"]
            )
        )
    return out
