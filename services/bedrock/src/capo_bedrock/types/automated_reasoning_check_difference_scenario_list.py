"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckDifferenceScenarioList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_scenario

AutomatedReasoningCheckDifferenceScenarioList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_check_scenario.AutomatedReasoningCheckScenario"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckDifferenceScenarioList) -> list:
    import capo_bedrock.types.automated_reasoning_check_scenario

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_check_scenario.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckDifferenceScenarioList:
    import capo_bedrock.types.automated_reasoning_check_scenario

    out: AutomatedReasoningCheckDifferenceScenarioList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_check_scenario.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AutomatedReasoningCheckDifferenceScenarioList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_check_scenario

    return [
        capo_bedrock.types.automated_reasoning_check_scenario.redact_sensitive(item)
        for item in value
    ]
