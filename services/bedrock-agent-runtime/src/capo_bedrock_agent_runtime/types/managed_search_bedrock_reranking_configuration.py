"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ManagedSearchBedrockRerankingConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_model_configuration
    import capo_bedrock_agent_runtime.types.metadata_configuration_for_reranking


class ManagedSearchBedrockRerankingConfiguration(TypedDict, closed=True):
    model_configuration: "capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_model_configuration.ManagedSearchBedrockRerankingModelConfiguration"
    """<p>The model configuration containing the model ARN for reranking.</p>"""
    number_of_reranked_results: NotRequired["int"]
    """<p>The number of results to return after reranking.</p>"""
    metadata_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.metadata_configuration_for_reranking.MetadataConfigurationForReranking"
    ]
    """<p>The metadata configuration for reranking.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedSearchBedrockRerankingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_model_configuration

    out["modelConfiguration"] = (
        capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_model_configuration.serialize_json(
            value["model_configuration"]
        )
    )
    if "number_of_reranked_results" in value:
        out["numberOfRerankedResults"] = value["number_of_reranked_results"]
    if "metadata_configuration" in value:
        import capo_bedrock_agent_runtime.types.metadata_configuration_for_reranking

        out["metadataConfiguration"] = (
            capo_bedrock_agent_runtime.types.metadata_configuration_for_reranking.serialize_json(
                value["metadata_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedSearchBedrockRerankingConfiguration:
    out: ManagedSearchBedrockRerankingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_model_configuration

        out["model_configuration"] = (
            capo_bedrock_agent_runtime.types.managed_search_bedrock_reranking_model_configuration.deserialize_json(
                data["modelConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedSearchBedrockRerankingConfiguration.model_configuration required"
        )
    if data.get("numberOfRerankedResults") is not None:
        out["number_of_reranked_results"] = data["numberOfRerankedResults"]
    if data.get("metadataConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.metadata_configuration_for_reranking

        out["metadata_configuration"] = (
            capo_bedrock_agent_runtime.types.metadata_configuration_for_reranking.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    return out


def redact_sensitive(
    value: ManagedSearchBedrockRerankingConfiguration,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "metadata_configuration" in value:
        import capo_bedrock_agent_runtime.types.metadata_configuration_for_reranking

        out["metadata_configuration"] = (
            capo_bedrock_agent_runtime.types.metadata_configuration_for_reranking.redact_sensitive(
                value["metadata_configuration"]
            )
        )
    return out
