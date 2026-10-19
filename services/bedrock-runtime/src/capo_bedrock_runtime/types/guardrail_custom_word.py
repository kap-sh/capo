"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailCustomWord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_word_policy_action


class GuardrailCustomWord(TypedDict, closed=True):
    match: "str"
    """<p>The match for the custom word.</p>"""
    action: "capo_bedrock_runtime.types.guardrail_word_policy_action.GuardrailWordPolicyAction"
    """<p>The action for the custom word.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether custom word content that breaches the guardrail configuration is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailCustomWord) -> dict:
    out: dict = {}
    out["match"] = value["match"]
    import capo_bedrock_runtime.types.guardrail_word_policy_action

    out["action"] = (
        capo_bedrock_runtime.types.guardrail_word_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailCustomWord:
    out: GuardrailCustomWord = {}  # type: ignore[typeddict-item]
    if data.get("match") is not None:
        out["match"] = data["match"]
    else:
        out["match"] = ""
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
