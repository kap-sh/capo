"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_alias_id
    import capo_bedrock_agent.types.agent_alias_routing_configuration
    import capo_bedrock_agent.types.alias_invocation_state
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name


class UpdateAgentAliasRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId"
    """<p>The unique identifier of the alias.</p>"""
    agent_alias_name: "capo_bedrock_agent.types.name.Name"
    """<p>Specifies a new name for the alias.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>Specifies a new description for the alias.</p>"""
    routing_configuration: NotRequired[
        "capo_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
    ]
    """<p>Contains details about the routing configuration of the alias.</p>"""
    alias_invocation_state: NotRequired[
        "capo_bedrock_agent.types.alias_invocation_state.AliasInvocationState"
    ]
    """<p>The invocation state for the agent alias. To pause the agent alias, set the value to <code>REJECT_INVOCATIONS</code>. To start the agent alias running again, set the value to <code>ACCEPT_INVOCATIONS</code>. Use the <code>GetAgentAlias</code>, or <code>ListAgentAliases</code>, operation to get the invocation state of an agent alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentAliasRequest) -> dict:
    out: dict = {}
    out["agentAliasName"] = value["agent_alias_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "routing_configuration" in value:
        import capo_bedrock_agent.types.agent_alias_routing_configuration

        out["routingConfiguration"] = (
            capo_bedrock_agent.types.agent_alias_routing_configuration.serialize_json(
                value["routing_configuration"]
            )
        )
    if "alias_invocation_state" in value:
        import capo_bedrock_agent.types.alias_invocation_state

        out["aliasInvocationState"] = (
            capo_bedrock_agent.types.alias_invocation_state.serialize_json(
                value["alias_invocation_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentAliasRequest:
    out: UpdateAgentAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentAliasName") is not None:
        out["agent_alias_name"] = data["agentAliasName"]
    else:
        out["agent_alias_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("routingConfiguration") is not None:
        import capo_bedrock_agent.types.agent_alias_routing_configuration

        out["routing_configuration"] = (
            capo_bedrock_agent.types.agent_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    if data.get("aliasInvocationState") is not None:
        import capo_bedrock_agent.types.alias_invocation_state

        out["alias_invocation_state"] = (
            capo_bedrock_agent.types.alias_invocation_state.deserialize_json(
                data["aliasInvocationState"]
            )
        )
    return out
