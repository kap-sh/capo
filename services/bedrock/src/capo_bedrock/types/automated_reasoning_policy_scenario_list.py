"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyScenarioList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_scenario

AutomatedReasoningPolicyScenarioList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_scenario.AutomatedReasoningPolicyScenario"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyScenarioList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_scenario

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_scenario.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyScenarioList:
    import capo_bedrock.types.automated_reasoning_policy_scenario

    out: AutomatedReasoningPolicyScenarioList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_scenario.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyScenarioList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_scenario

    return [
        capo_bedrock.types.automated_reasoning_policy_scenario.redact_sensitive(item)
        for item in value
    ]
