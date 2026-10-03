"""Generated from Smithy shape ``com.amazonaws.connect#PutUserStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.agent_status_id
    import capo_connect.types.instance_id
    import capo_connect.types.user_id


class PutUserStatusRequest(TypedDict, closed=True):
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    agent_status_id: "capo_connect.types.agent_status_id.AgentStatusId"
    """<p>The identifier of the agent status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutUserStatusRequest) -> dict:
    out: dict = {}
    out["AgentStatusId"] = value["agent_status_id"]
    return out


def deserialize_json(data: dict) -> PutUserStatusRequest:
    out: PutUserStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("AgentStatusId") is not None:
        out["agent_status_id"] = data["AgentStatusId"]
    else:
        raise DeserializationError("PutUserStatusRequest.agent_status_id required")
    return out
