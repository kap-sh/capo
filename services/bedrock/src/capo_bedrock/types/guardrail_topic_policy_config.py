"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicPolicyConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_topics_config
    import capo_bedrock.types.guardrail_topics_tier_config


class GuardrailTopicPolicyConfig(TypedDict, closed=True):
    topics_config: "capo_bedrock.types.guardrail_topics_config.GuardrailTopicsConfig"
    """<p>A list of policies related to topics that the guardrail should deny.</p>"""
    tier_config: NotRequired[
        "capo_bedrock.types.guardrail_topics_tier_config.GuardrailTopicsTierConfig"
    ]
    """<p>The tier that your guardrail uses for denied topic filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicPolicyConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_topics_config

    out["topicsConfig"] = capo_bedrock.types.guardrail_topics_config.serialize_json(
        value["topics_config"]
    )
    if "tier_config" in value:
        import capo_bedrock.types.guardrail_topics_tier_config

        out["tierConfig"] = (
            capo_bedrock.types.guardrail_topics_tier_config.serialize_json(
                value["tier_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailTopicPolicyConfig:
    out: GuardrailTopicPolicyConfig = {}  # type: ignore[typeddict-item]
    if data.get("topicsConfig") is not None:
        import capo_bedrock.types.guardrail_topics_config

        out["topics_config"] = (
            capo_bedrock.types.guardrail_topics_config.deserialize_json(
                data["topicsConfig"]
            )
        )
    else:
        raise DeserializationError("GuardrailTopicPolicyConfig.topics_config required")
    if data.get("tierConfig") is not None:
        import capo_bedrock.types.guardrail_topics_tier_config

        out["tier_config"] = (
            capo_bedrock.types.guardrail_topics_tier_config.deserialize_json(
                data["tierConfig"]
            )
        )
    return out


def redact_sensitive(value: GuardrailTopicPolicyConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "topics_config" in value:
        import capo_bedrock.types.guardrail_topics_config

        out["topics_config"] = (
            capo_bedrock.types.guardrail_topics_config.redact_sensitive(
                value["topics_config"]
            )
        )
    if "tier_config" in value:
        import capo_bedrock.types.guardrail_topics_tier_config

        out["tier_config"] = (
            capo_bedrock.types.guardrail_topics_tier_config.redact_sensitive(
                value["tier_config"]
            )
        )
    return out
