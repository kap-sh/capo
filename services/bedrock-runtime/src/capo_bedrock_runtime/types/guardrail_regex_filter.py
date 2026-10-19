"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailRegexFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action


class GuardrailRegexFilter(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The regex filter name.</p>"""
    match: NotRequired["str"]
    """<p>The regesx filter match.</p>"""
    regex: NotRequired["str"]
    """<p>The regex query.</p>"""
    action: "capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action.GuardrailSensitiveInformationPolicyAction"
    """<p>The region filter action.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether custom regex entities that breach the guardrail configuration are detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "match" in value:
        out["match"] = value["match"]
    if "regex" in value:
        out["regex"] = value["regex"]
    import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action

    out["action"] = (
        capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailRegexFilter:
    out: GuardrailRegexFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("match") is not None:
        out["match"] = data["match"]
    if data.get("regex") is not None:
        out["regex"] = data["regex"]
    if data.get("action") is not None:
        import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action

        out["action"] = (
            capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action.GuardrailSensitiveInformationPolicyAction",
            "",
        )
    if data.get("detected") is not None:
        out["detected"] = data["detected"]
    return out
