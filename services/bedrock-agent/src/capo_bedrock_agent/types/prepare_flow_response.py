"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PrepareFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_id
    import capo_bedrock_agent.types.flow_status


class PrepareFlowResponse(TypedDict, closed=True):
    id: "capo_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    status: "capo_bedrock_agent.types.flow_status.FlowStatus"
    """<p>The status of the flow. When you submit this request, the status will be <code>NotPrepared</code>. If preparation succeeds, the status becomes <code>Prepared</code>. If it fails, the status becomes <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrepareFlowResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_bedrock_agent.types.flow_status

    out["status"] = capo_bedrock_agent.types.flow_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> PrepareFlowResponse:
    out: PrepareFlowResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agent.types.flow_status

        out["status"] = capo_bedrock_agent.types.flow_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent.types.flow_status.FlowStatus", ""
        )
    return out
