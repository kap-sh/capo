"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_node_input_category
    import capo_bedrock_agent_runtime.types.flow_node_io_data_type
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_content
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_source
    import capo_bedrock_agent_runtime.types.node_input_name


class FlowTraceNodeInputField(TypedDict, closed=True):
    node_input_name: "capo_bedrock_agent_runtime.types.node_input_name.NodeInputName"
    """<p>The name of the node input.</p>"""
    content: "capo_bedrock_agent_runtime.types.flow_trace_node_input_content.FlowTraceNodeInputContent"
    """<p>The content of the node input.</p>"""
    source: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_trace_node_input_source.FlowTraceNodeInputSource"
    ]
    """<p>The source node that provides input data to this field.</p>"""
    type: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_node_io_data_type.FlowNodeIODataType"
    ]
    """<p>The data type of the input field for compatibility validation.</p>"""
    category: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_node_input_category.FlowNodeInputCategory"
    ]
    """<p>The category of the input field.</p>"""
    execution_chain: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain.FlowTraceNodeInputExecutionChain"
    ]
    """<p>The execution path through nested nodes like iterators and loops.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputField) -> dict:
    out: dict = {}
    out["nodeInputName"] = value["node_input_name"]
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_content

    out["content"] = (
        capo_bedrock_agent_runtime.types.flow_trace_node_input_content.serialize_json(
            value["content"]
        )
    )
    if "source" in value:
        import capo_bedrock_agent_runtime.types.flow_trace_node_input_source

        out["source"] = (
            capo_bedrock_agent_runtime.types.flow_trace_node_input_source.serialize_json(
                value["source"]
            )
        )
    if "type" in value:
        import capo_bedrock_agent_runtime.types.flow_node_io_data_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.flow_node_io_data_type.serialize_json(
                value["type"]
            )
        )
    if "category" in value:
        import capo_bedrock_agent_runtime.types.flow_node_input_category

        out["category"] = (
            capo_bedrock_agent_runtime.types.flow_node_input_category.serialize_json(
                value["category"]
            )
        )
    if "execution_chain" in value:
        import capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain

        out["executionChain"] = (
            capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain.serialize_json(
                value["execution_chain"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowTraceNodeInputField:
    out: FlowTraceNodeInputField = {}  # type: ignore[typeddict-item]
    if data.get("nodeInputName") is not None:
        out["node_input_name"] = data["nodeInputName"]
    else:
        out["node_input_name"] = ""
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_node_input_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.flow_trace_node_input_content.deserialize_json(
                data["content"]
            )
        )
    else:
        import capo_bedrock_agent_runtime.types._unknown

        out["content"] = capo_bedrock_agent_runtime.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("source") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_node_input_source

        out["source"] = (
            capo_bedrock_agent_runtime.types.flow_trace_node_input_source.deserialize_json(
                data["source"]
            )
        )
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.flow_node_io_data_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.flow_node_io_data_type.deserialize_json(
                data["type"]
            )
        )
    if data.get("category") is not None:
        import capo_bedrock_agent_runtime.types.flow_node_input_category

        out["category"] = (
            capo_bedrock_agent_runtime.types.flow_node_input_category.deserialize_json(
                data["category"]
            )
        )
    if data.get("executionChain") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain

        out["execution_chain"] = (
            capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain.deserialize_json(
                data["executionChain"]
            )
        )
    return out
