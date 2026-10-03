"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateFlowAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.flow_alias_concurrency_configuration
    import capo_bedrock_agent.types.flow_alias_routing_configuration
    import capo_bedrock_agent.types.flow_identifier
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.tags_map


class CreateFlowAliasRequest(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.name.Name"
    """<p>A name for the alias.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>A description for the alias.</p>"""
    routing_configuration: "capo_bedrock_agent.types.flow_alias_routing_configuration.FlowAliasRoutingConfiguration"
    """<p>Contains information about the version to which to map the alias.</p>"""
    concurrency_configuration: NotRequired[
        "capo_bedrock_agent.types.flow_alias_concurrency_configuration.FlowAliasConcurrencyConfiguration"
    ]
    """<p>The configuration that specifies how nodes in the flow are executed in parallel.</p>"""
    flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow for which to create an alias.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    tags: NotRequired["capo_bedrock_agent.types.tags_map.TagsMap"]
    """<p>Any tags that you want to attach to the alias of the flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowAliasRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.flow_alias_routing_configuration

    out["routingConfiguration"] = (
        capo_bedrock_agent.types.flow_alias_routing_configuration.serialize_json(
            value["routing_configuration"]
        )
    )
    if "concurrency_configuration" in value:
        import capo_bedrock_agent.types.flow_alias_concurrency_configuration

        out["concurrencyConfiguration"] = (
            capo_bedrock_agent.types.flow_alias_concurrency_configuration.serialize_json(
                value["concurrency_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateFlowAliasRequest:
    out: CreateFlowAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFlowAliasRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("routingConfiguration") is not None:
        import capo_bedrock_agent.types.flow_alias_routing_configuration

        out["routing_configuration"] = (
            capo_bedrock_agent.types.flow_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateFlowAliasRequest.routing_configuration required"
        )
    if data.get("concurrencyConfiguration") is not None:
        import capo_bedrock_agent.types.flow_alias_concurrency_configuration

        out["concurrency_configuration"] = (
            capo_bedrock_agent.types.flow_alias_concurrency_configuration.deserialize_json(
                data["concurrencyConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.deserialize_json(data["tags"])
    return out
