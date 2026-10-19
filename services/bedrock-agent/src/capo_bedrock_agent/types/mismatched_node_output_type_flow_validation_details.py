"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MismatchedNodeOutputTypeFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_io_data_type
    import capo_bedrock_agent.types.flow_node_name
    import capo_bedrock_agent.types.flow_node_output_name


class MismatchedNodeOutputTypeFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node containing the output with the mismatched data type.</p>"""
    output: "capo_bedrock_agent.types.flow_node_output_name.FlowNodeOutputName"
    """<p>The name of the output with the mismatched data type.</p>"""
    expected_type: "capo_bedrock_agent.types.flow_node_io_data_type.FlowNodeIODataType"
    """<p>The expected data type for the node output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MismatchedNodeOutputTypeFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["output"] = value["output"]
    import capo_bedrock_agent.types.flow_node_io_data_type

    out["expectedType"] = (
        capo_bedrock_agent.types.flow_node_io_data_type.serialize_json(
            value["expected_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> MismatchedNodeOutputTypeFlowValidationDetails:
    out: MismatchedNodeOutputTypeFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("node") is not None:
        out["node"] = data["node"]
    else:
        out["node"] = ""
    if data.get("output") is not None:
        out["output"] = data["output"]
    else:
        out["output"] = ""
    if data.get("expectedType") is not None:
        import capo_bedrock_agent.types.flow_node_io_data_type

        out["expected_type"] = (
            capo_bedrock_agent.types.flow_node_io_data_type.deserialize_json(
                data["expectedType"]
            )
        )
    else:
        import typing

        out["expected_type"] = typing.cast(
            "capo_bedrock_agent.types.flow_node_io_data_type.FlowNodeIODataType", ""
        )
    return out
