"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingFilterConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_contextual_grounding_action
    import capo_bedrock.types.guardrail_contextual_grounding_filter_type


class GuardrailContextualGroundingFilterConfig(TypedDict, closed=True):
    type: "capo_bedrock.types.guardrail_contextual_grounding_filter_type.GuardrailContextualGroundingFilterType"
    """<p>The filter details for the guardrails contextual grounding filter.</p>"""
    threshold: "float"
    """<p>The threshold details for the guardrails contextual grounding filter.</p>"""
    action: NotRequired[
        "capo_bedrock.types.guardrail_contextual_grounding_action.GuardrailContextualGroundingAction"
    ]
    """<p>Specifies the action to take when content fails the contextual grounding evaluation. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether to enable contextual grounding evaluation. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFilterConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_contextual_grounding_filter_type

    out["type"] = (
        capo_bedrock.types.guardrail_contextual_grounding_filter_type.serialize_json(
            value["type"]
        )
    )
    out["threshold"] = (
        "NaN"
        if value["threshold"] != value["threshold"]
        else "Infinity"
        if value["threshold"] == float("inf")
        else "-Infinity"
        if value["threshold"] == float("-inf")
        else value["threshold"]
    )
    if "action" in value:
        import capo_bedrock.types.guardrail_contextual_grounding_action

        out["action"] = (
            capo_bedrock.types.guardrail_contextual_grounding_action.serialize_json(
                value["action"]
            )
        )
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingFilterConfig:
    out: GuardrailContextualGroundingFilterConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock.types.guardrail_contextual_grounding_filter_type

        out["type"] = (
            capo_bedrock.types.guardrail_contextual_grounding_filter_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock.types.guardrail_contextual_grounding_filter_type.GuardrailContextualGroundingFilterType",
            "",
        )
    if data.get("threshold") is not None:
        out["threshold"] = float(data["threshold"])
    else:
        out["threshold"] = 0.0
    if data.get("action") is not None:
        import capo_bedrock.types.guardrail_contextual_grounding_action

        out["action"] = (
            capo_bedrock.types.guardrail_contextual_grounding_action.deserialize_json(
                data["action"]
            )
        )
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    return out


def redact_sensitive(value: GuardrailContextualGroundingFilterConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "action" in value:
        out["action"] = "*** Sensitive Data Redacted ***"
    return out
