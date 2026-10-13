"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboratorInvocationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_alias_arn
    import capo_bedrock_agent_runtime.types.agent_collaborator_output_payload
    import capo_bedrock_agent_runtime.types.metadata


class AgentCollaboratorInvocationOutput(TypedDict, closed=True):
    agent_collaborator_name: NotRequired["str"]
    """<p>The output's agent collaborator name.</p>"""
    agent_collaborator_alias_arn: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_alias_arn.AgentAliasArn"
    ]
    """<p>The output's agent collaborator alias ARN.</p>"""
    output: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_collaborator_output_payload.AgentCollaboratorOutputPayload"
    ]
    """<p>The output's output.</p>"""
    metadata: NotRequired["capo_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the output from the agent collaborator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorInvocationOutput) -> dict:
    out: dict = {}
    if "agent_collaborator_name" in value:
        out["agentCollaboratorName"] = value["agent_collaborator_name"]
    if "agent_collaborator_alias_arn" in value:
        out["agentCollaboratorAliasArn"] = value["agent_collaborator_alias_arn"]
    if "output" in value:
        import capo_bedrock_agent_runtime.types.agent_collaborator_output_payload

        out["output"] = (
            capo_bedrock_agent_runtime.types.agent_collaborator_output_payload.serialize_json(
                value["output"]
            )
        )
    if "metadata" in value:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorInvocationOutput:
    out: AgentCollaboratorInvocationOutput = {}  # type: ignore[typeddict-item]
    if data.get("agentCollaboratorName") is not None:
        out["agent_collaborator_name"] = data["agentCollaboratorName"]
    if data.get("agentCollaboratorAliasArn") is not None:
        out["agent_collaborator_alias_arn"] = data["agentCollaboratorAliasArn"]
    if data.get("output") is not None:
        import capo_bedrock_agent_runtime.types.agent_collaborator_output_payload

        out["output"] = (
            capo_bedrock_agent_runtime.types.agent_collaborator_output_payload.deserialize_json(
                data["output"]
            )
        )
    if data.get("metadata") is not None:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out


def redact_sensitive(value: AgentCollaboratorInvocationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "output" in value:
        import capo_bedrock_agent_runtime.types.agent_collaborator_output_payload

        out["output"] = (
            capo_bedrock_agent_runtime.types.agent_collaborator_output_payload.redact_sensitive(
                value["output"]
            )
        )
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
