"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAutomatedReasoningPolicyResponse``."""

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


class CreateAutomatedReasoningPolicyResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that you created.</p>"""
    version: "capo_bedrock.types.automated_reasoning_policy_version.AutomatedReasoningPolicyVersion"
    """<p>The version number of the newly created Automated Reasoning policy. The initial version is always DRAFT.</p>"""
    name: "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>The name of the Automated Reasoning policy.</p>"""
    description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
    ]
    """<p>The description of the Automated Reasoning policy.</p>"""
    definition_hash: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    ]
    """<p>The hash of the policy definition. This is used as a concurrency token for creating policy versions that you can use in your application.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy was created.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomatedReasoningPolicyResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["version"] = value["version"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "definition_hash" in value:
        out["definitionHash"] = value["definition_hash"]
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> CreateAutomatedReasoningPolicyResponse:
    out: CreateAutomatedReasoningPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.policy_arn required"
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.version required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("definitionHash") is not None:
        out["definition_hash"] = data["definitionHash"]
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.created_at required"
        )
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.updated_at required"
        )
    return out


def redact_sensitive(value: CreateAutomatedReasoningPolicyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
