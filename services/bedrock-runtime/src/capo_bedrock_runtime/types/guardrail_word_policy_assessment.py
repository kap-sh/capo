"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailWordPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_custom_word_list
    import capo_bedrock_runtime.types.guardrail_managed_word_list


class GuardrailWordPolicyAssessment(TypedDict, closed=True):
    custom_words: (
        "capo_bedrock_runtime.types.guardrail_custom_word_list.GuardrailCustomWordList"
    )
    """<p>Custom words in the assessment.</p>"""
    managed_word_lists: "capo_bedrock_runtime.types.guardrail_managed_word_list.GuardrailManagedWordList"
    """<p>Managed word lists in the assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordPolicyAssessment) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_custom_word_list

    out["customWords"] = (
        capo_bedrock_runtime.types.guardrail_custom_word_list.serialize_json(
            value["custom_words"]
        )
    )
    import capo_bedrock_runtime.types.guardrail_managed_word_list

    out["managedWordLists"] = (
        capo_bedrock_runtime.types.guardrail_managed_word_list.serialize_json(
            value["managed_word_lists"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailWordPolicyAssessment:
    out: GuardrailWordPolicyAssessment = {}  # type: ignore[typeddict-item]
    if data.get("customWords") is not None:
        import capo_bedrock_runtime.types.guardrail_custom_word_list

        out["custom_words"] = (
            capo_bedrock_runtime.types.guardrail_custom_word_list.deserialize_json(
                data["customWords"]
            )
        )
    else:
        out["custom_words"] = []
    if data.get("managedWordLists") is not None:
        import capo_bedrock_runtime.types.guardrail_managed_word_list

        out["managed_word_lists"] = (
            capo_bedrock_runtime.types.guardrail_managed_word_list.deserialize_json(
                data["managedWordLists"]
            )
        )
    else:
        out["managed_word_lists"] = []
    return out
