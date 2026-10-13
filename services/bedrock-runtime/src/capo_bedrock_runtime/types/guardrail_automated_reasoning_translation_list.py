"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningTranslationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation

GuardrailAutomatedReasoningTranslationList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_automated_reasoning_translation.GuardrailAutomatedReasoningTranslation"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningTranslationList) -> list:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningTranslationList:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation

    out: GuardrailAutomatedReasoningTranslationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: GuardrailAutomatedReasoningTranslationList) -> list[Any]:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation

    return [
        capo_bedrock_runtime.types.guardrail_automated_reasoning_translation.redact_sensitive(
            item
        )
        for item in value
    ]
