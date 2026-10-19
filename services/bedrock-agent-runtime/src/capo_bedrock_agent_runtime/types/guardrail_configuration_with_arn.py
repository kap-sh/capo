"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailConfigurationWithArn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_identifier_with_arn
    import capo_bedrock_agent_runtime.types.guardrail_version


class GuardrailConfigurationWithArn(TypedDict, closed=True):
    guardrail_identifier: "capo_bedrock_agent_runtime.types.guardrail_identifier_with_arn.GuardrailIdentifierWithArn"
    """<p> The unique identifier for the guardrail. </p>"""
    guardrail_version: (
        "capo_bedrock_agent_runtime.types.guardrail_version.GuardrailVersion"
    )
    """<p> The version of the guardrail. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConfigurationWithArn) -> dict:
    out: dict = {}
    out["guardrailIdentifier"] = value["guardrail_identifier"]
    out["guardrailVersion"] = value["guardrail_version"]
    return out


def deserialize_json(data: dict) -> GuardrailConfigurationWithArn:
    out: GuardrailConfigurationWithArn = {}  # type: ignore[typeddict-item]
    if data.get("guardrailIdentifier") is not None:
        out["guardrail_identifier"] = data["guardrailIdentifier"]
    else:
        out["guardrail_identifier"] = ""
    if data.get("guardrailVersion") is not None:
        out["guardrail_version"] = data["guardrailVersion"]
    else:
        out["guardrail_version"] = ""
    return out
