"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_version_summaries
    import capo_bedrock_agent.types.next_token


class ListAgentVersionsResponse(TypedDict, closed=True):
    agent_version_summaries: (
        "capo_bedrock_agent.types.agent_version_summaries.AgentVersionSummaries"
    )
    """<p>A list of objects, each of which contains information about a version of the agent.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentVersionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_version_summaries

    out["agentVersionSummaries"] = (
        capo_bedrock_agent.types.agent_version_summaries.serialize_json(
            value["agent_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentVersionsResponse:
    out: ListAgentVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentVersionSummaries") is not None:
        import capo_bedrock_agent.types.agent_version_summaries

        out["agent_version_summaries"] = (
            capo_bedrock_agent.types.agent_version_summaries.deserialize_json(
                data["agentVersionSummaries"]
            )
        )
    else:
        out["agent_version_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
