"""Generated from Smithy shape ``com.amazonaws.bedrock#KnowledgeBaseVectorSearchConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.implicit_filter_configuration
    import capo_bedrock.types.retrieval_filter
    import capo_bedrock.types.search_type
    import capo_bedrock.types.vector_search_reranking_configuration


class KnowledgeBaseVectorSearchConfiguration(TypedDict, closed=True):
    number_of_results: NotRequired["int"]
    """<p>The number of text chunks to retrieve; the number of results to return.</p>"""
    override_search_type: NotRequired["capo_bedrock.types.search_type.SearchType"]
    """<p>By default, Amazon Bedrock decides a search strategy for you. If you're using an Amazon OpenSearch Serverless vector store that contains a filterable text field, you can specify whether to query the knowledge base with a <code>HYBRID</code> search using both vector embeddings and raw text, or <code>SEMANTIC</code> search using only vector embeddings. For other vector store configurations, only <code>SEMANTIC</code> search is available.</p>"""
    filter: NotRequired["capo_bedrock.types.retrieval_filter.RetrievalFilter"]
    """<p>Specifies the filters to use on the metadata fields in the knowledge base data sources before returning results.</p>"""
    implicit_filter_configuration: NotRequired[
        "capo_bedrock.types.implicit_filter_configuration.ImplicitFilterConfiguration"
    ]
    """<p>Configuration for implicit filtering in Knowledge Base vector searches. This allows the system to automatically apply filters based on the query context without requiring explicit filter expressions.</p>"""
    reranking_configuration: NotRequired[
        "capo_bedrock.types.vector_search_reranking_configuration.VectorSearchRerankingConfiguration"
    ]
    """<p>Configuration for reranking search results in Knowledge Base vector searches. Reranking improves search relevance by reordering initial vector search results using more sophisticated relevance models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseVectorSearchConfiguration) -> dict:
    out: dict = {}
    if "number_of_results" in value:
        out["numberOfResults"] = value["number_of_results"]
    if "override_search_type" in value:
        import capo_bedrock.types.search_type

        out["overrideSearchType"] = capo_bedrock.types.search_type.serialize_json(
            value["override_search_type"]
        )
    if "filter" in value:
        import capo_bedrock.types.retrieval_filter

        out["filter"] = capo_bedrock.types.retrieval_filter.serialize_json(
            value["filter"]
        )
    if "implicit_filter_configuration" in value:
        import capo_bedrock.types.implicit_filter_configuration

        out["implicitFilterConfiguration"] = (
            capo_bedrock.types.implicit_filter_configuration.serialize_json(
                value["implicit_filter_configuration"]
            )
        )
    if "reranking_configuration" in value:
        import capo_bedrock.types.vector_search_reranking_configuration

        out["rerankingConfiguration"] = (
            capo_bedrock.types.vector_search_reranking_configuration.serialize_json(
                value["reranking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseVectorSearchConfiguration:
    out: KnowledgeBaseVectorSearchConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("numberOfResults") is not None:
        out["number_of_results"] = data["numberOfResults"]
    if data.get("overrideSearchType") is not None:
        import capo_bedrock.types.search_type

        out["override_search_type"] = capo_bedrock.types.search_type.deserialize_json(
            data["overrideSearchType"]
        )
    if data.get("filter") is not None:
        import capo_bedrock.types.retrieval_filter

        out["filter"] = capo_bedrock.types.retrieval_filter.deserialize_json(
            data["filter"]
        )
    if data.get("implicitFilterConfiguration") is not None:
        import capo_bedrock.types.implicit_filter_configuration

        out["implicit_filter_configuration"] = (
            capo_bedrock.types.implicit_filter_configuration.deserialize_json(
                data["implicitFilterConfiguration"]
            )
        )
    if data.get("rerankingConfiguration") is not None:
        import capo_bedrock.types.vector_search_reranking_configuration

        out["reranking_configuration"] = (
            capo_bedrock.types.vector_search_reranking_configuration.deserialize_json(
                data["rerankingConfiguration"]
            )
        )
    return out


def redact_sensitive(value: KnowledgeBaseVectorSearchConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter" in value:
        out["filter"] = "*** Sensitive Data Redacted ***"
    if "implicit_filter_configuration" in value:
        import capo_bedrock.types.implicit_filter_configuration

        out["implicit_filter_configuration"] = (
            capo_bedrock.types.implicit_filter_configuration.redact_sensitive(
                value["implicit_filter_configuration"]
            )
        )
    if "reranking_configuration" in value:
        import capo_bedrock.types.vector_search_reranking_configuration

        out["reranking_configuration"] = (
            capo_bedrock.types.vector_search_reranking_configuration.redact_sensitive(
                value["reranking_configuration"]
            )
        )
    return out
