"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningDifferenceScenarioList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_scenario

GuardrailAutomatedReasoningDifferenceScenarioList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_automated_reasoning_scenario.GuardrailAutomatedReasoningScenario"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningDifferenceScenarioList) -> list:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_scenario

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_scenario.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningDifferenceScenarioList:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_scenario

    out: GuardrailAutomatedReasoningDifferenceScenarioList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_scenario.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: GuardrailAutomatedReasoningDifferenceScenarioList,
) -> list[Any]:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_scenario

    return [
        capo_bedrock_runtime.types.guardrail_automated_reasoning_scenario.redact_sensitive(
            item
        )
        for item in value
    ]
