"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_alias_id
    import capo_bedrock_agent.types.agent_alias_routing_configuration
    import capo_bedrock_agent.types.agent_alias_status
    import capo_bedrock_agent.types.alias_invocation_state
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.name


class AgentAliasSummary(TypedDict, closed=True):
    agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId"
    """<p>Contains details about </p>"""
    agent_alias_name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the alias.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the alias.</p>"""
    routing_configuration: NotRequired[
        "capo_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
    ]
    """<p>Contains details about the version of the agent with which the alias is associated.</p>"""
    agent_alias_status: "capo_bedrock_agent.types.agent_alias_status.AgentAliasStatus"
    """<p>The status of the alias.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias of the agent was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias was last updated.</p>"""
    alias_invocation_state: NotRequired[
        "capo_bedrock_agent.types.alias_invocation_state.AliasInvocationState"
    ]
    """<p>The invocation state for the agent alias. If the agent alias is running, the value is <code>ACCEPT_INVOCATIONS</code>. If the agent alias is paused, the value is <code>REJECT_INVOCATIONS</code>. Use the <code>UpdateAgentAlias</code> operation to change the invocation state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentAliasSummary) -> dict:
    out: dict = {}
    out["agentAliasId"] = value["agent_alias_id"]
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
    import capo_bedrock_agent.types.agent_alias_status

    out["agentAliasStatus"] = (
        capo_bedrock_agent.types.agent_alias_status.serialize_json(
            value["agent_alias_status"]
        )
    )
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "alias_invocation_state" in value:
        import capo_bedrock_agent.types.alias_invocation_state

        out["aliasInvocationState"] = (
            capo_bedrock_agent.types.alias_invocation_state.serialize_json(
                value["alias_invocation_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentAliasSummary:
    out: AgentAliasSummary = {}  # type: ignore[typeddict-item]
    if data.get("agentAliasId") is not None:
        out["agent_alias_id"] = data["agentAliasId"]
    else:
        out["agent_alias_id"] = ""
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
    if data.get("agentAliasStatus") is not None:
        import capo_bedrock_agent.types.agent_alias_status

        out["agent_alias_status"] = (
            capo_bedrock_agent.types.agent_alias_status.deserialize_json(
                data["agentAliasStatus"]
            )
        )
    else:
        import typing

        out["agent_alias_status"] = typing.cast(
            "capo_bedrock_agent.types.agent_alias_status.AgentAliasStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("aliasInvocationState") is not None:
        import capo_bedrock_agent.types.alias_invocation_state

        out["alias_invocation_state"] = (
            capo_bedrock_agent.types.alias_invocation_state.deserialize_json(
                data["aliasInvocationState"]
            )
        )
    return out
