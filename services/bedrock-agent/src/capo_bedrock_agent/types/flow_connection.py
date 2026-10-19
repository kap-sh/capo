"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_connection_configuration
    import capo_bedrock_agent.types.flow_connection_name
    import capo_bedrock_agent.types.flow_connection_type
    import capo_bedrock_agent.types.flow_node_name


class FlowConnection(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.flow_connection_type.FlowConnectionType"
    """<p>Whether the source node that the connection begins from is a condition node (<code>Conditional</code>) or not (<code>Data</code>).</p>"""
    name: "capo_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>A name for the connection that you can reference.</p>"""
    source: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The node that the connection starts at.</p>"""
    target: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The node that the connection ends at.</p>"""
    configuration: NotRequired[
        "capo_bedrock_agent.types.flow_connection_configuration.FlowConnectionConfiguration"
    ]
    """<p>The configuration of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowConnection) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.flow_connection_type

    out["type"] = capo_bedrock_agent.types.flow_connection_type.serialize_json(
        value["type"]
    )
    out["name"] = value["name"]
    out["source"] = value["source"]
    out["target"] = value["target"]
    if "configuration" in value:
        import capo_bedrock_agent.types.flow_connection_configuration

        out["configuration"] = (
            capo_bedrock_agent.types.flow_connection_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowConnection:
    out: FlowConnection = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.flow_connection_type

        out["type"] = capo_bedrock_agent.types.flow_connection_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.flow_connection_type.FlowConnectionType", ""
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("target") is not None:
        out["target"] = data["target"]
    else:
        out["target"] = ""
    if data.get("configuration") is not None:
        import capo_bedrock_agent.types.flow_connection_configuration

        out["configuration"] = (
            capo_bedrock_agent.types.flow_connection_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
