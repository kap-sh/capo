"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicPolicy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_topics
    import capo_bedrock.types.guardrail_topics_tier


class GuardrailTopicPolicy(TypedDict, closed=True):
    topics: "capo_bedrock.types.guardrail_topics.GuardrailTopics"
    """<p>A list of policies related to topics that the guardrail should deny.</p>"""
    tier: NotRequired["capo_bedrock.types.guardrail_topics_tier.GuardrailTopicsTier"]
    """<p>The tier that your guardrail uses for denied topic filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicPolicy) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_topics

    out["topics"] = capo_bedrock.types.guardrail_topics.serialize_json(value["topics"])
    if "tier" in value:
        import capo_bedrock.types.guardrail_topics_tier

        out["tier"] = capo_bedrock.types.guardrail_topics_tier.serialize_json(
            value["tier"]
        )
    return out


def deserialize_json(data: dict) -> GuardrailTopicPolicy:
    out: GuardrailTopicPolicy = {}  # type: ignore[typeddict-item]
    if data.get("topics") is not None:
        import capo_bedrock.types.guardrail_topics

        out["topics"] = capo_bedrock.types.guardrail_topics.deserialize_json(
            data["topics"]
        )
    else:
        raise DeserializationError("GuardrailTopicPolicy.topics required")
    if data.get("tier") is not None:
        import capo_bedrock.types.guardrail_topics_tier

        out["tier"] = capo_bedrock.types.guardrail_topics_tier.deserialize_json(
            data["tier"]
        )
    return out


def redact_sensitive(value: GuardrailTopicPolicy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "topics" in value:
        import capo_bedrock.types.guardrail_topics

        out["topics"] = capo_bedrock.types.guardrail_topics.redact_sensitive(
            value["topics"]
        )
    if "tier" in value:
        import capo_bedrock.types.guardrail_topics_tier

        out["tier"] = capo_bedrock.types.guardrail_topics_tier.redact_sensitive(
            value["tier"]
        )
    return out
