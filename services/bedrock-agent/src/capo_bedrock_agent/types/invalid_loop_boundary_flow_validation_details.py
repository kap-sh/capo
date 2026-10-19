"""Generated from Smithy shape ``com.amazonaws.bedrockagent#InvalidLoopBoundaryFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_connection_name
    import capo_bedrock_agent.types.flow_node_name


class InvalidLoopBoundaryFlowValidationDetails(TypedDict, closed=True):
    connection: "capo_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection that violates loop boundary rules.</p>"""
    source: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The source node of the connection that violates DoWhile loop boundary rules.</p>"""
    target: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The target node of the connection that violates DoWhile loop boundary rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidLoopBoundaryFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    out["source"] = value["source"]
    out["target"] = value["target"]
    return out


def deserialize_json(data: dict) -> InvalidLoopBoundaryFlowValidationDetails:
    out: InvalidLoopBoundaryFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("connection") is not None:
        out["connection"] = data["connection"]
    else:
        out["connection"] = ""
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("target") is not None:
        out["target"] = data["target"]
    else:
        out["target"] = ""
    return out
