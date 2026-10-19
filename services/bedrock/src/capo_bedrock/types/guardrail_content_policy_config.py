"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentPolicyConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_content_filters_config
    import capo_bedrock.types.guardrail_content_filters_tier_config


class GuardrailContentPolicyConfig(TypedDict, closed=True):
    filters_config: "capo_bedrock.types.guardrail_content_filters_config.GuardrailContentFiltersConfig"
    """<p>Contains the type of the content filter and how strongly it should apply to prompts and model responses.</p>"""
    tier_config: NotRequired[
        "capo_bedrock.types.guardrail_content_filters_tier_config.GuardrailContentFiltersTierConfig"
    ]
    """<p>The tier that your guardrail uses for content filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentPolicyConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_content_filters_config

    out["filtersConfig"] = (
        capo_bedrock.types.guardrail_content_filters_config.serialize_json(
            value["filters_config"]
        )
    )
    if "tier_config" in value:
        import capo_bedrock.types.guardrail_content_filters_tier_config

        out["tierConfig"] = (
            capo_bedrock.types.guardrail_content_filters_tier_config.serialize_json(
                value["tier_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailContentPolicyConfig:
    out: GuardrailContentPolicyConfig = {}  # type: ignore[typeddict-item]
    if data.get("filtersConfig") is not None:
        import capo_bedrock.types.guardrail_content_filters_config

        out["filters_config"] = (
            capo_bedrock.types.guardrail_content_filters_config.deserialize_json(
                data["filtersConfig"]
            )
        )
    else:
        out["filters_config"] = []
    if data.get("tierConfig") is not None:
        import capo_bedrock.types.guardrail_content_filters_tier_config

        out["tier_config"] = (
            capo_bedrock.types.guardrail_content_filters_tier_config.deserialize_json(
                data["tierConfig"]
            )
        )
    return out


def redact_sensitive(value: GuardrailContentPolicyConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters_config" in value:
        import capo_bedrock.types.guardrail_content_filters_config

        out["filters_config"] = (
            capo_bedrock.types.guardrail_content_filters_config.redact_sensitive(
                value["filters_config"]
            )
        )
    if "tier_config" in value:
        import capo_bedrock.types.guardrail_content_filters_tier_config

        out["tier_config"] = (
            capo_bedrock.types.guardrail_content_filters_tier_config.redact_sensitive(
                value["tier_config"]
            )
        )
    return out
