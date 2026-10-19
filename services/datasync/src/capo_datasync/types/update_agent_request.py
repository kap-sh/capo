"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn
    import capo_datasync.types.tag_value


class UpdateAgentRequest(TypedDict, closed=True):
    agent_arn: "capo_datasync.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent to update.</p>"""
    name: NotRequired["capo_datasync.types.tag_value.TagValue"]
    """<p>The name that you want to use to configure the agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAgentRequest) -> dict:
    out: dict = {}
    out["AgentArn"] = value["agent_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAgentRequest:
    out: UpdateAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AgentArn") is not None:
        out["agent_arn"] = data["AgentArn"]
    else:
        out["agent_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
