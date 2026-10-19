"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MalformedNodeInputExpressionFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.error_message
    import capo_bedrock_agent.types.flow_node_input_name
    import capo_bedrock_agent.types.flow_node_name


class MalformedNodeInputExpressionFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node containing the malformed input expression.</p>"""
    input: "capo_bedrock_agent.types.flow_node_input_name.FlowNodeInputName"
    """<p>The name of the input with the malformed expression.</p>"""
    cause: "capo_bedrock_agent.types.error_message.ErrorMessage"
    """<p>The error message describing why the input expression is malformed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MalformedNodeInputExpressionFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["input"] = value["input"]
    out["cause"] = value["cause"]
    return out


def deserialize_json(data: dict) -> MalformedNodeInputExpressionFlowValidationDetails:
    out: MalformedNodeInputExpressionFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("node") is not None:
        out["node"] = data["node"]
    else:
        out["node"] = ""
    if data.get("input") is not None:
        out["input"] = data["input"]
    else:
        out["input"] = ""
    if data.get("cause") is not None:
        out["cause"] = data["cause"]
    else:
        out["cause"] = ""
    return out
