"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#VectorSearchRerankingConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.vector_search_bedrock_reranking_configuration
    import capo_bedrock_agent_runtime.types.vector_search_reranking_configuration_type


class VectorSearchRerankingConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.vector_search_reranking_configuration_type.VectorSearchRerankingConfigurationType"
    """<p>The type of reranker model.</p>"""
    bedrock_reranking_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.vector_search_bedrock_reranking_configuration.VectorSearchBedrockRerankingConfiguration"
    ]
    """<p>Contains configurations for an Amazon Bedrock reranker model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchRerankingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.vector_search_reranking_configuration_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.vector_search_reranking_configuration_type.serialize_json(
            value["type"]
        )
    )
    if "bedrock_reranking_configuration" in value:
        import capo_bedrock_agent_runtime.types.vector_search_bedrock_reranking_configuration

        out["bedrockRerankingConfiguration"] = (
            capo_bedrock_agent_runtime.types.vector_search_bedrock_reranking_configuration.serialize_json(
                value["bedrock_reranking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorSearchRerankingConfiguration:
    out: VectorSearchRerankingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.vector_search_reranking_configuration_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.vector_search_reranking_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.vector_search_reranking_configuration_type.VectorSearchRerankingConfigurationType",
            "",
        )
    if data.get("bedrockRerankingConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.vector_search_bedrock_reranking_configuration

        out["bedrock_reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.vector_search_bedrock_reranking_configuration.deserialize_json(
                data["bedrockRerankingConfiguration"]
            )
        )
    return out


def redact_sensitive(value: VectorSearchRerankingConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bedrock_reranking_configuration" in value:
        import capo_bedrock_agent_runtime.types.vector_search_bedrock_reranking_configuration

        out["bedrock_reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.vector_search_bedrock_reranking_configuration.redact_sensitive(
                value["bedrock_reranking_configuration"]
            )
        )
    return out
