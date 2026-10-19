"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CollaboratorConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_alias_arn
    import capo_bedrock_agent_runtime.types.collaboration_instruction
    import capo_bedrock_agent_runtime.types.name
    import capo_bedrock_agent_runtime.types.relay_conversation_history


class CollaboratorConfiguration(TypedDict, closed=True):
    collaborator_name: "capo_bedrock_agent_runtime.types.name.Name"
    """<p> Name of the inline collaborator agent which must be the same name as specified for <code>agentName</code>. </p>"""
    collaborator_instruction: "capo_bedrock_agent_runtime.types.collaboration_instruction.CollaborationInstruction"
    """<p> Instructions that tell the inline collaborator agent what it should do and how it should interact with users. </p>"""
    agent_alias_arn: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_alias_arn.AgentAliasArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the inline collaborator agent. </p>"""
    relay_conversation_history: NotRequired[
        "capo_bedrock_agent_runtime.types.relay_conversation_history.RelayConversationHistory"
    ]
    """<p> A relay conversation history for the inline collaborator agent. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaboratorConfiguration) -> dict:
    out: dict = {}
    out["collaboratorName"] = value["collaborator_name"]
    out["collaboratorInstruction"] = value["collaborator_instruction"]
    if "agent_alias_arn" in value:
        out["agentAliasArn"] = value["agent_alias_arn"]
    if "relay_conversation_history" in value:
        import capo_bedrock_agent_runtime.types.relay_conversation_history

        out["relayConversationHistory"] = (
            capo_bedrock_agent_runtime.types.relay_conversation_history.serialize_json(
                value["relay_conversation_history"]
            )
        )
    return out


def deserialize_json(data: dict) -> CollaboratorConfiguration:
    out: CollaboratorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("collaboratorName") is not None:
        out["collaborator_name"] = data["collaboratorName"]
    else:
        out["collaborator_name"] = ""
    if data.get("collaboratorInstruction") is not None:
        out["collaborator_instruction"] = data["collaboratorInstruction"]
    else:
        out["collaborator_instruction"] = ""
    if data.get("agentAliasArn") is not None:
        out["agent_alias_arn"] = data["agentAliasArn"]
    if data.get("relayConversationHistory") is not None:
        import capo_bedrock_agent_runtime.types.relay_conversation_history

        out["relay_conversation_history"] = (
            capo_bedrock_agent_runtime.types.relay_conversation_history.deserialize_json(
                data["relayConversationHistory"]
            )
        )
    return out


def redact_sensitive(value: CollaboratorConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "collaborator_name" in value:
        out["collaborator_name"] = "*** Sensitive Data Redacted ***"
    if "collaborator_instruction" in value:
        out["collaborator_instruction"] = "*** Sensitive Data Redacted ***"
    return out
