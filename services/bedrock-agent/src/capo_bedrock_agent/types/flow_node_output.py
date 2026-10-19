"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_io_data_type
    import capo_bedrock_agent.types.flow_node_output_name


class FlowNodeOutput(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.flow_node_output_name.FlowNodeOutputName"
    """<p>A name for the output that you can reference.</p>"""
    type: "capo_bedrock_agent.types.flow_node_io_data_type.FlowNodeIODataType"
    """<p>The data type of the output. If the output doesn't match this type at runtime, a validation error will be thrown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodeOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agent.types.flow_node_io_data_type

    out["type"] = capo_bedrock_agent.types.flow_node_io_data_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> FlowNodeOutput:
    out: FlowNodeOutput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_bedrock_agent.types.flow_node_io_data_type

        out["type"] = capo_bedrock_agent.types.flow_node_io_data_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.flow_node_io_data_type.FlowNodeIODataType", ""
        )
    return out
