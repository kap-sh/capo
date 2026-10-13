"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VectorSearchBedrockRerankingConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.metadata_configuration_for_reranking
    import capo_bedrock_agent.types.vector_search_bedrock_reranking_model_configuration


class VectorSearchBedrockRerankingConfiguration(TypedDict, closed=True):
    model_configuration: "capo_bedrock_agent.types.vector_search_bedrock_reranking_model_configuration.VectorSearchBedrockRerankingModelConfiguration"
    """<p>Specifies the configuration for the Amazon Bedrock reranker model.</p>"""
    number_of_reranked_results: NotRequired["int"]
    """<p>Specifies the number of results to return after reranking.</p>"""
    metadata_configuration: NotRequired[
        "capo_bedrock_agent.types.metadata_configuration_for_reranking.MetadataConfigurationForReranking"
    ]
    """<p>Specifies how metadata fields should be handled during the reranking process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchBedrockRerankingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.vector_search_bedrock_reranking_model_configuration

    out["modelConfiguration"] = (
        capo_bedrock_agent.types.vector_search_bedrock_reranking_model_configuration.serialize_json(
            value["model_configuration"]
        )
    )
    if "number_of_reranked_results" in value:
        out["numberOfRerankedResults"] = value["number_of_reranked_results"]
    if "metadata_configuration" in value:
        import capo_bedrock_agent.types.metadata_configuration_for_reranking

        out["metadataConfiguration"] = (
            capo_bedrock_agent.types.metadata_configuration_for_reranking.serialize_json(
                value["metadata_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorSearchBedrockRerankingConfiguration:
    out: VectorSearchBedrockRerankingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelConfiguration") is not None:
        import capo_bedrock_agent.types.vector_search_bedrock_reranking_model_configuration

        out["model_configuration"] = (
            capo_bedrock_agent.types.vector_search_bedrock_reranking_model_configuration.deserialize_json(
                data["modelConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "VectorSearchBedrockRerankingConfiguration.model_configuration required"
        )
    if data.get("numberOfRerankedResults") is not None:
        out["number_of_reranked_results"] = data["numberOfRerankedResults"]
    if data.get("metadataConfiguration") is not None:
        import capo_bedrock_agent.types.metadata_configuration_for_reranking

        out["metadata_configuration"] = (
            capo_bedrock_agent.types.metadata_configuration_for_reranking.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    return out


def redact_sensitive(
    value: VectorSearchBedrockRerankingConfiguration,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "metadata_configuration" in value:
        import capo_bedrock_agent.types.metadata_configuration_for_reranking

        out["metadata_configuration"] = (
            capo_bedrock_agent.types.metadata_configuration_for_reranking.redact_sensitive(
                value["metadata_configuration"]
            )
        )
    return out
