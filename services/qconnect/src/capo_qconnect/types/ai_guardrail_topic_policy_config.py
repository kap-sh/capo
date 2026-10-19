"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailTopicPolicyConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_topics_config


class AIGuardrailTopicPolicyConfig(TypedDict, closed=True):
    topics_config: "capo_qconnect.types.guardrail_topics_config.GuardrailTopicsConfig"
    """<p>A list of policies related to topics that the AI Guardrail should deny.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailTopicPolicyConfig) -> dict:
    out: dict = {}
    import capo_qconnect.types.guardrail_topics_config

    out["topicsConfig"] = capo_qconnect.types.guardrail_topics_config.serialize_json(
        value["topics_config"]
    )
    return out


def deserialize_json(data: dict) -> AIGuardrailTopicPolicyConfig:
    out: AIGuardrailTopicPolicyConfig = {}  # type: ignore[typeddict-item]
    if data.get("topicsConfig") is not None:
        import capo_qconnect.types.guardrail_topics_config

        out["topics_config"] = (
            capo_qconnect.types.guardrail_topics_config.deserialize_json(
                data["topicsConfig"]
            )
        )
    else:
        out["topics_config"] = []
    return out


def redact_sensitive(value: AIGuardrailTopicPolicyConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "topics_config" in value:
        import capo_qconnect.types.guardrail_topics_config

        out["topics_config"] = (
            capo_qconnect.types.guardrail_topics_config.redact_sensitive(
                value["topics_config"]
            )
        )
    return out
