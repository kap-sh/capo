"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateAgentAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_alias_routing_configuration
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.tags_map


class CreateAgentAliasRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_alias_name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the alias.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>A description of the alias of the agent.</p>"""
    routing_configuration: NotRequired[
        "capo_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
    ]
    """<p>Contains details about the routing configuration of the alias.</p>"""
    tags: NotRequired["capo_bedrock_agent.types.tags_map.TagsMap"]
    """<p>Any tags that you want to attach to the alias of the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentAliasRequest) -> dict:
    out: dict = {}
    out["agentAliasName"] = value["agent_alias_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "routing_configuration" in value:
        import capo_bedrock_agent.types.agent_alias_routing_configuration

        out["routingConfiguration"] = (
            capo_bedrock_agent.types.agent_alias_routing_configuration.serialize_json(
                value["routing_configuration"]
            )
        )
    if "tags" in value:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentAliasRequest:
    out: CreateAgentAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentAliasName") is not None:
        out["agent_alias_name"] = data["agentAliasName"]
    else:
        raise DeserializationError("CreateAgentAliasRequest.agent_alias_name required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("routingConfiguration") is not None:
        import capo_bedrock_agent.types.agent_alias_routing_configuration

        out["routing_configuration"] = (
            capo_bedrock_agent.types.agent_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.deserialize_json(data["tags"])
    return out
