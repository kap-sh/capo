"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingPolicy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_contextual_grounding_filters
    import capo_bedrock.types.guardrail_contextual_grounding_tier


class GuardrailContextualGroundingPolicy(TypedDict, closed=True):
    filters: "capo_bedrock.types.guardrail_contextual_grounding_filters.GuardrailContextualGroundingFilters"
    """<p>The filter details for the guardrails contextual grounding policy.</p>"""
    tier: NotRequired[
        "capo_bedrock.types.guardrail_contextual_grounding_tier.GuardrailContextualGroundingTier"
    ]
    """<p>The tier that your guardrail uses for contextual grounding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingPolicy) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_contextual_grounding_filters

    out["filters"] = (
        capo_bedrock.types.guardrail_contextual_grounding_filters.serialize_json(
            value["filters"]
        )
    )
    if "tier" in value:
        import capo_bedrock.types.guardrail_contextual_grounding_tier

        out["tier"] = (
            capo_bedrock.types.guardrail_contextual_grounding_tier.serialize_json(
                value["tier"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingPolicy:
    out: GuardrailContextualGroundingPolicy = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_bedrock.types.guardrail_contextual_grounding_filters

        out["filters"] = (
            capo_bedrock.types.guardrail_contextual_grounding_filters.deserialize_json(
                data["filters"]
            )
        )
    else:
        out["filters"] = []
    if data.get("tier") is not None:
        import capo_bedrock.types.guardrail_contextual_grounding_tier

        out["tier"] = (
            capo_bedrock.types.guardrail_contextual_grounding_tier.deserialize_json(
                data["tier"]
            )
        )
    return out


def redact_sensitive(value: GuardrailContextualGroundingPolicy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_bedrock.types.guardrail_contextual_grounding_filters

        out["filters"] = (
            capo_bedrock.types.guardrail_contextual_grounding_filters.redact_sensitive(
                value["filters"]
            )
        )
    if "tier" in value:
        import capo_bedrock.types.guardrail_contextual_grounding_tier

        out["tier"] = (
            capo_bedrock.types.guardrail_contextual_grounding_tier.redact_sensitive(
                value["tier"]
            )
        )
    return out
