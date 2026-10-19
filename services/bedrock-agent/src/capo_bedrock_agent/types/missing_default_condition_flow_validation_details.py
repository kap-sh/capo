"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MissingDefaultConditionFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_name


class MissingDefaultConditionFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node missing the default condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingDefaultConditionFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    return out


def deserialize_json(data: dict) -> MissingDefaultConditionFlowValidationDetails:
    out: MissingDefaultConditionFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("node") is not None:
        out["node"] = data["node"]
    else:
        out["node"] = ""
    return out
