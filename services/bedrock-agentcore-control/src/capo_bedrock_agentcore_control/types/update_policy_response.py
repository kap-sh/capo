"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatePolicyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.enforcement_mode
    import capo_bedrock_agentcore_control.types.policy_arn
    import capo_bedrock_agentcore_control.types.policy_definition
    import capo_bedrock_agentcore_control.types.policy_name
    import capo_bedrock_agentcore_control.types.policy_status
    import capo_bedrock_agentcore_control.types.policy_status_reasons
    import capo_bedrock_agentcore_control.types.resource_id


class UpdatePolicyResponse(TypedDict, closed=True):
    policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the updated policy.</p>"""
    name: "capo_bedrock_agentcore_control.types.policy_name.PolicyName"
    """<p>The name of the updated policy.</p>"""
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine managing the updated policy.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The original creation timestamp of the policy.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was last updated.</p>"""
    policy_arn: "capo_bedrock_agentcore_control.types.policy_arn.PolicyArn"
    """<p>The ARN of the updated policy.</p>"""
    status: "capo_bedrock_agentcore_control.types.policy_status.PolicyStatus"
    """<p>The current status of the updated policy.</p>"""
    enforcement_mode: (
        "capo_bedrock_agentcore_control.types.enforcement_mode.EnforcementMode"
    )
    """<p>The current enforcement mode of the updated policy.</p>"""
    definition: (
        "capo_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    )
    """<p>The updated Cedar or Dogwood policy statement.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The updated description of the policy.</p>"""
    status_reasons: (
        "capo_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    )
    """<p>Additional information about the update status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicyResponse) -> dict:
    out: dict = {}
    out["policyId"] = value["policy_id"]
    out["name"] = value["name"]
    out["policyEngineId"] = value["policy_engine_id"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    out["policyArn"] = value["policy_arn"]
    import capo_bedrock_agentcore_control.types.policy_status

    out["status"] = capo_bedrock_agentcore_control.types.policy_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore_control.types.enforcement_mode

    out["enforcementMode"] = (
        capo_bedrock_agentcore_control.types.enforcement_mode.serialize_json(
            value.get("enforcement_mode", "ACTIVE")
        )
    )
    import capo_bedrock_agentcore_control.types.policy_definition

    out["definition"] = (
        capo_bedrock_agentcore_control.types.policy_definition.serialize_json(
            value["definition"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.policy_status_reasons

    out["statusReasons"] = (
        capo_bedrock_agentcore_control.types.policy_status_reasons.serialize_json(
            value["status_reasons"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePolicyResponse:
    out: UpdatePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("UpdatePolicyResponse.policy_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdatePolicyResponse.name required")
    if data.get("policyEngineId") is not None:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("UpdatePolicyResponse.policy_engine_id required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.updated_at required")
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("UpdatePolicyResponse.policy_arn required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.policy_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.policy_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.status required")
    if data.get("enforcementMode") is not None:
        import capo_bedrock_agentcore_control.types.enforcement_mode

        out["enforcement_mode"] = (
            capo_bedrock_agentcore_control.types.enforcement_mode.deserialize_json(
                data["enforcementMode"]
            )
        )
    else:
        out["enforcement_mode"] = "ACTIVE"
    if data.get("definition") is not None:
        import capo_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            capo_bedrock_agentcore_control.types.policy_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.definition required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("statusReasons") is not None:
        import capo_bedrock_agentcore_control.types.policy_status_reasons

        out["status_reasons"] = (
            capo_bedrock_agentcore_control.types.policy_status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.status_reasons required")
    return out


def redact_sensitive(value: UpdatePolicyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
