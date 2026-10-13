"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildStepList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_step

AutomatedReasoningPolicyBuildStepList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_build_step.AutomatedReasoningPolicyBuildStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildStepList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_build_step

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_step.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyBuildStepList:
    import capo_bedrock.types.automated_reasoning_policy_build_step

    out: AutomatedReasoningPolicyBuildStepList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_step.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyBuildStepList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_build_step

    return [
        capo_bedrock.types.automated_reasoning_policy_build_step.redact_sensitive(item)
        for item in value
    ]
