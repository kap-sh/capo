"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_configuration
    import capo_bedrock_agent.types.knowledge_base_role_arn
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.storage_configuration


class UpdateKnowledgeBaseRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to update.</p>"""
    name: "capo_bedrock_agent.types.name.Name"
    """<p>Specifies a new name for the knowledge base.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>Specifies a new description for the knowledge base.</p>"""
    role_arn: "capo_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn"
    """<p>Specifies a different Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>"""
    knowledge_base_configuration: "capo_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
    """<p>Specifies the configuration for the embeddings model used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>"""
    storage_configuration: NotRequired[
        "capo_bedrock_agent.types.storage_configuration.StorageConfiguration"
    ]
    """<p>Specifies the configuration for the vector store used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKnowledgeBaseRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["roleArn"] = value["role_arn"]
    import capo_bedrock_agent.types.knowledge_base_configuration

    out["knowledgeBaseConfiguration"] = (
        capo_bedrock_agent.types.knowledge_base_configuration.serialize_json(
            value["knowledge_base_configuration"]
        )
    )
    if "storage_configuration" in value:
        import capo_bedrock_agent.types.storage_configuration

        out["storageConfiguration"] = (
            capo_bedrock_agent.types.storage_configuration.serialize_json(
                value["storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKnowledgeBaseRequest:
    out: UpdateKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateKnowledgeBaseRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("UpdateKnowledgeBaseRequest.role_arn required")
    if data.get("knowledgeBaseConfiguration") is not None:
        import capo_bedrock_agent.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            capo_bedrock_agent.types.knowledge_base_configuration.deserialize_json(
                data["knowledgeBaseConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateKnowledgeBaseRequest.knowledge_base_configuration required"
        )
    if data.get("storageConfiguration") is not None:
        import capo_bedrock_agent.types.storage_configuration

        out["storage_configuration"] = (
            capo_bedrock_agent.types.storage_configuration.deserialize_json(
                data["storageConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateKnowledgeBaseRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            capo_bedrock_agent.types.knowledge_base_configuration.redact_sensitive(
                value["knowledge_base_configuration"]
            )
        )
    if "storage_configuration" in value:
        import capo_bedrock_agent.types.storage_configuration

        out["storage_configuration"] = (
            capo_bedrock_agent.types.storage_configuration.redact_sensitive(
                value["storage_configuration"]
            )
        )
    return out
