"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteFlowAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_alias_id
    import capo_bedrock_agent.types.flow_id


class DeleteFlowAliasResponse(TypedDict, closed=True):
    flow_id: "capo_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow that the alias belongs to.</p>"""
    id: "capo_bedrock_agent.types.flow_alias_id.FlowAliasId"
    """<p>The unique identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowAliasResponse) -> dict:
    out: dict = {}
    out["flowId"] = value["flow_id"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeleteFlowAliasResponse:
    out: DeleteFlowAliasResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowId") is not None:
        out["flow_id"] = data["flowId"]
    else:
        out["flow_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
