"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseVectorSearchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.implicit_filter_configuration
    import capo_bedrock_agent_runtime.types.retrieval_filter
    import capo_bedrock_agent_runtime.types.search_type
    import capo_bedrock_agent_runtime.types.vector_search_reranking_configuration


class KnowledgeBaseVectorSearchConfiguration(TypedDict, closed=True):
    number_of_results: "int"
    """<p>The number of source chunks to retrieve.</p>"""
    override_search_type: NotRequired[
        "capo_bedrock_agent_runtime.types.search_type.SearchType"
    ]
    """<p>By default, Amazon Bedrock decides a search strategy for you. If you're using an Amazon OpenSearch Serverless vector store that contains a filterable text field, you can specify whether to query the knowledge base with a <code>HYBRID</code> search using both vector embeddings and raw text, or <code>SEMANTIC</code> search using only vector embeddings. For other vector store configurations, only <code>SEMANTIC</code> search is available. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-test.html">Test a knowledge base</a>.</p>"""
    filter: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_filter.RetrievalFilter"
    ]
    """<p>Specifies the filters to use on the metadata in the knowledge base data sources before returning results. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>"""
    reranking_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.vector_search_reranking_configuration.VectorSearchRerankingConfiguration"
    ]
    """<p>Contains configurations for reranking the retrieved results. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html">Improve the relevance of query responses with a reranker model</a>.</p>"""
    implicit_filter_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.implicit_filter_configuration.ImplicitFilterConfiguration"
    ]
    """<p>Settings for implicit filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseVectorSearchConfiguration) -> dict:
    out: dict = {}
    out["numberOfResults"] = value.get("number_of_results", 5)
    if "override_search_type" in value:
        import capo_bedrock_agent_runtime.types.search_type

        out["overrideSearchType"] = (
            capo_bedrock_agent_runtime.types.search_type.serialize_json(
                value["override_search_type"]
            )
        )
    if "filter" in value:
        import capo_bedrock_agent_runtime.types.retrieval_filter

        out["filter"] = (
            capo_bedrock_agent_runtime.types.retrieval_filter.serialize_json(
                value["filter"]
            )
        )
    if "reranking_configuration" in value:
        import capo_bedrock_agent_runtime.types.vector_search_reranking_configuration

        out["rerankingConfiguration"] = (
            capo_bedrock_agent_runtime.types.vector_search_reranking_configuration.serialize_json(
                value["reranking_configuration"]
            )
        )
    if "implicit_filter_configuration" in value:
        import capo_bedrock_agent_runtime.types.implicit_filter_configuration

        out["implicitFilterConfiguration"] = (
            capo_bedrock_agent_runtime.types.implicit_filter_configuration.serialize_json(
                value["implicit_filter_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseVectorSearchConfiguration:
    out: KnowledgeBaseVectorSearchConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("numberOfResults") is not None:
        out["number_of_results"] = data["numberOfResults"]
    else:
        out["number_of_results"] = 5
    if data.get("overrideSearchType") is not None:
        import capo_bedrock_agent_runtime.types.search_type

        out["override_search_type"] = (
            capo_bedrock_agent_runtime.types.search_type.deserialize_json(
                data["overrideSearchType"]
            )
        )
    if data.get("filter") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_filter

        out["filter"] = (
            capo_bedrock_agent_runtime.types.retrieval_filter.deserialize_json(
                data["filter"]
            )
        )
    if data.get("rerankingConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.vector_search_reranking_configuration

        out["reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.vector_search_reranking_configuration.deserialize_json(
                data["rerankingConfiguration"]
            )
        )
    if data.get("implicitFilterConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.implicit_filter_configuration

        out["implicit_filter_configuration"] = (
            capo_bedrock_agent_runtime.types.implicit_filter_configuration.deserialize_json(
                data["implicitFilterConfiguration"]
            )
        )
    return out
