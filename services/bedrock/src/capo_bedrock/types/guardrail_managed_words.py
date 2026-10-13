"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailManagedWords``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_managed_words_type
    import capo_bedrock.types.guardrail_word_action


class GuardrailManagedWords(TypedDict, closed=True):
    type: "capo_bedrock.types.guardrail_managed_words_type.GuardrailManagedWordsType"
    """<p>ManagedWords$type The managed word type that was configured for the guardrail. (For now, we only offer profanity word list)</p>"""
    input_action: NotRequired[
        "capo_bedrock.types.guardrail_word_action.GuardrailWordAction"
    ]
    """<p>The action to take when harmful content is detected in the input. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    output_action: NotRequired[
        "capo_bedrock.types.guardrail_word_action.GuardrailWordAction"
    ]
    """<p>The action to take when harmful content is detected in the output. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    input_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""
    output_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWords) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_managed_words_type

    out["type"] = capo_bedrock.types.guardrail_managed_words_type.serialize_json(
        value["type"]
    )
    if "input_action" in value:
        import capo_bedrock.types.guardrail_word_action

        out["inputAction"] = capo_bedrock.types.guardrail_word_action.serialize_json(
            value["input_action"]
        )
    if "output_action" in value:
        import capo_bedrock.types.guardrail_word_action

        out["outputAction"] = capo_bedrock.types.guardrail_word_action.serialize_json(
            value["output_action"]
        )
    if "input_enabled" in value:
        out["inputEnabled"] = value["input_enabled"]
    if "output_enabled" in value:
        out["outputEnabled"] = value["output_enabled"]
    return out


def deserialize_json(data: dict) -> GuardrailManagedWords:
    out: GuardrailManagedWords = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock.types.guardrail_managed_words_type

        out["type"] = capo_bedrock.types.guardrail_managed_words_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GuardrailManagedWords.type required")
    if data.get("inputAction") is not None:
        import capo_bedrock.types.guardrail_word_action

        out["input_action"] = capo_bedrock.types.guardrail_word_action.deserialize_json(
            data["inputAction"]
        )
    if data.get("outputAction") is not None:
        import capo_bedrock.types.guardrail_word_action

        out["output_action"] = (
            capo_bedrock.types.guardrail_word_action.deserialize_json(
                data["outputAction"]
            )
        )
    if data.get("inputEnabled") is not None:
        out["input_enabled"] = data["inputEnabled"]
    if data.get("outputEnabled") is not None:
        out["output_enabled"] = data["outputEnabled"]
    return out


def redact_sensitive(value: GuardrailManagedWords) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_action" in value:
        out["input_action"] = "*** Sensitive Data Redacted ***"
    if "output_action" in value:
        out["output_action"] = "*** Sensitive Data Redacted ***"
    return out
