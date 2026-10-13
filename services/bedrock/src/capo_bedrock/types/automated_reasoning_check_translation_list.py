"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckTranslationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_translation

AutomatedReasoningCheckTranslationList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_check_translation.AutomatedReasoningCheckTranslation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckTranslationList) -> list:
    import capo_bedrock.types.automated_reasoning_check_translation

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_check_translation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckTranslationList:
    import capo_bedrock.types.automated_reasoning_check_translation

    out: AutomatedReasoningCheckTranslationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_check_translation.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningCheckTranslationList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_check_translation

    return [
        capo_bedrock.types.automated_reasoning_check_translation.redact_sensitive(item)
        for item in value
    ]
