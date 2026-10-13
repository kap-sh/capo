"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailWordPolicy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_managed_word_lists
    import capo_bedrock.types.guardrail_words


class GuardrailWordPolicy(TypedDict, closed=True):
    words: NotRequired["capo_bedrock.types.guardrail_words.GuardrailWords"]
    """<p>A list of words configured for the guardrail.</p>"""
    managed_word_lists: NotRequired[
        "capo_bedrock.types.guardrail_managed_word_lists.GuardrailManagedWordLists"
    ]
    """<p>A list of managed words configured for the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordPolicy) -> dict:
    out: dict = {}
    if "words" in value:
        import capo_bedrock.types.guardrail_words

        out["words"] = capo_bedrock.types.guardrail_words.serialize_json(value["words"])
    if "managed_word_lists" in value:
        import capo_bedrock.types.guardrail_managed_word_lists

        out["managedWordLists"] = (
            capo_bedrock.types.guardrail_managed_word_lists.serialize_json(
                value["managed_word_lists"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailWordPolicy:
    out: GuardrailWordPolicy = {}  # type: ignore[typeddict-item]
    if data.get("words") is not None:
        import capo_bedrock.types.guardrail_words

        out["words"] = capo_bedrock.types.guardrail_words.deserialize_json(
            data["words"]
        )
    if data.get("managedWordLists") is not None:
        import capo_bedrock.types.guardrail_managed_word_lists

        out["managed_word_lists"] = (
            capo_bedrock.types.guardrail_managed_word_lists.deserialize_json(
                data["managedWordLists"]
            )
        )
    return out


def redact_sensitive(value: GuardrailWordPolicy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "words" in value:
        import capo_bedrock.types.guardrail_words

        out["words"] = capo_bedrock.types.guardrail_words.redact_sensitive(
            value["words"]
        )
    if "managed_word_lists" in value:
        import capo_bedrock.types.guardrail_managed_word_lists

        out["managed_word_lists"] = (
            capo_bedrock.types.guardrail_managed_word_lists.redact_sensitive(
                value["managed_word_lists"]
            )
        )
    return out
