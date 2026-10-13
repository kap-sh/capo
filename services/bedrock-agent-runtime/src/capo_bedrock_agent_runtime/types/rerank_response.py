"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.rerank_results_list


class RerankResponse(TypedDict, closed=True):
    results: "capo_bedrock_agent_runtime.types.rerank_results_list.RerankResultsList"
    """<p>An array of objects, each of which contains information about the results of reranking.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results is greater than can fit in the response, use this token in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.rerank_results_list

    out["results"] = (
        capo_bedrock_agent_runtime.types.rerank_results_list.serialize_json(
            value["results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> RerankResponse:
    out: RerankResponse = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_bedrock_agent_runtime.types.rerank_results_list

        out["results"] = (
            capo_bedrock_agent_runtime.types.rerank_results_list.deserialize_json(
                data["results"]
            )
        )
    else:
        raise DeserializationError("RerankResponse.results required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: RerankResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_bedrock_agent_runtime.types.rerank_results_list

        out["results"] = (
            capo_bedrock_agent_runtime.types.rerank_results_list.redact_sensitive(
                value["results"]
            )
        )
    return out
