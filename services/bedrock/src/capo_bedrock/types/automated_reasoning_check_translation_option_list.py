"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckTranslationOptionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_translation_option

AutomatedReasoningCheckTranslationOptionList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_check_translation_option.AutomatedReasoningCheckTranslationOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckTranslationOptionList) -> list:
    import capo_bedrock.types.automated_reasoning_check_translation_option

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_check_translation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckTranslationOptionList:
    import capo_bedrock.types.automated_reasoning_check_translation_option

    out: AutomatedReasoningCheckTranslationOptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_check_translation_option.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningCheckTranslationOptionList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_check_translation_option

    return [
        capo_bedrock.types.automated_reasoning_check_translation_option.redact_sensitive(
            item
        )
        for item in value
    ]
