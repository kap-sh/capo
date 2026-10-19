"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListKnowledgeBasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.knowledge_base_summaries
    import capo_bedrock_agent.types.next_token


class ListKnowledgeBasesResponse(TypedDict, closed=True):
    knowledge_base_summaries: (
        "capo_bedrock_agent.types.knowledge_base_summaries.KnowledgeBaseSummaries"
    )
    """<p>A list of knowledge bases with information about each knowledge base.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKnowledgeBasesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.knowledge_base_summaries

    out["knowledgeBaseSummaries"] = (
        capo_bedrock_agent.types.knowledge_base_summaries.serialize_json(
            value["knowledge_base_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKnowledgeBasesResponse:
    out: ListKnowledgeBasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseSummaries") is not None:
        import capo_bedrock_agent.types.knowledge_base_summaries

        out["knowledge_base_summaries"] = (
            capo_bedrock_agent.types.knowledge_base_summaries.deserialize_json(
                data["knowledgeBaseSummaries"]
            )
        )
    else:
        out["knowledge_base_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
