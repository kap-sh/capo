"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DuplicateConnectionsFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_name


class DuplicateConnectionsFlowValidationDetails(TypedDict, closed=True):
    source: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the source node where the duplicate connection starts.</p>"""
    target: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the target node where the duplicate connection ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DuplicateConnectionsFlowValidationDetails) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["target"] = value["target"]
    return out


def deserialize_json(data: dict) -> DuplicateConnectionsFlowValidationDetails:
    out: DuplicateConnectionsFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("target") is not None:
        out["target"] = data["target"]
    else:
        out["target"] = ""
    return out
