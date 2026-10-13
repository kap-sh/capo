"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotation

AutomatedReasoningPolicyAnnotationList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_annotation.AutomatedReasoningPolicyAnnotation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotationList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_annotation

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_annotation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyAnnotationList:
    import capo_bedrock.types.automated_reasoning_policy_annotation

    out: AutomatedReasoningPolicyAnnotationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_annotation.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyAnnotationList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_annotation

    return [
        capo_bedrock.types.automated_reasoning_policy_annotation.redact_sensitive(item)
        for item in value
    ]
