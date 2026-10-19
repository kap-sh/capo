"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingPolicy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_contextual_grounding_filters


class GuardrailContextualGroundingPolicy(TypedDict, closed=True):
    filters: "capo_bedrock.types.guardrail_contextual_grounding_filters.GuardrailContextualGroundingFilters"
    """<p>The filter details for the guardrails contextual grounding policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingPolicy) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_contextual_grounding_filters

    out["filters"] = (
        capo_bedrock.types.guardrail_contextual_grounding_filters.serialize_json(
            value["filters"]
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
    return out
