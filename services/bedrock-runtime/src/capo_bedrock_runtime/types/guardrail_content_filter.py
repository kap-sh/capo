"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_content_filter_confidence
    import capo_bedrock_runtime.types.guardrail_content_filter_strength
    import capo_bedrock_runtime.types.guardrail_content_filter_type
    import capo_bedrock_runtime.types.guardrail_content_policy_action


class GuardrailContentFilter(TypedDict, closed=True):
    type: "capo_bedrock_runtime.types.guardrail_content_filter_type.GuardrailContentFilterType"
    """<p>The guardrail type.</p>"""
    confidence: "capo_bedrock_runtime.types.guardrail_content_filter_confidence.GuardrailContentFilterConfidence"
    """<p>The guardrail confidence.</p>"""
    filter_strength: NotRequired[
        "capo_bedrock_runtime.types.guardrail_content_filter_strength.GuardrailContentFilterStrength"
    ]
    """<p>The filter strength setting for the guardrail content filter.</p>"""
    action: "capo_bedrock_runtime.types.guardrail_content_policy_action.GuardrailContentPolicyAction"
    """<p>The guardrail action.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether content that breaches the guardrail configuration is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilter) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_content_filter_type

    out["type"] = (
        capo_bedrock_runtime.types.guardrail_content_filter_type.serialize_json(
            value["type"]
        )
    )
    import capo_bedrock_runtime.types.guardrail_content_filter_confidence

    out["confidence"] = (
        capo_bedrock_runtime.types.guardrail_content_filter_confidence.serialize_json(
            value["confidence"]
        )
    )
    if "filter_strength" in value:
        import capo_bedrock_runtime.types.guardrail_content_filter_strength

        out["filterStrength"] = (
            capo_bedrock_runtime.types.guardrail_content_filter_strength.serialize_json(
                value["filter_strength"]
            )
        )
    import capo_bedrock_runtime.types.guardrail_content_policy_action

    out["action"] = (
        capo_bedrock_runtime.types.guardrail_content_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailContentFilter:
    out: GuardrailContentFilter = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_runtime.types.guardrail_content_filter_type

        out["type"] = (
            capo_bedrock_runtime.types.guardrail_content_filter_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_content_filter_type.GuardrailContentFilterType",
            "",
        )
    if data.get("confidence") is not None:
        import capo_bedrock_runtime.types.guardrail_content_filter_confidence

        out["confidence"] = (
            capo_bedrock_runtime.types.guardrail_content_filter_confidence.deserialize_json(
                data["confidence"]
            )
        )
    else:
        import typing

        out["confidence"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_content_filter_confidence.GuardrailContentFilterConfidence",
            "",
        )
    if data.get("filterStrength") is not None:
        import capo_bedrock_runtime.types.guardrail_content_filter_strength

        out["filter_strength"] = (
            capo_bedrock_runtime.types.guardrail_content_filter_strength.deserialize_json(
                data["filterStrength"]
            )
        )
    if data.get("action") is not None:
        import capo_bedrock_runtime.types.guardrail_content_policy_action

        out["action"] = (
            capo_bedrock_runtime.types.guardrail_content_policy_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_content_policy_action.GuardrailContentPolicyAction",
            "",
        )
    if data.get("detected") is not None:
        out["detected"] = data["detected"]
    return out
