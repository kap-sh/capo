"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guadrail_action
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_results
    import capo_bedrock_agent_runtime.types.next_token


class RetrieveResponse(TypedDict, closed=True):
    retrieval_results: "capo_bedrock_agent_runtime.types.knowledge_base_retrieval_results.KnowledgeBaseRetrievalResults"
    """<p>A list of results from querying the knowledge base.</p>"""
    guardrail_action: NotRequired[
        "capo_bedrock_agent_runtime.types.guadrail_action.GuadrailAction"
    ]
    """<p>Specifies if there is a guardrail intervention in the response.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If there are more results than can fit in the response, the response returns a <code>nextToken</code>. Use this token in the <code>nextToken</code> field of another request to retrieve the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_results

    out["retrievalResults"] = (
        capo_bedrock_agent_runtime.types.knowledge_base_retrieval_results.serialize_json(
            value["retrieval_results"]
        )
    )
    if "guardrail_action" in value:
        import capo_bedrock_agent_runtime.types.guadrail_action

        out["guardrailAction"] = (
            capo_bedrock_agent_runtime.types.guadrail_action.serialize_json(
                value["guardrail_action"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> RetrieveResponse:
    out: RetrieveResponse = {}  # type: ignore[typeddict-item]
    if data.get("retrievalResults") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_results

        out["retrieval_results"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_retrieval_results.deserialize_json(
                data["retrievalResults"]
            )
        )
    else:
        out["retrieval_results"] = []
    if data.get("guardrailAction") is not None:
        import capo_bedrock_agent_runtime.types.guadrail_action

        out["guardrail_action"] = (
            capo_bedrock_agent_runtime.types.guadrail_action.deserialize_json(
                data["guardrailAction"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: RetrieveResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "retrieval_results" in value:
        out["retrieval_results"] = "*** Sensitive Data Redacted ***"
    return out
