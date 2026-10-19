"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentKnowledgeBasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_knowledge_base_summaries
    import capo_bedrock_agent.types.next_token


class ListAgentKnowledgeBasesResponse(TypedDict, closed=True):
    agent_knowledge_base_summaries: "capo_bedrock_agent.types.agent_knowledge_base_summaries.AgentKnowledgeBaseSummaries"
    """<p>A list of objects, each of which contains information about a knowledge base associated with the agent.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentKnowledgeBasesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_knowledge_base_summaries

    out["agentKnowledgeBaseSummaries"] = (
        capo_bedrock_agent.types.agent_knowledge_base_summaries.serialize_json(
            value["agent_knowledge_base_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentKnowledgeBasesResponse:
    out: ListAgentKnowledgeBasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentKnowledgeBaseSummaries") is not None:
        import capo_bedrock_agent.types.agent_knowledge_base_summaries

        out["agent_knowledge_base_summaries"] = (
            capo_bedrock_agent.types.agent_knowledge_base_summaries.deserialize_json(
                data["agentKnowledgeBaseSummaries"]
            )
        )
    else:
        out["agent_knowledge_base_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
