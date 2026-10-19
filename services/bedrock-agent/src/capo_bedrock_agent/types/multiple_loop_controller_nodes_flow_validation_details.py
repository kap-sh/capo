"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MultipleLoopControllerNodesFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_name


class MultipleLoopControllerNodesFlowValidationDetails(TypedDict, closed=True):
    loop_node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The DoWhile loop in a flow that contains multiple <code>LoopController</code> nodes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultipleLoopControllerNodesFlowValidationDetails) -> dict:
    out: dict = {}
    out["loopNode"] = value["loop_node"]
    return out


def deserialize_json(data: dict) -> MultipleLoopControllerNodesFlowValidationDetails:
    out: MultipleLoopControllerNodesFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("loopNode") is not None:
        out["loop_node"] = data["loopNode"]
    else:
        out["loop_node"] = ""
    return out
