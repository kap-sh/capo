"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedContentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotated_content

AutomatedReasoningPolicyAnnotatedContentList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_annotated_content.AutomatedReasoningPolicyAnnotatedContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedContentList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_annotated_content

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_annotated_content.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyAnnotatedContentList:
    import capo_bedrock.types.automated_reasoning_policy_annotated_content

    out: AutomatedReasoningPolicyAnnotatedContentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_annotated_content.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyAnnotatedContentList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_annotated_content

    return [
        capo_bedrock.types.automated_reasoning_policy_annotated_content.redact_sensitive(
            item
        )
        for item in value
    ]
