"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailWordPolicyConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_managed_word_lists_config
    import capo_qconnect.types.guardrail_words_config


class AIGuardrailWordPolicyConfig(TypedDict, closed=True):
    words_config: NotRequired[
        "capo_qconnect.types.guardrail_words_config.GuardrailWordsConfig"
    ]
    """<p>A list of words to configure for the AI Guardrail.</p>"""
    managed_word_lists_config: NotRequired[
        "capo_qconnect.types.guardrail_managed_word_lists_config.GuardrailManagedWordListsConfig"
    ]
    """<p>A list of managed words to configure for the AI Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailWordPolicyConfig) -> dict:
    out: dict = {}
    if "words_config" in value:
        import capo_qconnect.types.guardrail_words_config

        out["wordsConfig"] = capo_qconnect.types.guardrail_words_config.serialize_json(
            value["words_config"]
        )
    if "managed_word_lists_config" in value:
        import capo_qconnect.types.guardrail_managed_word_lists_config

        out["managedWordListsConfig"] = (
            capo_qconnect.types.guardrail_managed_word_lists_config.serialize_json(
                value["managed_word_lists_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AIGuardrailWordPolicyConfig:
    out: AIGuardrailWordPolicyConfig = {}  # type: ignore[typeddict-item]
    if data.get("wordsConfig") is not None:
        import capo_qconnect.types.guardrail_words_config

        out["words_config"] = (
            capo_qconnect.types.guardrail_words_config.deserialize_json(
                data["wordsConfig"]
            )
        )
    if data.get("managedWordListsConfig") is not None:
        import capo_qconnect.types.guardrail_managed_word_lists_config

        out["managed_word_lists_config"] = (
            capo_qconnect.types.guardrail_managed_word_lists_config.deserialize_json(
                data["managedWordListsConfig"]
            )
        )
    return out


def redact_sensitive(value: AIGuardrailWordPolicyConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "words_config" in value:
        import capo_qconnect.types.guardrail_words_config

        out["words_config"] = (
            capo_qconnect.types.guardrail_words_config.redact_sensitive(
                value["words_config"]
            )
        )
    if "managed_word_lists_config" in value:
        import capo_qconnect.types.guardrail_managed_word_lists_config

        out["managed_word_lists_config"] = (
            capo_qconnect.types.guardrail_managed_word_lists_config.redact_sensitive(
                value["managed_word_lists_config"]
            )
        )
    return out
