"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.agent_arn
    import capo_quicksight.types.agent_id
    import capo_quicksight.types.agent_name
    import capo_quicksight.types.agent_status


class CreateAgentResponse(TypedDict, closed=True):
    arn: "capo_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "capo_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    agent_status: "capo_quicksight.types.agent_status.AgentStatus"
    """<p>The status of the agent.</p>"""
    agent_name: "capo_quicksight.types.agent_name.AgentName"
    """<p>The name of the agent.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    import capo_quicksight.types.agent_status

    out["AgentStatus"] = capo_quicksight.types.agent_status.serialize_json(
        value["agent_status"]
    )
    out["AgentName"] = value["agent_name"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateAgentResponse:
    out: CreateAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("AgentId") is not None:
        out["agent_id"] = data["AgentId"]
    else:
        out["agent_id"] = ""
    if data.get("AgentStatus") is not None:
        import capo_quicksight.types.agent_status

        out["agent_status"] = capo_quicksight.types.agent_status.deserialize_json(
            data["AgentStatus"]
        )
    else:
        import typing

        out["agent_status"] = typing.cast(
            "capo_quicksight.types.agent_status.AgentStatus", ""
        )
    if data.get("AgentName") is not None:
        out["agent_name"] = data["AgentName"]
    else:
        out["agent_name"] = ""
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
