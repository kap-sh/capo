"""Generated from Smithy shape ``com.amazonaws.devopsagent#SlackBidirectionalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.role_arn


class SlackBidirectionalConfiguration(TypedDict, closed=True):
    role_arn: "capo_devops_agent.types.role_arn.RoleArn"
    """<p>IAM role ARN that AWS DevOps Agent assumes to exchange messages with your Slack workspace on behalf of this association.</p>"""
    enabled: NotRequired["bool"]
    """<p>Whether bidirectional communication is enabled for this association. When you set this value to true, you can mention the agent in a configured Slack channel and it responds in that channel. When you omit this value or set it to false, the agent ignores mentions and only sends notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackBidirectionalConfiguration) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> SlackBidirectionalConfiguration:
    out: SlackBidirectionalConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    return out
