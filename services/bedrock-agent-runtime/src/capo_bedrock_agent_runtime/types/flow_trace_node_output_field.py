"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_node_io_data_type
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_content
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_next_list
    import capo_bedrock_agent_runtime.types.node_output_name


class FlowTraceNodeOutputField(TypedDict, closed=True):
    node_output_name: "capo_bedrock_agent_runtime.types.node_output_name.NodeOutputName"
    """<p>The name of the node output.</p>"""
    content: "capo_bedrock_agent_runtime.types.flow_trace_node_output_content.FlowTraceNodeOutputContent"
    """<p>The content of the node output.</p>"""
    next: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_trace_node_output_next_list.FlowTraceNodeOutputNextList"
    ]
    """<p>The next node that receives output data from this field.</p>"""
    type: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_node_io_data_type.FlowNodeIODataType"
    ]
    """<p>The data type of the output field for compatibility validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputField) -> dict:
    out: dict = {}
    out["nodeOutputName"] = value["node_output_name"]
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_content

    out["content"] = (
        capo_bedrock_agent_runtime.types.flow_trace_node_output_content.serialize_json(
            value["content"]
        )
    )
    if "next" in value:
        import capo_bedrock_agent_runtime.types.flow_trace_node_output_next_list

        out["next"] = (
            capo_bedrock_agent_runtime.types.flow_trace_node_output_next_list.serialize_json(
                value["next"]
            )
        )
    if "type" in value:
        import capo_bedrock_agent_runtime.types.flow_node_io_data_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.flow_node_io_data_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowTraceNodeOutputField:
    out: FlowTraceNodeOutputField = {}  # type: ignore[typeddict-item]
    if data.get("nodeOutputName") is not None:
        out["node_output_name"] = data["nodeOutputName"]
    else:
        out["node_output_name"] = ""
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_node_output_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.flow_trace_node_output_content.deserialize_json(
                data["content"]
            )
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("next") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_node_output_next_list

        out["next"] = (
            capo_bedrock_agent_runtime.types.flow_trace_node_output_next_list.deserialize_json(
                data["next"]
            )
        )
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.flow_node_io_data_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.flow_node_io_data_type.deserialize_json(
                data["type"]
            )
        )
    return out
