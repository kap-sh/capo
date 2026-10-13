"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckInputTextReferenceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_input_text_reference

AutomatedReasoningCheckInputTextReferenceList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_check_input_text_reference.AutomatedReasoningCheckInputTextReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckInputTextReferenceList) -> list:
    import capo_bedrock.types.automated_reasoning_check_input_text_reference

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_check_input_text_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckInputTextReferenceList:
    import capo_bedrock.types.automated_reasoning_check_input_text_reference

    out: AutomatedReasoningCheckInputTextReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_check_input_text_reference.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningCheckInputTextReferenceList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_check_input_text_reference

    return [
        capo_bedrock.types.automated_reasoning_check_input_text_reference.redact_sensitive(
            item
        )
        for item in value
    ]
