"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ManagedSearchConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.managed_search_reranking_configuration
    import capo_bedrock_agent_runtime.types.reranking_model_type
    import capo_bedrock_agent_runtime.types.retrieval_filter


class ManagedSearchConfiguration(TypedDict, closed=True):
    number_of_results: NotRequired["int"]
    """<p>The number of results to retrieve.</p>"""
    filter: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_filter.RetrievalFilter"
    ]
    """<p>Filters the metadata of the retrieved results so that Amazon Bedrock returns only results that match the filter.</p>"""
    reranking_model_type: NotRequired[
        "capo_bedrock_agent_runtime.types.reranking_model_type.RerankingModelType"
    ]
    """<p>The type of reranking model to use when reranking results retrieved from the managed search. Use <code>CUSTOM</code> to specify a model, <code>MANAGED</code> to use the service default, or <code>NONE</code> to disable reranking.</p>"""
    reranking_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.managed_search_reranking_configuration.ManagedSearchRerankingConfiguration"
    ]
    """<p>Contains configurations for reranking the results retrieved from the managed search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedSearchConfiguration) -> dict:
    out: dict = {}
    if "number_of_results" in value:
        out["numberOfResults"] = value["number_of_results"]
    if "filter" in value:
        import capo_bedrock_agent_runtime.types.retrieval_filter

        out["filter"] = (
            capo_bedrock_agent_runtime.types.retrieval_filter.serialize_json(
                value["filter"]
            )
        )
    if "reranking_model_type" in value:
        import capo_bedrock_agent_runtime.types.reranking_model_type

        out["rerankingModelType"] = (
            capo_bedrock_agent_runtime.types.reranking_model_type.serialize_json(
                value["reranking_model_type"]
            )
        )
    if "reranking_configuration" in value:
        import capo_bedrock_agent_runtime.types.managed_search_reranking_configuration

        out["rerankingConfiguration"] = (
            capo_bedrock_agent_runtime.types.managed_search_reranking_configuration.serialize_json(
                value["reranking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedSearchConfiguration:
    out: ManagedSearchConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("numberOfResults") is not None:
        out["number_of_results"] = data["numberOfResults"]
    if data.get("filter") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_filter

        out["filter"] = (
            capo_bedrock_agent_runtime.types.retrieval_filter.deserialize_json(
                data["filter"]
            )
        )
    if data.get("rerankingModelType") is not None:
        import capo_bedrock_agent_runtime.types.reranking_model_type

        out["reranking_model_type"] = (
            capo_bedrock_agent_runtime.types.reranking_model_type.deserialize_json(
                data["rerankingModelType"]
            )
        )
    if data.get("rerankingConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.managed_search_reranking_configuration

        out["reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.managed_search_reranking_configuration.deserialize_json(
                data["rerankingConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ManagedSearchConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter" in value:
        out["filter"] = "*** Sensitive Data Redacted ***"
    if "reranking_configuration" in value:
        import capo_bedrock_agent_runtime.types.managed_search_reranking_configuration

        out["reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.managed_search_reranking_configuration.redact_sensitive(
                value["reranking_configuration"]
            )
        )
    return out
