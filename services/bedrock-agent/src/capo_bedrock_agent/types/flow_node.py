"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNode``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_configuration
    import capo_bedrock_agent.types.flow_node_inputs
    import capo_bedrock_agent.types.flow_node_name
    import capo_bedrock_agent.types.flow_node_outputs
    import capo_bedrock_agent.types.flow_node_type


class FlowNode(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>A name for the node.</p>"""
    type: "capo_bedrock_agent.types.flow_node_type.FlowNodeType"
    """<p>The type of node. This value must match the name of the key that you provide in the configuration you provide in the <code>FlowNodeConfiguration</code> field.</p>"""
    configuration: NotRequired[
        "capo_bedrock_agent.types.flow_node_configuration.FlowNodeConfiguration"
    ]
    """<p>Contains configurations for the node.</p>"""
    inputs: NotRequired["capo_bedrock_agent.types.flow_node_inputs.FlowNodeInputs"]
    """<p>An array of objects, each of which contains information about an input into the node.</p>"""
    outputs: NotRequired["capo_bedrock_agent.types.flow_node_outputs.FlowNodeOutputs"]
    """<p>A list of objects, each of which contains information about an output from the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowNode) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agent.types.flow_node_type

    out["type"] = capo_bedrock_agent.types.flow_node_type.serialize_json(value["type"])
    if "configuration" in value:
        import capo_bedrock_agent.types.flow_node_configuration

        out["configuration"] = (
            capo_bedrock_agent.types.flow_node_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "inputs" in value:
        import capo_bedrock_agent.types.flow_node_inputs

        out["inputs"] = capo_bedrock_agent.types.flow_node_inputs.serialize_json(
            value["inputs"]
        )
    if "outputs" in value:
        import capo_bedrock_agent.types.flow_node_outputs

        out["outputs"] = capo_bedrock_agent.types.flow_node_outputs.serialize_json(
            value["outputs"]
        )
    return out


def deserialize_json(data: dict) -> FlowNode:
    out: FlowNode = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FlowNode.name required")
    if data.get("type") is not None:
        import capo_bedrock_agent.types.flow_node_type

        out["type"] = capo_bedrock_agent.types.flow_node_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("FlowNode.type required")
    if data.get("configuration") is not None:
        import capo_bedrock_agent.types.flow_node_configuration

        out["configuration"] = (
            capo_bedrock_agent.types.flow_node_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if data.get("inputs") is not None:
        import capo_bedrock_agent.types.flow_node_inputs

        out["inputs"] = capo_bedrock_agent.types.flow_node_inputs.deserialize_json(
            data["inputs"]
        )
    if data.get("outputs") is not None:
        import capo_bedrock_agent.types.flow_node_outputs

        out["outputs"] = capo_bedrock_agent.types.flow_node_outputs.deserialize_json(
            data["outputs"]
        )
    return out


def redact_sensitive(value: FlowNode) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_bedrock_agent.types.flow_node_configuration

        out["configuration"] = (
            capo_bedrock_agent.types.flow_node_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    if "inputs" in value:
        import capo_bedrock_agent.types.flow_node_inputs

        out["inputs"] = capo_bedrock_agent.types.flow_node_inputs.redact_sensitive(
            value["inputs"]
        )
    return out
