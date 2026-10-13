"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAutomatedReasoningPolicyVersionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_description
    import capo_bedrock.types.automated_reasoning_policy_hash
    import capo_bedrock.types.automated_reasoning_policy_name
    import capo_bedrock.types.automated_reasoning_policy_version
    import capo_bedrock.types.timestamp


class CreateAutomatedReasoningPolicyVersionResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The versioned Amazon Resource Name (ARN) of the policy version.</p>"""
    version: "capo_bedrock.types.automated_reasoning_policy_version.AutomatedReasoningPolicyVersion"
    """<p>The version number of the policy version.</p>"""
    name: "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>The name of the policy version.</p>"""
    description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
    ]
    """<p>The description of the policy version.</p>"""
    definition_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    """<p>The hash of the policy definition for this version.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomatedReasoningPolicyVersionResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["version"] = value["version"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["definitionHash"] = value["definition_hash"]
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    return out


def deserialize_json(data: dict) -> CreateAutomatedReasoningPolicyVersionResponse:
    out: CreateAutomatedReasoningPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.policy_arn required"
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.version required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("definitionHash") is not None:
        out["definition_hash"] = data["definitionHash"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.definition_hash required"
        )
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.created_at required"
        )
    return out


def redact_sensitive(
    value: CreateAutomatedReasoningPolicyVersionResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
