"""Generated from Smithy shape ``com.amazonaws.bedrock#ExportAutomatedReasoningPolicyVersionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition


class ExportAutomatedReasoningPolicyVersionResponse(TypedDict, closed=True):
    policy_definition: "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
    """<p>The exported policy definition containing the formal logic rules, variables, and custom variable types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportAutomatedReasoningPolicyVersionResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_definition

    out["policyDefinition"] = (
        capo_bedrock.types.automated_reasoning_policy_definition.serialize_json(
            value["policy_definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExportAutomatedReasoningPolicyVersionResponse:
    out: ExportAutomatedReasoningPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyDefinition") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.deserialize_json(
                data["policyDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "ExportAutomatedReasoningPolicyVersionResponse.policy_definition required"
        )
    return out


def redact_sensitive(
    value: ExportAutomatedReasoningPolicyVersionResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_definition" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.redact_sensitive(
                value["policy_definition"]
            )
        )
    return out
