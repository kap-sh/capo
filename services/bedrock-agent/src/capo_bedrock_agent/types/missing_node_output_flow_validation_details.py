"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MissingNodeOutputFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_name
    import capo_bedrock_agent.types.flow_node_output_name


class MissingNodeOutputFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node missing the required output.</p>"""
    output: "capo_bedrock_agent.types.flow_node_output_name.FlowNodeOutputName"
    """<p>The name of the missing output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingNodeOutputFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["output"] = value["output"]
    return out


def deserialize_json(data: dict) -> MissingNodeOutputFlowValidationDetails:
    out: MissingNodeOutputFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("node") is not None:
        out["node"] = data["node"]
    else:
        out["node"] = ""
    if data.get("output") is not None:
        out["output"] = data["output"]
    else:
        out["output"] = ""
    return out
