"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicyResponse``."""

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


class GetPolicyResponse(TypedDict, closed=True):
    policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the retrieved policy. This matches the policy ID provided in the request and serves as the system identifier for the policy.</p>"""
    name: "capo_bedrock_agentcore_control.types.policy_name.PolicyName"
    """<p>The customer-assigned name of the policy. This is the human-readable identifier that was specified when the policy was created.</p>"""
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine that manages this policy. This confirms the policy engine context for the retrieved policy.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was originally created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was last modified. This tracks the most recent changes to the policy configuration.</p>"""
    policy_arn: "capo_bedrock_agentcore_control.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy. This globally unique identifier can be used for cross-service references and IAM policy statements.</p>"""
    status: "capo_bedrock_agentcore_control.types.policy_status.PolicyStatus"
    """<p>The current status of the policy.</p>"""
    enforcement_mode: (
        "capo_bedrock_agentcore_control.types.enforcement_mode.EnforcementMode"
    )
    """<p>The current enforcement mode of the policy.</p>"""
    definition: (
        "capo_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    )
    """<p>The Cedar or Dogwood policy statement that defines the access control rules. This contains the actual policy logic used for agent behavior control and access decisions.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The human-readable description of the policy's purpose and functionality. This helps administrators understand and manage the policy.</p>"""
    status_reasons: (
        "capo_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    )
    """<p>Additional information about the policy status. This provides details about any failures or the current state of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyResponse) -> dict:
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


def deserialize_json(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("GetPolicyResponse.policy_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetPolicyResponse.name required")
    if data.get("policyEngineId") is not None:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("GetPolicyResponse.policy_engine_id required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetPolicyResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetPolicyResponse.updated_at required")
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("GetPolicyResponse.policy_arn required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.policy_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.policy_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetPolicyResponse.status required")
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
        raise DeserializationError("GetPolicyResponse.definition required")
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
        raise DeserializationError("GetPolicyResponse.status_reasons required")
    return out


def redact_sensitive(value: GetPolicyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
