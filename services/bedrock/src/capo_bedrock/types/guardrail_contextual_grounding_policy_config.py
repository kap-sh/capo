"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingPolicyConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_contextual_grounding_filters_config


class GuardrailContextualGroundingPolicyConfig(TypedDict, closed=True):
    filters_config: "capo_bedrock.types.guardrail_contextual_grounding_filters_config.GuardrailContextualGroundingFiltersConfig"
    """<p>The filter configuration details for the guardrails contextual grounding policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingPolicyConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_contextual_grounding_filters_config

    out["filtersConfig"] = (
        capo_bedrock.types.guardrail_contextual_grounding_filters_config.serialize_json(
            value["filters_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingPolicyConfig:
    out: GuardrailContextualGroundingPolicyConfig = {}  # type: ignore[typeddict-item]
    if data.get("filtersConfig") is not None:
        import capo_bedrock.types.guardrail_contextual_grounding_filters_config

        out["filters_config"] = (
            capo_bedrock.types.guardrail_contextual_grounding_filters_config.deserialize_json(
                data["filtersConfig"]
            )
        )
    else:
        out["filters_config"] = []
    return out


def redact_sensitive(value: GuardrailContextualGroundingPolicyConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters_config" in value:
        import capo_bedrock.types.guardrail_contextual_grounding_filters_config

        out["filters_config"] = (
            capo_bedrock.types.guardrail_contextual_grounding_filters_config.redact_sensitive(
                value["filters_config"]
            )
        )
    return out
