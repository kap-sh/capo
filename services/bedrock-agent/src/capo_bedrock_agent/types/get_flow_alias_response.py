"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetFlowAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.flow_alias_arn
    import capo_bedrock_agent.types.flow_alias_concurrency_configuration
    import capo_bedrock_agent.types.flow_alias_id
    import capo_bedrock_agent.types.flow_alias_routing_configuration
    import capo_bedrock_agent.types.flow_id
    import capo_bedrock_agent.types.name


class GetFlowAliasResponse(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the alias.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the flow.</p>"""
    routing_configuration: "capo_bedrock_agent.types.flow_alias_routing_configuration.FlowAliasRoutingConfiguration"
    """<p>Contains information about the version that the alias is mapped to.</p>"""
    concurrency_configuration: NotRequired[
        "capo_bedrock_agent.types.flow_alias_concurrency_configuration.FlowAliasConcurrencyConfiguration"
    ]
    """<p>The configuration that specifies how nodes in the flow are executed in parallel.</p>"""
    flow_id: "capo_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow that the alias belongs to.</p>"""
    id: "capo_bedrock_agent.types.flow_alias_id.FlowAliasId"
    """<p>The unique identifier of the alias of the flow.</p>"""
    arn: "capo_bedrock_agent.types.flow_alias_arn.FlowAliasArn"
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the flow was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowAliasResponse) -> dict:
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
    out["flowId"] = value["flow_id"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetFlowAliasResponse:
    out: GetFlowAliasResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
        out["routing_configuration"] = []
    if data.get("concurrencyConfiguration") is not None:
        import capo_bedrock_agent.types.flow_alias_concurrency_configuration

        out["concurrency_configuration"] = (
            capo_bedrock_agent.types.flow_alias_concurrency_configuration.deserialize_json(
                data["concurrencyConfiguration"]
            )
        )
    if data.get("flowId") is not None:
        out["flow_id"] = data["flowId"]
    else:
        out["flow_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
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
    return out
