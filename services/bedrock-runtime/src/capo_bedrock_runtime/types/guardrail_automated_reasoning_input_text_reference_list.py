"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningInputTextReferenceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference

GuardrailAutomatedReasoningInputTextReferenceList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference.GuardrailAutomatedReasoningInputTextReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningInputTextReferenceList) -> list:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailAutomatedReasoningInputTextReferenceList:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference

    out: GuardrailAutomatedReasoningInputTextReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: GuardrailAutomatedReasoningInputTextReferenceList,
) -> list[Any]:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference

    return [
        capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference.redact_sensitive(
            item
        )
        for item in value
    ]
