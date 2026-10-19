"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputNext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_node_input_name
    import capo_bedrock_agent_runtime.types.node_name


class FlowTraceNodeOutputNext(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the next node that receives the output data.</p>"""
    input_field_name: (
        "capo_bedrock_agent_runtime.types.flow_node_input_name.FlowNodeInputName"
    )
    """<p>The name of the input field in the next node that receives the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputNext) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    out["inputFieldName"] = value["input_field_name"]
    return out


def deserialize_json(data: dict) -> FlowTraceNodeOutputNext:
    out: FlowTraceNodeOutputNext = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        out["node_name"] = ""
    if data.get("inputFieldName") is not None:
        out["input_field_name"] = data["inputFieldName"]
    else:
        out["input_field_name"] = ""
    return out
