"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckTranslationOption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_translation_list


class AutomatedReasoningCheckTranslationOption(TypedDict, closed=True):
    translations: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_translation_list.AutomatedReasoningCheckTranslationList"
    ]
    """<p>Different logical interpretations that were detected during translation of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckTranslationOption) -> dict:
    out: dict = {}
    if "translations" in value:
        import capo_bedrock.types.automated_reasoning_check_translation_list

        out["translations"] = (
            capo_bedrock.types.automated_reasoning_check_translation_list.serialize_json(
                value["translations"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckTranslationOption:
    out: AutomatedReasoningCheckTranslationOption = {}  # type: ignore[typeddict-item]
    if data.get("translations") is not None:
        import capo_bedrock.types.automated_reasoning_check_translation_list

        out["translations"] = (
            capo_bedrock.types.automated_reasoning_check_translation_list.deserialize_json(
                data["translations"]
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningCheckTranslationOption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "translations" in value:
        import capo_bedrock.types.automated_reasoning_check_translation_list

        out["translations"] = (
            capo_bedrock.types.automated_reasoning_check_translation_list.redact_sensitive(
                value["translations"]
            )
        )
    return out
