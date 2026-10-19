"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowDataConnectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_input_name
    import capo_bedrock_agent.types.flow_node_output_name


class FlowDataConnectionConfiguration(TypedDict, closed=True):
    source_output: "capo_bedrock_agent.types.flow_node_output_name.FlowNodeOutputName"
    """<p>The name of the output in the source node that the connection begins from.</p>"""
    target_input: "capo_bedrock_agent.types.flow_node_input_name.FlowNodeInputName"
    """<p>The name of the input in the target node that the connection ends at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowDataConnectionConfiguration) -> dict:
    out: dict = {}
    out["sourceOutput"] = value["source_output"]
    out["targetInput"] = value["target_input"]
    return out


def deserialize_json(data: dict) -> FlowDataConnectionConfiguration:
    out: FlowDataConnectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceOutput") is not None:
        out["source_output"] = data["sourceOutput"]
    else:
        out["source_output"] = ""
    if data.get("targetInput") is not None:
        out["target_input"] = data["targetInput"]
    else:
        out["target_input"] = ""
    return out
