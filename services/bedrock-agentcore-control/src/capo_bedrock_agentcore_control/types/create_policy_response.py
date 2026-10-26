"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePolicyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

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


class CreatePolicyResponse(TypedDict, closed=True):
    policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier for the created policy. This is a system-generated identifier consisting of the user name plus a 10-character generated suffix, used for all subsequent policy operations.</p>"""
    name: "capo_bedrock_agentcore_control.types.policy_name.PolicyName"
    """<p>The customer-assigned name of the created policy. This matches the name provided in the request and serves as the human-readable identifier for the policy.</p>"""
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine that manages this policy. This confirms the policy engine assignment and is used for policy evaluation routing.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was created. This is automatically set by the service and used for auditing and lifecycle management.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was last updated. For newly created policies, this matches the createdAt timestamp.</p>"""
    policy_arn: "capo_bedrock_agentcore_control.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the created policy. This globally unique identifier can be used for cross-service references and IAM policy statements.</p>"""
    status: "capo_bedrock_agentcore_control.types.policy_status.PolicyStatus"
    """<p>The current status of the policy. A status of <code>ACTIVE</code> indicates the policy is ready for use.</p>"""
    enforcement_mode: (
        "capo_bedrock_agentcore_control.types.enforcement_mode.EnforcementMode"
    )
    """<p>The enforcement mode of the created policy.</p>"""
    definition: (
        "capo_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    )
    """<p>The Cedar or Dogwood policy statement that was created. This is the validated policy definition that will be used for agent behavior control and access decisions.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The human-readable description of the policy's purpose and functionality. This helps administrators understand and manage the policy.</p>"""
    status_reasons: (
        "capo_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    )
    """<p>Additional information about the policy status. This provides details about any failures or the current state of the policy creation process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyResponse) -> dict:
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


def deserialize_json(data: dict) -> CreatePolicyResponse:
    out: CreatePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        out["policy_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("policyEngineId") is not None:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        out["policy_engine_id"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.policy_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.policy_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.policy_status.PolicyStatus", ""
        )
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
        out["definition"] = {"$unknown": {"name": ""}}
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
        out["status_reasons"] = []
    return out


def redact_sensitive(value: CreatePolicyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
