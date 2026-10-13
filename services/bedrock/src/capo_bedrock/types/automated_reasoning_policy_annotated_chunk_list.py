"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedChunkList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotated_chunk

AutomatedReasoningPolicyAnnotatedChunkList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_annotated_chunk.AutomatedReasoningPolicyAnnotatedChunk"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedChunkList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_annotated_chunk

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_annotated_chunk.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyAnnotatedChunkList:
    import capo_bedrock.types.automated_reasoning_policy_annotated_chunk

    out: AutomatedReasoningPolicyAnnotatedChunkList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_annotated_chunk.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyAnnotatedChunkList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_annotated_chunk

    return [
        capo_bedrock.types.automated_reasoning_policy_annotated_chunk.redact_sensitive(
            item
        )
        for item in value
    ]
