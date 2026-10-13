"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentCollaboratorSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_collaborator_summary

AgentCollaboratorSummaries: TypeAlias = list[
    "capo_bedrock_agent.types.agent_collaborator_summary.AgentCollaboratorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorSummaries) -> list:
    import capo_bedrock_agent.types.agent_collaborator_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.agent_collaborator_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentCollaboratorSummaries:
    import capo_bedrock_agent.types.agent_collaborator_summary

    out: AgentCollaboratorSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.agent_collaborator_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AgentCollaboratorSummaries) -> list[Any]:
    import capo_bedrock_agent.types.agent_collaborator_summary

    return [
        capo_bedrock_agent.types.agent_collaborator_summary.redact_sensitive(item)
        for item in value
    ]
