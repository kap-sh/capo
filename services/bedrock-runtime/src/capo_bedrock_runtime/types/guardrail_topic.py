"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTopic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_topic_policy_action
    import capo_bedrock_runtime.types.guardrail_topic_type


class GuardrailTopic(TypedDict, closed=True):
    name: "str"
    """<p>The name for the guardrail.</p>"""
    type: "capo_bedrock_runtime.types.guardrail_topic_type.GuardrailTopicType"
    """<p>The type behavior that the guardrail should perform when the model detects the topic.</p>"""
    action: "capo_bedrock_runtime.types.guardrail_topic_policy_action.GuardrailTopicPolicyAction"
    """<p>The action the guardrail should take when it intervenes on a topic.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether topic content that breaches the guardrail configuration is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopic) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_runtime.types.guardrail_topic_type

    out["type"] = capo_bedrock_runtime.types.guardrail_topic_type.serialize_json(
        value["type"]
    )
    import capo_bedrock_runtime.types.guardrail_topic_policy_action

    out["action"] = (
        capo_bedrock_runtime.types.guardrail_topic_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailTopic:
    out: GuardrailTopic = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_bedrock_runtime.types.guardrail_topic_type

        out["type"] = capo_bedrock_runtime.types.guardrail_topic_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_topic_type.GuardrailTopicType", ""
        )
    if data.get("action") is not None:
        import capo_bedrock_runtime.types.guardrail_topic_policy_action

        out["action"] = (
            capo_bedrock_runtime.types.guardrail_topic_policy_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_topic_policy_action.GuardrailTopicPolicyAction",
            "",
        )
    if data.get("detected") is not None:
        out["detected"] = data["detected"]
    return out
