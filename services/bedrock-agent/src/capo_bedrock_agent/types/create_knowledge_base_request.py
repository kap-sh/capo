"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.knowledge_base_configuration
    import capo_bedrock_agent.types.knowledge_base_role_arn
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.storage_configuration
    import capo_bedrock_agent.types.tags_map


class CreateKnowledgeBaseRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    name: "capo_bedrock_agent.types.name.Name"
    """<p>A name for the knowledge base.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>A description of the knowledge base.</p>"""
    role_arn: "capo_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>"""
    knowledge_base_configuration: "capo_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
    """<p>Contains details about the embeddings model used for the knowledge base.</p>"""
    storage_configuration: NotRequired[
        "capo_bedrock_agent.types.storage_configuration.StorageConfiguration"
    ]
    """<p>Contains details about the configuration of the vector database used for the knowledge base.</p>"""
    tags: NotRequired["capo_bedrock_agent.types.tags_map.TagsMap"]
    """<p>Specify the key-value pairs for the tags that you want to attach to your knowledge base in this object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKnowledgeBaseRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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
    if "tags" in value:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateKnowledgeBaseRequest:
    out: CreateKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateKnowledgeBaseRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateKnowledgeBaseRequest.role_arn required")
    if data.get("knowledgeBaseConfiguration") is not None:
        import capo_bedrock_agent.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            capo_bedrock_agent.types.knowledge_base_configuration.deserialize_json(
                data["knowledgeBaseConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateKnowledgeBaseRequest.knowledge_base_configuration required"
        )
    if data.get("storageConfiguration") is not None:
        import capo_bedrock_agent.types.storage_configuration

        out["storage_configuration"] = (
            capo_bedrock_agent.types.storage_configuration.deserialize_json(
                data["storageConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.deserialize_json(data["tags"])
    return out
