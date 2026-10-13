"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboratorInvocationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_alias_arn
    import capo_bedrock_agent_runtime.types.agent_collaborator_input_payload


class AgentCollaboratorInvocationInput(TypedDict, closed=True):
    agent_collaborator_name: NotRequired["str"]
    """<p>The collaborator's name.</p>"""
    agent_collaborator_alias_arn: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_alias_arn.AgentAliasArn"
    ]
    """<p>The collaborator's alias ARN.</p>"""
    input: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_collaborator_input_payload.AgentCollaboratorInputPayload"
    ]
    """<p>Text or action invocation result input for the collaborator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorInvocationInput) -> dict:
    out: dict = {}
    if "agent_collaborator_name" in value:
        out["agentCollaboratorName"] = value["agent_collaborator_name"]
    if "agent_collaborator_alias_arn" in value:
        out["agentCollaboratorAliasArn"] = value["agent_collaborator_alias_arn"]
    if "input" in value:
        import capo_bedrock_agent_runtime.types.agent_collaborator_input_payload

        out["input"] = (
            capo_bedrock_agent_runtime.types.agent_collaborator_input_payload.serialize_json(
                value["input"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorInvocationInput:
    out: AgentCollaboratorInvocationInput = {}  # type: ignore[typeddict-item]
    if data.get("agentCollaboratorName") is not None:
        out["agent_collaborator_name"] = data["agentCollaboratorName"]
    if data.get("agentCollaboratorAliasArn") is not None:
        out["agent_collaborator_alias_arn"] = data["agentCollaboratorAliasArn"]
    if data.get("input") is not None:
        import capo_bedrock_agent_runtime.types.agent_collaborator_input_payload

        out["input"] = (
            capo_bedrock_agent_runtime.types.agent_collaborator_input_payload.deserialize_json(
                data["input"]
            )
        )
    return out


def redact_sensitive(value: AgentCollaboratorInvocationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        import capo_bedrock_agent_runtime.types.agent_collaborator_input_payload

        out["input"] = (
            capo_bedrock_agent_runtime.types.agent_collaborator_input_payload.redact_sensitive(
                value["input"]
            )
        )
    return out
