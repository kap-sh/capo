"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VectorKnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.bedrock_embedding_model_arn
    import capo_bedrock_agent.types.embedding_model_configuration
    import capo_bedrock_agent.types.supplemental_data_storage_configuration


class VectorKnowledgeBaseConfiguration(TypedDict, closed=True):
    embedding_model_arn: (
        "capo_bedrock_agent.types.bedrock_embedding_model_arn.BedrockEmbeddingModelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.</p>"""
    embedding_model_configuration: NotRequired[
        "capo_bedrock_agent.types.embedding_model_configuration.EmbeddingModelConfiguration"
    ]
    """<p>The embeddings model configuration details for the vector model used in Knowledge Base.</p>"""
    supplemental_data_storage_configuration: NotRequired[
        "capo_bedrock_agent.types.supplemental_data_storage_configuration.SupplementalDataStorageConfiguration"
    ]
    """<p>If you include multimodal data from your data source, use this object to specify configurations for the storage location of the images extracted from your documents. These images can be retrieved and returned to the end user. They can also be used in generation when using <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html">RetrieveAndGenerate</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorKnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    out["embeddingModelArn"] = value["embedding_model_arn"]
    if "embedding_model_configuration" in value:
        import capo_bedrock_agent.types.embedding_model_configuration

        out["embeddingModelConfiguration"] = (
            capo_bedrock_agent.types.embedding_model_configuration.serialize_json(
                value["embedding_model_configuration"]
            )
        )
    if "supplemental_data_storage_configuration" in value:
        import capo_bedrock_agent.types.supplemental_data_storage_configuration

        out["supplementalDataStorageConfiguration"] = (
            capo_bedrock_agent.types.supplemental_data_storage_configuration.serialize_json(
                value["supplemental_data_storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorKnowledgeBaseConfiguration:
    out: VectorKnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("embeddingModelArn") is not None:
        out["embedding_model_arn"] = data["embeddingModelArn"]
    else:
        raise DeserializationError(
            "VectorKnowledgeBaseConfiguration.embedding_model_arn required"
        )
    if data.get("embeddingModelConfiguration") is not None:
        import capo_bedrock_agent.types.embedding_model_configuration

        out["embedding_model_configuration"] = (
            capo_bedrock_agent.types.embedding_model_configuration.deserialize_json(
                data["embeddingModelConfiguration"]
            )
        )
    if data.get("supplementalDataStorageConfiguration") is not None:
        import capo_bedrock_agent.types.supplemental_data_storage_configuration

        out["supplemental_data_storage_configuration"] = (
            capo_bedrock_agent.types.supplemental_data_storage_configuration.deserialize_json(
                data["supplementalDataStorageConfiguration"]
            )
        )
    return out
