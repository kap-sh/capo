"""Generated from Smithy shape ``com.amazonaws.datasync#DeleteAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn


class DeleteAgentRequest(TypedDict, closed=True):
    agent_arn: "capo_datasync.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent to delete. Use the <code>ListAgents</code> operation to return a list of agents for your account and Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAgentRequest) -> dict:
    out: dict = {}
    out["AgentArn"] = value["agent_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAgentRequest:
    out: DeleteAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AgentArn") is not None:
        out["agent_arn"] = data["AgentArn"]
    else:
        out["agent_arn"] = ""
    return out
