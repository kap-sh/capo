"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.client_token
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.encryption_configuration
    import capo_cloudwatchomni.types.tag_map


class CreateSpaceInput(TypedDict, closed=True):
    name: "str"
    """A name that identifies the space. Must be 3-64 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens."""
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The ID of the domain to create the space in."""
    data_access_role_arn: "capo_cloudwatchomni.types.arn.Arn"
    """The ARN of the IAM role used for data access. The role must be in the caller's account."""
    agent_core_evaluation_role_arn: NotRequired["capo_cloudwatchomni.types.arn.Arn"]
    """The ARN of the IAM role used by AgentCore online evaluation. Must be in the caller's account. Omit if the space does not use AgentCore online evaluation."""
    encryption_configuration: NotRequired[
        "capo_cloudwatchomni.types.encryption_configuration.EncryptionConfiguration"
    ]
    """How to encrypt the space's data at rest. Omit for service owned encryption, which is equivalent to passing `encryptionStrategy` AWS_OWNED."""
    tags: NotRequired["capo_cloudwatchomni.types.tag_map.TagMap"]
    """The tags to associate with the space."""
    client_token: NotRequired["capo_cloudwatchomni.types.client_token.ClientToken"]
    """Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSpaceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["domainId"] = value["domain_id"]
    out["dataAccessRoleArn"] = value["data_access_role_arn"]
    if "agent_core_evaluation_role_arn" in value:
        out["agentCoreEvaluationRoleArn"] = value["agent_core_evaluation_role_arn"]
    if "encryption_configuration" in value:
        import capo_cloudwatchomni.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_cloudwatchomni.types.encryption_configuration.serialize_cbor(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateSpaceInput:
    out: CreateSpaceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("dataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["dataAccessRoleArn"]
    else:
        out["data_access_role_arn"] = ""
    if data.get("agentCoreEvaluationRoleArn") is not None:
        out["agent_core_evaluation_role_arn"] = data["agentCoreEvaluationRoleArn"]
    if data.get("encryptionConfiguration") is not None:
        import capo_cloudwatchomni.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_cloudwatchomni.types.encryption_configuration.deserialize_cbor(
                data["encryptionConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.deserialize_cbor(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
