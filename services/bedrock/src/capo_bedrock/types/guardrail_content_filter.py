"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_content_filter_action
    import capo_bedrock.types.guardrail_content_filter_type
    import capo_bedrock.types.guardrail_filter_strength
    import capo_bedrock.types.guardrail_modalities


class GuardrailContentFilter(TypedDict, closed=True):
    type: "capo_bedrock.types.guardrail_content_filter_type.GuardrailContentFilterType"
    """<p>The harmful category that the content filter is applied to.</p>"""
    input_strength: (
        "capo_bedrock.types.guardrail_filter_strength.GuardrailFilterStrength"
    )
    """<p>The strength of the content filter to apply to prompts. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.</p>"""
    output_strength: (
        "capo_bedrock.types.guardrail_filter_strength.GuardrailFilterStrength"
    )
    """<p>The strength of the content filter to apply to model responses. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.</p>"""
    input_modalities: NotRequired[
        "capo_bedrock.types.guardrail_modalities.GuardrailModalities"
    ]
    """<p>The input modalities selected for the guardrail content filter.</p>"""
    output_modalities: NotRequired[
        "capo_bedrock.types.guardrail_modalities.GuardrailModalities"
    ]
    """<p>The output modalities selected for the guardrail content filter.</p>"""
    input_action: NotRequired[
        "capo_bedrock.types.guardrail_content_filter_action.GuardrailContentFilterAction"
    ]
    """<p>The action to take when harmful content is detected in the input. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    output_action: NotRequired[
        "capo_bedrock.types.guardrail_content_filter_action.GuardrailContentFilterAction"
    ]
    """<p>The action to take when harmful content is detected in the output. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    input_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""
    output_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilter) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_content_filter_type

    out["type"] = capo_bedrock.types.guardrail_content_filter_type.serialize_json(
        value["type"]
    )
    import capo_bedrock.types.guardrail_filter_strength

    out["inputStrength"] = capo_bedrock.types.guardrail_filter_strength.serialize_json(
        value["input_strength"]
    )
    import capo_bedrock.types.guardrail_filter_strength

    out["outputStrength"] = capo_bedrock.types.guardrail_filter_strength.serialize_json(
        value["output_strength"]
    )
    if "input_modalities" in value:
        import capo_bedrock.types.guardrail_modalities

        out["inputModalities"] = capo_bedrock.types.guardrail_modalities.serialize_json(
            value["input_modalities"]
        )
    if "output_modalities" in value:
        import capo_bedrock.types.guardrail_modalities

        out["outputModalities"] = (
            capo_bedrock.types.guardrail_modalities.serialize_json(
                value["output_modalities"]
            )
        )
    if "input_action" in value:
        import capo_bedrock.types.guardrail_content_filter_action

        out["inputAction"] = (
            capo_bedrock.types.guardrail_content_filter_action.serialize_json(
                value["input_action"]
            )
        )
    if "output_action" in value:
        import capo_bedrock.types.guardrail_content_filter_action

        out["outputAction"] = (
            capo_bedrock.types.guardrail_content_filter_action.serialize_json(
                value["output_action"]
            )
        )
    if "input_enabled" in value:
        out["inputEnabled"] = value["input_enabled"]
    if "output_enabled" in value:
        out["outputEnabled"] = value["output_enabled"]
    return out


def deserialize_json(data: dict) -> GuardrailContentFilter:
    out: GuardrailContentFilter = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock.types.guardrail_content_filter_type

        out["type"] = capo_bedrock.types.guardrail_content_filter_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GuardrailContentFilter.type required")
    if data.get("inputStrength") is not None:
        import capo_bedrock.types.guardrail_filter_strength

        out["input_strength"] = (
            capo_bedrock.types.guardrail_filter_strength.deserialize_json(
                data["inputStrength"]
            )
        )
    else:
        raise DeserializationError("GuardrailContentFilter.input_strength required")
    if data.get("outputStrength") is not None:
        import capo_bedrock.types.guardrail_filter_strength

        out["output_strength"] = (
            capo_bedrock.types.guardrail_filter_strength.deserialize_json(
                data["outputStrength"]
            )
        )
    else:
        raise DeserializationError("GuardrailContentFilter.output_strength required")
    if data.get("inputModalities") is not None:
        import capo_bedrock.types.guardrail_modalities

        out["input_modalities"] = (
            capo_bedrock.types.guardrail_modalities.deserialize_json(
                data["inputModalities"]
            )
        )
    if data.get("outputModalities") is not None:
        import capo_bedrock.types.guardrail_modalities

        out["output_modalities"] = (
            capo_bedrock.types.guardrail_modalities.deserialize_json(
                data["outputModalities"]
            )
        )
    if data.get("inputAction") is not None:
        import capo_bedrock.types.guardrail_content_filter_action

        out["input_action"] = (
            capo_bedrock.types.guardrail_content_filter_action.deserialize_json(
                data["inputAction"]
            )
        )
    if data.get("outputAction") is not None:
        import capo_bedrock.types.guardrail_content_filter_action

        out["output_action"] = (
            capo_bedrock.types.guardrail_content_filter_action.deserialize_json(
                data["outputAction"]
            )
        )
    if data.get("inputEnabled") is not None:
        out["input_enabled"] = data["inputEnabled"]
    if data.get("outputEnabled") is not None:
        out["output_enabled"] = data["outputEnabled"]
    return out


def redact_sensitive(value: GuardrailContentFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_modalities" in value:
        import capo_bedrock.types.guardrail_modalities

        out["input_modalities"] = (
            capo_bedrock.types.guardrail_modalities.redact_sensitive(
                value["input_modalities"]
            )
        )
    if "output_modalities" in value:
        import capo_bedrock.types.guardrail_modalities

        out["output_modalities"] = (
            capo_bedrock.types.guardrail_modalities.redact_sensitive(
                value["output_modalities"]
            )
        )
    if "input_action" in value:
        out["input_action"] = "*** Sensitive Data Redacted ***"
    if "output_action" in value:
        out["output_action"] = "*** Sensitive Data Redacted ***"
    return out
