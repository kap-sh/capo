"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicySummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_summary

AutomatedReasoningPolicySummaries: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_summary.AutomatedReasoningPolicySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicySummaries) -> list:
    import capo_bedrock.types.automated_reasoning_policy_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicySummaries:
    import capo_bedrock.types.automated_reasoning_policy_summary

    out: AutomatedReasoningPolicySummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicySummaries) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_summary

    return [
        capo_bedrock.types.automated_reasoning_policy_summary.redact_sensitive(item)
        for item in value
    ]
