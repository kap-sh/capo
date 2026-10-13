"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePolicyEngineRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.policy_engine_name
    import capo_bedrock_agentcore_control.types.tags_map


class CreatePolicyEngineRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.policy_engine_name.PolicyEngineName"
    """<p>The customer-assigned immutable name for the policy engine. This name identifies the policy engine and cannot be changed after creation.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>A human-readable description of the policy engine's purpose and scope (1-4,096 characters). This helps administrators understand the policy engine's role in the overall governance strategy. Document which Gateway this engine will be associated with, what types of tools or workflows it governs, and the team or service responsible for maintaining it. Clear descriptions are essential when managing multiple policy engines across different services or environments.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy engine.</p>"""
    encryption_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to an AgentCore Policy. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyEngineRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePolicyEngineRequest:
    out: CreatePolicyEngineRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePolicyEngineRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreatePolicyEngineRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
