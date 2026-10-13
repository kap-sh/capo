"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateAutomatedReasoningPolicyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_hash
    import capo_bedrock.types.automated_reasoning_policy_name
    import capo_bedrock.types.timestamp


class UpdateAutomatedReasoningPolicyResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the updated policy.</p>"""
    name: "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>The updated name of the policy.</p>"""
    definition_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    """<p>The hash of the updated policy definition.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomatedReasoningPolicyResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["name"] = value["name"]
    out["definitionHash"] = value["definition_hash"]
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> UpdateAutomatedReasoningPolicyResponse:
    out: UpdateAutomatedReasoningPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyResponse.policy_arn required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyResponse.name required"
        )
    if data.get("definitionHash") is not None:
        out["definition_hash"] = data["definitionHash"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyResponse.definition_hash required"
        )
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyResponse.updated_at required"
        )
    return out


def redact_sensitive(value: UpdateAutomatedReasoningPolicyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
