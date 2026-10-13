"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateAutomatedReasoningPolicyRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_definition
    import capo_bedrock.types.automated_reasoning_policy_description
    import capo_bedrock.types.automated_reasoning_policy_name


class UpdateAutomatedReasoningPolicyRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to update. This must be the ARN of a draft policy.</p>"""
    policy_definition: "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
    """<p>The updated policy definition containing the formal logic rules, variables, and types.</p>"""
    name: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    ]
    """<p>The updated name for the Automated Reasoning policy.</p>"""
    description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
    ]
    """<p>The updated description for the Automated Reasoning policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomatedReasoningPolicyRequest) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_definition

    out["policyDefinition"] = (
        capo_bedrock.types.automated_reasoning_policy_definition.serialize_json(
            value["policy_definition"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAutomatedReasoningPolicyRequest:
    out: UpdateAutomatedReasoningPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyDefinition") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.deserialize_json(
                data["policyDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyRequest.policy_definition required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: UpdateAutomatedReasoningPolicyRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_definition" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.redact_sensitive(
                value["policy_definition"]
            )
        )
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
