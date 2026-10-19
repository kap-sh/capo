"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentCollaboratorSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_descriptor
    import capo_bedrock_agent.types.collaboration_instruction
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.relay_conversation_history
    import capo_bedrock_agent.types.version


class AgentCollaboratorSummary(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The collaborator's agent ID.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The collaborator's agent version.</p>"""
    collaborator_id: "capo_bedrock_agent.types.id.Id"
    """<p>The collaborator's ID.</p>"""
    agent_descriptor: "capo_bedrock_agent.types.agent_descriptor.AgentDescriptor"
    """<p>The collaborator's agent descriptor.</p>"""
    collaboration_instruction: (
        "capo_bedrock_agent.types.collaboration_instruction.CollaborationInstruction"
    )
    """<p>The collaborator's collaboration instruction.</p>"""
    relay_conversation_history: (
        "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
    )
    """<p>The collaborator's relay conversation history.</p>"""
    collaborator_name: "capo_bedrock_agent.types.name.Name"
    """<p>The collaborator's name.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When the collaborator was created.</p>"""
    last_updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When the collaborator was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorSummary) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentVersion"] = value["agent_version"]
    out["collaboratorId"] = value["collaborator_id"]
    import capo_bedrock_agent.types.agent_descriptor

    out["agentDescriptor"] = capo_bedrock_agent.types.agent_descriptor.serialize_json(
        value["agent_descriptor"]
    )
    out["collaborationInstruction"] = value["collaboration_instruction"]
    import capo_bedrock_agent.types.relay_conversation_history

    out["relayConversationHistory"] = (
        capo_bedrock_agent.types.relay_conversation_history.serialize_json(
            value["relay_conversation_history"]
        )
    )
    out["collaboratorName"] = value["collaborator_name"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["lastUpdatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorSummary:
    out: AgentCollaboratorSummary = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        out["agent_id"] = ""
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    else:
        out["agent_version"] = ""
    if data.get("collaboratorId") is not None:
        out["collaborator_id"] = data["collaboratorId"]
    else:
        out["collaborator_id"] = ""
    if data.get("agentDescriptor") is not None:
        import capo_bedrock_agent.types.agent_descriptor

        out["agent_descriptor"] = (
            capo_bedrock_agent.types.agent_descriptor.deserialize_json(
                data["agentDescriptor"]
            )
        )
    else:
        raise DeserializationError("AgentCollaboratorSummary.agent_descriptor required")
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
    else:
        import typing

        out["relay_conversation_history"] = typing.cast(
            "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory",
            "",
        )
    if data.get("collaboratorName") is not None:
        out["collaborator_name"] = data["collaboratorName"]
    else:
        out["collaborator_name"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agent.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out


def redact_sensitive(value: AgentCollaboratorSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "collaboration_instruction" in value:
        out["collaboration_instruction"] = "*** Sensitive Data Redacted ***"
    return out
