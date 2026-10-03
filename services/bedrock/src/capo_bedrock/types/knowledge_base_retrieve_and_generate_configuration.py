"""Generated from Smithy shape ``com.amazonaws.bedrock#KnowledgeBaseRetrieveAndGenerateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.bedrock_model_arn
    import capo_bedrock.types.generation_configuration
    import capo_bedrock.types.knowledge_base_id
    import capo_bedrock.types.knowledge_base_retrieval_configuration
    import capo_bedrock.types.orchestration_configuration


class KnowledgeBaseRetrieveAndGenerateConfiguration(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier of the knowledge base.</p>"""
    model_arn: "capo_bedrock.types.bedrock_model_arn.BedrockModelArn"
    """<p>The Amazon Resource Name (ARN) of the foundation model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a> used to generate responses.</p>"""
    retrieval_configuration: NotRequired[
        "capo_bedrock.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
    ]
    """<p>Contains configuration details for retrieving text chunks.</p>"""
    generation_configuration: NotRequired[
        "capo_bedrock.types.generation_configuration.GenerationConfiguration"
    ]
    """<p>Contains configurations details for response generation based on retrieved text chunks.</p>"""
    orchestration_configuration: NotRequired[
        "capo_bedrock.types.orchestration_configuration.OrchestrationConfiguration"
    ]
    """<p>Contains configuration details for the model to process the prompt prior to retrieval and response generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseRetrieveAndGenerateConfiguration) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["modelArn"] = value["model_arn"]
    if "retrieval_configuration" in value:
        import capo_bedrock.types.knowledge_base_retrieval_configuration

        out["retrievalConfiguration"] = (
            capo_bedrock.types.knowledge_base_retrieval_configuration.serialize_json(
                value["retrieval_configuration"]
            )
        )
    if "generation_configuration" in value:
        import capo_bedrock.types.generation_configuration

        out["generationConfiguration"] = (
            capo_bedrock.types.generation_configuration.serialize_json(
                value["generation_configuration"]
            )
        )
    if "orchestration_configuration" in value:
        import capo_bedrock.types.orchestration_configuration

        out["orchestrationConfiguration"] = (
            capo_bedrock.types.orchestration_configuration.serialize_json(
                value["orchestration_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseRetrieveAndGenerateConfiguration:
    out: KnowledgeBaseRetrieveAndGenerateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "KnowledgeBaseRetrieveAndGenerateConfiguration.knowledge_base_id required"
        )
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "KnowledgeBaseRetrieveAndGenerateConfiguration.model_arn required"
        )
    if data.get("retrievalConfiguration") is not None:
        import capo_bedrock.types.knowledge_base_retrieval_configuration

        out["retrieval_configuration"] = (
            capo_bedrock.types.knowledge_base_retrieval_configuration.deserialize_json(
                data["retrievalConfiguration"]
            )
        )
    if data.get("generationConfiguration") is not None:
        import capo_bedrock.types.generation_configuration

        out["generation_configuration"] = (
            capo_bedrock.types.generation_configuration.deserialize_json(
                data["generationConfiguration"]
            )
        )
    if data.get("orchestrationConfiguration") is not None:
        import capo_bedrock.types.orchestration_configuration

        out["orchestration_configuration"] = (
            capo_bedrock.types.orchestration_configuration.deserialize_json(
                data["orchestrationConfiguration"]
            )
        )
    return out
