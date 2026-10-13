"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningTranslationOption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_list


class GuardrailAutomatedReasoningTranslationOption(TypedDict, closed=True):
    translations: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_list.GuardrailAutomatedReasoningTranslationList"
    ]
    """<p>Example translations that provide this possible interpretation of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningTranslationOption) -> dict:
    out: dict = {}
    if "translations" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_list

        out["translations"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_list.serialize_json(
                value["translations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningTranslationOption:
    out: GuardrailAutomatedReasoningTranslationOption = {}  # type: ignore[typeddict-item]
    if data.get("translations") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_list

        out["translations"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_list.deserialize_json(
                data["translations"]
            )
        )
    return out


def redact_sensitive(
    value: GuardrailAutomatedReasoningTranslationOption,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "translations" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_list

        out["translations"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_list.redact_sensitive(
                value["translations"]
            )
        )
    return out
