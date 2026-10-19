"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailManagedWord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_managed_word_type
    import capo_bedrock_runtime.types.guardrail_word_policy_action


class GuardrailManagedWord(TypedDict, closed=True):
    match: "str"
    """<p>The match for the managed word.</p>"""
    type: "capo_bedrock_runtime.types.guardrail_managed_word_type.GuardrailManagedWordType"
    """<p>The type for the managed word.</p>"""
    action: "capo_bedrock_runtime.types.guardrail_word_policy_action.GuardrailWordPolicyAction"
    """<p>The action for the managed word.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether managed word content that breaches the guardrail configuration is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWord) -> dict:
    out: dict = {}
    out["match"] = value["match"]
    import capo_bedrock_runtime.types.guardrail_managed_word_type

    out["type"] = capo_bedrock_runtime.types.guardrail_managed_word_type.serialize_json(
        value["type"]
    )
    import capo_bedrock_runtime.types.guardrail_word_policy_action

    out["action"] = (
        capo_bedrock_runtime.types.guardrail_word_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailManagedWord:
    out: GuardrailManagedWord = {}  # type: ignore[typeddict-item]
    if data.get("match") is not None:
        out["match"] = data["match"]
    else:
        out["match"] = ""
    if data.get("type") is not None:
        import capo_bedrock_runtime.types.guardrail_managed_word_type

        out["type"] = (
            capo_bedrock_runtime.types.guardrail_managed_word_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_managed_word_type.GuardrailManagedWordType",
            "",
        )
    if data.get("action") is not None:
        import capo_bedrock_runtime.types.guardrail_word_policy_action

        out["action"] = (
            capo_bedrock_runtime.types.guardrail_word_policy_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_word_policy_action.GuardrailWordPolicyAction",
            "",
        )
    if data.get("detected") is not None:
        out["detected"] = data["detected"]
    return out
