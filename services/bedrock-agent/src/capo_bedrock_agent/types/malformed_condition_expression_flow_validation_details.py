"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MalformedConditionExpressionFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.error_message
    import capo_bedrock_agent.types.flow_condition_name
    import capo_bedrock_agent.types.flow_node_name


class MalformedConditionExpressionFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node containing the malformed condition expression.</p>"""
    condition: "capo_bedrock_agent.types.flow_condition_name.FlowConditionName"
    """<p>The name of the malformed condition.</p>"""
    cause: "capo_bedrock_agent.types.error_message.ErrorMessage"
    """<p>The error message describing why the condition expression is malformed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MalformedConditionExpressionFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["condition"] = value["condition"]
    out["cause"] = value["cause"]
    return out


def deserialize_json(data: dict) -> MalformedConditionExpressionFlowValidationDetails:
    out: MalformedConditionExpressionFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("node") is not None:
        out["node"] = data["node"]
    else:
        out["node"] = ""
    if data.get("condition") is not None:
        out["condition"] = data["condition"]
    else:
        out["condition"] = ""
    if data.get("cause") is not None:
        out["cause"] = data["cause"]
    else:
        out["cause"] = ""
    return out
