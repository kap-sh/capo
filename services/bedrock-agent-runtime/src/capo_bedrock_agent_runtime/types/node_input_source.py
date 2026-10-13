"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeInputSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_node_input_expression
    import capo_bedrock_agent_runtime.types.flow_node_output_name
    import capo_bedrock_agent_runtime.types.node_name


class NodeInputSource(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the source node that provides the input data.</p>"""
    output_field_name: (
        "capo_bedrock_agent_runtime.types.flow_node_output_name.FlowNodeOutputName"
    )
    """<p>The name of the output field from the source node.</p>"""
    expression: "capo_bedrock_agent_runtime.types.flow_node_input_expression.FlowNodeInputExpression"
    """<p>The expression used to extract data from the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInputSource) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    out["outputFieldName"] = value["output_field_name"]
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> NodeInputSource:
    out: NodeInputSource = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("NodeInputSource.node_name required")
    if data.get("outputFieldName") is not None:
        out["output_field_name"] = data["outputFieldName"]
    else:
        raise DeserializationError("NodeInputSource.output_field_name required")
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("NodeInputSource.expression required")
    return out


def redact_sensitive(value: NodeInputSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
