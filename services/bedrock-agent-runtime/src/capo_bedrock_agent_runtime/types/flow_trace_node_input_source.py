"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_node_input_expression
    import capo_bedrock_agent_runtime.types.flow_node_output_name
    import capo_bedrock_agent_runtime.types.node_name


class FlowTraceNodeInputSource(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the source node that provides the input data.</p>"""
    output_field_name: (
        "capo_bedrock_agent_runtime.types.flow_node_output_name.FlowNodeOutputName"
    )
    """<p>The name of the output field from the source node.</p>"""
    expression: "capo_bedrock_agent_runtime.types.flow_node_input_expression.FlowNodeInputExpression"
    """<p>The expression used to extract data from the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputSource) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    out["outputFieldName"] = value["output_field_name"]
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> FlowTraceNodeInputSource:
    out: FlowTraceNodeInputSource = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        out["node_name"] = ""
    if data.get("outputFieldName") is not None:
        out["output_field_name"] = data["outputFieldName"]
    else:
        out["output_field_name"] = ""
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    return out
