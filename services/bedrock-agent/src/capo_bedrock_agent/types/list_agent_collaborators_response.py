"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentCollaboratorsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_collaborator_summaries
    import capo_bedrock_agent.types.next_token


class ListAgentCollaboratorsResponse(TypedDict, closed=True):
    agent_collaborator_summaries: "capo_bedrock_agent.types.agent_collaborator_summaries.AgentCollaboratorSummaries"
    """<p>A list of collaborator summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentCollaboratorsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_collaborator_summaries

    out["agentCollaboratorSummaries"] = (
        capo_bedrock_agent.types.agent_collaborator_summaries.serialize_json(
            value["agent_collaborator_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentCollaboratorsResponse:
    out: ListAgentCollaboratorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentCollaboratorSummaries") is not None:
        import capo_bedrock_agent.types.agent_collaborator_summaries

        out["agent_collaborator_summaries"] = (
            capo_bedrock_agent.types.agent_collaborator_summaries.deserialize_json(
                data["agentCollaboratorSummaries"]
            )
        )
    else:
        out["agent_collaborator_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAgentCollaboratorsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_collaborator_summaries" in value:
        import capo_bedrock_agent.types.agent_collaborator_summaries

        out["agent_collaborator_summaries"] = (
            capo_bedrock_agent.types.agent_collaborator_summaries.redact_sensitive(
                value["agent_collaborator_summaries"]
            )
        )
    return out
