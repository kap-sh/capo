"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningTranslationOptionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_option

GuardrailAutomatedReasoningTranslationOptionList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_option.GuardrailAutomatedReasoningTranslationOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningTranslationOptionList) -> list:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_option

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningTranslationOptionList:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_option

    out: GuardrailAutomatedReasoningTranslationOptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_option.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: GuardrailAutomatedReasoningTranslationOptionList,
) -> list[Any]:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_option

    return [
        capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_option.redact_sensitive(
            item
        )
        for item in value
    ]
