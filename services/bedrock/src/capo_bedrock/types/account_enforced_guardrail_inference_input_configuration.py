"""Generated from Smithy shape ``com.amazonaws.bedrock#AccountEnforcedGuardrailInferenceInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_identifier
    import capo_bedrock.types.guardrail_numerical_version
    import capo_bedrock.types.model_enforcement
    import capo_bedrock.types.selective_content_guarding


class AccountEnforcedGuardrailInferenceInputConfiguration(TypedDict, closed=True):
    guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier"
    """<p>Identifier for the guardrail, could be the ID or the ARN.</p>"""
    guardrail_version: (
        "capo_bedrock.types.guardrail_numerical_version.GuardrailNumericalVersion"
    )
    """<p>Numerical guardrail version.</p>"""
    selective_content_guarding: NotRequired[
        "capo_bedrock.types.selective_content_guarding.SelectiveContentGuarding"
    ]
    """<p>Selective content guarding controls for enforced guardrails.</p>"""
    model_enforcement: NotRequired[
        "capo_bedrock.types.model_enforcement.ModelEnforcement"
    ]
    """<p>Model-specific information for the enforced guardrail configuration. If not present, the configuration is enforced on all models</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountEnforcedGuardrailInferenceInputConfiguration) -> dict:
    out: dict = {}
    out["guardrailIdentifier"] = value["guardrail_identifier"]
    out["guardrailVersion"] = value["guardrail_version"]
    if "selective_content_guarding" in value:
        import capo_bedrock.types.selective_content_guarding

        out["selectiveContentGuarding"] = (
            capo_bedrock.types.selective_content_guarding.serialize_json(
                value["selective_content_guarding"]
            )
        )
    if "model_enforcement" in value:
        import capo_bedrock.types.model_enforcement

        out["modelEnforcement"] = capo_bedrock.types.model_enforcement.serialize_json(
            value["model_enforcement"]
        )
    return out


def deserialize_json(data: dict) -> AccountEnforcedGuardrailInferenceInputConfiguration:
    out: AccountEnforcedGuardrailInferenceInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("guardrailIdentifier") is not None:
        out["guardrail_identifier"] = data["guardrailIdentifier"]
    else:
        out["guardrail_identifier"] = ""
    if data.get("guardrailVersion") is not None:
        out["guardrail_version"] = data["guardrailVersion"]
    else:
        out["guardrail_version"] = ""
    if data.get("selectiveContentGuarding") is not None:
        import capo_bedrock.types.selective_content_guarding

        out["selective_content_guarding"] = (
            capo_bedrock.types.selective_content_guarding.deserialize_json(
                data["selectiveContentGuarding"]
            )
        )
    if data.get("modelEnforcement") is not None:
        import capo_bedrock.types.model_enforcement

        out["model_enforcement"] = (
            capo_bedrock.types.model_enforcement.deserialize_json(
                data["modelEnforcement"]
            )
        )
    return out
