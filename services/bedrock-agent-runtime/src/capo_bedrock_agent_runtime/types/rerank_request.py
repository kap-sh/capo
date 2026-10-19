"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.rerank_queries_list
    import capo_bedrock_agent_runtime.types.rerank_sources_list
    import capo_bedrock_agent_runtime.types.reranking_configuration


class RerankRequest(TypedDict, closed=True):
    queries: "capo_bedrock_agent_runtime.types.rerank_queries_list.RerankQueriesList"
    """<p>An array of objects, each of which contains information about a query to submit to the reranker model.</p>"""
    sources: "capo_bedrock_agent_runtime.types.rerank_sources_list.RerankSourcesList"
    """<p>An array of objects, each of which contains information about the sources to rerank.</p>"""
    reranking_configuration: "capo_bedrock_agent_runtime.types.reranking_configuration.RerankingConfiguration"
    """<p>Contains configurations for reranking.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results was greater than could fit in a response, a token is returned in the <code>nextToken</code> field. You can enter that token in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.rerank_queries_list

    out["queries"] = (
        capo_bedrock_agent_runtime.types.rerank_queries_list.serialize_json(
            value["queries"]
        )
    )
    import capo_bedrock_agent_runtime.types.rerank_sources_list

    out["sources"] = (
        capo_bedrock_agent_runtime.types.rerank_sources_list.serialize_json(
            value["sources"]
        )
    )
    import capo_bedrock_agent_runtime.types.reranking_configuration

    out["rerankingConfiguration"] = (
        capo_bedrock_agent_runtime.types.reranking_configuration.serialize_json(
            value["reranking_configuration"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> RerankRequest:
    out: RerankRequest = {}  # type: ignore[typeddict-item]
    if data.get("queries") is not None:
        import capo_bedrock_agent_runtime.types.rerank_queries_list

        out["queries"] = (
            capo_bedrock_agent_runtime.types.rerank_queries_list.deserialize_json(
                data["queries"]
            )
        )
    else:
        out["queries"] = []
    if data.get("sources") is not None:
        import capo_bedrock_agent_runtime.types.rerank_sources_list

        out["sources"] = (
            capo_bedrock_agent_runtime.types.rerank_sources_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    if data.get("rerankingConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.reranking_configuration

        out["reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.reranking_configuration.deserialize_json(
                data["rerankingConfiguration"]
            )
        )
    else:
        raise DeserializationError("RerankRequest.reranking_configuration required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: RerankRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "queries" in value:
        out["queries"] = "*** Sensitive Data Redacted ***"
    if "sources" in value:
        out["sources"] = "*** Sensitive Data Redacted ***"
    return out
