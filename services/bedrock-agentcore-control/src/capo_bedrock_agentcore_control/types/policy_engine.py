"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyEngine``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.policy_engine_arn
    import capo_bedrock_agentcore_control.types.policy_engine_name
    import capo_bedrock_agentcore_control.types.policy_engine_status
    import capo_bedrock_agentcore_control.types.policy_status_reasons
    import capo_bedrock_agentcore_control.types.resource_id


class PolicyEngine(TypedDict, closed=True):
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier for the policy engine. This system-generated identifier consists of the user name plus a 10-character generated suffix and serves as the primary key for policy engine operations.</p>"""
    name: "capo_bedrock_agentcore_control.types.policy_engine_name.PolicyEngineName"
    """<p>The customer-assigned immutable name for the policy engine. This human-readable identifier must be unique within the account and cannot exceed 48 characters.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy engine was originally created. This is automatically set by the service and used for auditing and lifecycle management.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy engine was last modified. This tracks the most recent changes to the policy engine configuration or metadata.</p>"""
    policy_engine_arn: (
        "capo_bedrock_agentcore_control.types.policy_engine_arn.PolicyEngineArn"
    )
    """<p>The Amazon Resource Name (ARN) of the policy engine. This globally unique identifier can be used for cross-service references and IAM policy statements.</p>"""
    status: (
        "capo_bedrock_agentcore_control.types.policy_engine_status.PolicyEngineStatus"
    )
    """<p>The current status of the policy engine.</p>"""
    encryption_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>A human-readable description of the policy engine's purpose and scope. Limited to 4,096 characters, this helps administrators understand the policy engine's role in the overall governance strategy.</p>"""
    status_reasons: (
        "capo_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    )
    """<p>Additional information about the policy engine status. This provides details about any failures or the current state of the policy engine lifecycle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEngine) -> dict:
    out: dict = {}
    out["policyEngineId"] = value["policy_engine_id"]
    out["name"] = value["name"]
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
    out["policyEngineArn"] = value["policy_engine_arn"]
    import capo_bedrock_agentcore_control.types.policy_engine_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.policy_engine_status.serialize_json(
            value["status"]
        )
    )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.policy_status_reasons

    out["statusReasons"] = (
        capo_bedrock_agentcore_control.types.policy_status_reasons.serialize_json(
            value["status_reasons"]
        )
    )
    return out


def deserialize_json(data: dict) -> PolicyEngine:
    out: PolicyEngine = {}  # type: ignore[typeddict-item]
    if data.get("policyEngineId") is not None:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("PolicyEngine.policy_engine_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PolicyEngine.name required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("PolicyEngine.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("PolicyEngine.updated_at required")
    if data.get("policyEngineArn") is not None:
        out["policy_engine_arn"] = data["policyEngineArn"]
    else:
        raise DeserializationError("PolicyEngine.policy_engine_arn required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.policy_engine_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.policy_engine_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("PolicyEngine.status required")
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
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
        raise DeserializationError("PolicyEngine.status_reasons required")
    return out


def redact_sensitive(value: PolicyEngine) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
