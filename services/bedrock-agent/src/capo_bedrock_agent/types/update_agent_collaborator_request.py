"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentCollaboratorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_descriptor
    import capo_bedrock_agent.types.collaboration_instruction
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.relay_conversation_history


class UpdateAgentCollaboratorRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The agent's ID.</p>"""
    agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The agent's version.</p>"""
    collaborator_id: "capo_bedrock_agent.types.id.Id"
    """<p>The collaborator's ID.</p>"""
    agent_descriptor: "capo_bedrock_agent.types.agent_descriptor.AgentDescriptor"
    """<p>An agent descriptor for the agent collaborator.</p>"""
    collaborator_name: "capo_bedrock_agent.types.name.Name"
    """<p>The collaborator's name.</p>"""
    collaboration_instruction: (
        "capo_bedrock_agent.types.collaboration_instruction.CollaborationInstruction"
    )
    """<p>Instruction for the collaborator.</p>"""
    relay_conversation_history: NotRequired[
        "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
    ]
    """<p>A relay conversation history for the collaborator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentCollaboratorRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_descriptor

    out["agentDescriptor"] = capo_bedrock_agent.types.agent_descriptor.serialize_json(
        value["agent_descriptor"]
    )
    out["collaboratorName"] = value["collaborator_name"]
    out["collaborationInstruction"] = value["collaboration_instruction"]
    if "relay_conversation_history" in value:
        import capo_bedrock_agent.types.relay_conversation_history

        out["relayConversationHistory"] = (
            capo_bedrock_agent.types.relay_conversation_history.serialize_json(
                value["relay_conversation_history"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentCollaboratorRequest:
    out: UpdateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentDescriptor") is not None:
        import capo_bedrock_agent.types.agent_descriptor

        out["agent_descriptor"] = (
            capo_bedrock_agent.types.agent_descriptor.deserialize_json(
                data["agentDescriptor"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAgentCollaboratorRequest.agent_descriptor required"
        )
    if data.get("collaboratorName") is not None:
        out["collaborator_name"] = data["collaboratorName"]
    else:
        out["collaborator_name"] = ""
    if data.get("collaborationInstruction") is not None:
        out["collaboration_instruction"] = data["collaborationInstruction"]
    else:
        out["collaboration_instruction"] = ""
    if data.get("relayConversationHistory") is not None:
        import capo_bedrock_agent.types.relay_conversation_history

        out["relay_conversation_history"] = (
            capo_bedrock_agent.types.relay_conversation_history.deserialize_json(
                data["relayConversationHistory"]
            )
        )
    return out


def redact_sensitive(value: UpdateAgentCollaboratorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "collaboration_instruction" in value:
        out["collaboration_instruction"] = "*** Sensitive Data Redacted ***"
    return out
