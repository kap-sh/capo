"""Generated from Smithy shape ``com.amazonaws.connect#DescribeAgentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_status_id
    import capo_connect.types.instance_id


class DescribeAgentStatusRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    agent_status_id: "capo_connect.types.agent_status_id.AgentStatusId"
    """<p>The identifier for the agent status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAgentStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAgentStatusRequest:
    out: DescribeAgentStatusRequest = {}  # type: ignore[typeddict-item]
    return out
