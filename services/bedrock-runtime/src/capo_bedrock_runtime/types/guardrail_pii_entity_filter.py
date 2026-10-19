"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailPiiEntityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_pii_entity_type
    import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action


class GuardrailPiiEntityFilter(TypedDict, closed=True):
    match: "str"
    """<p>The PII entity filter match.</p>"""
    type: "capo_bedrock_runtime.types.guardrail_pii_entity_type.GuardrailPiiEntityType"
    """<p>The PII entity filter type.</p>"""
    action: "capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action.GuardrailSensitiveInformationPolicyAction"
    """<p>The PII entity filter action.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether personally identifiable information (PII) that breaches the guardrail configuration is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntityFilter) -> dict:
    out: dict = {}
    out["match"] = value["match"]
    import capo_bedrock_runtime.types.guardrail_pii_entity_type

    out["type"] = capo_bedrock_runtime.types.guardrail_pii_entity_type.serialize_json(
        value["type"]
    )
    import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action

    out["action"] = (
        capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailPiiEntityFilter:
    out: GuardrailPiiEntityFilter = {}  # type: ignore[typeddict-item]
    if data.get("match") is not None:
        out["match"] = data["match"]
    else:
        out["match"] = ""
    if data.get("type") is not None:
        import capo_bedrock_runtime.types.guardrail_pii_entity_type

        out["type"] = (
            capo_bedrock_runtime.types.guardrail_pii_entity_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_pii_entity_type.GuardrailPiiEntityType",
            "",
        )
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
