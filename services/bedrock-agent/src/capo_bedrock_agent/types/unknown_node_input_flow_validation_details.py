"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UnknownNodeInputFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_input_name
    import capo_bedrock_agent.types.flow_node_name


class UnknownNodeInputFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the unknown input.</p>"""
    input: "capo_bedrock_agent.types.flow_node_input_name.FlowNodeInputName"
    """<p>The name of the node with the unknown input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnknownNodeInputFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["input"] = value["input"]
    return out


def deserialize_json(data: dict) -> UnknownNodeInputFlowValidationDetails:
    out: UnknownNodeInputFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("node") is not None:
        out["node"] = data["node"]
    else:
        out["node"] = ""
    if data.get("input") is not None:
        out["input"] = data["input"]
    else:
        out["input"] = ""
    return out
