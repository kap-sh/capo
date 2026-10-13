"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailManagedWordsConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_managed_words_type
    import capo_bedrock.types.guardrail_word_action


class GuardrailManagedWordsConfig(TypedDict, closed=True):
    type: "capo_bedrock.types.guardrail_managed_words_type.GuardrailManagedWordsType"
    """<p>The managed word type to configure for the guardrail.</p>"""
    input_action: NotRequired[
        "capo_bedrock.types.guardrail_word_action.GuardrailWordAction"
    ]
    """<p>Specifies the action to take when harmful content is detected in the input. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    output_action: NotRequired[
        "capo_bedrock.types.guardrail_word_action.GuardrailWordAction"
    ]
    """<p>Specifies the action to take when harmful content is detected in the output. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    input_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""
    output_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordsConfig) -> dict:
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


def deserialize_json(data: dict) -> GuardrailManagedWordsConfig:
    out: GuardrailManagedWordsConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock.types.guardrail_managed_words_type

        out["type"] = capo_bedrock.types.guardrail_managed_words_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GuardrailManagedWordsConfig.type required")
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


def redact_sensitive(value: GuardrailManagedWordsConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_action" in value:
        out["input_action"] = "*** Sensitive Data Redacted ***"
    if "output_action" in value:
        out["output_action"] = "*** Sensitive Data Redacted ***"
    return out
