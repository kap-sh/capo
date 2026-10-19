"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UnreachableNodeFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_name


class UnreachableNodeFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the unreachable node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnreachableNodeFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    return out


def deserialize_json(data: dict) -> UnreachableNodeFlowValidationDetails:
    out: UnreachableNodeFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("node") is not None:
        out["node"] = data["node"]
    else:
        out["node"] = ""
    return out
