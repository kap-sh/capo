"""Generated from Smithy shape ``com.amazonaws.devopsagent#MSTeamsBidirectionalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.role_arn


class MSTeamsBidirectionalConfiguration(TypedDict, closed=True):
    role_arn: "capo_devops_agent.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the agent assumes to exchange messages with the Microsoft Teams team for this association.</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether bidirectional communication is enabled for this association. If you set this value to <code>true</code>, you can mention the agent in the configured Microsoft Teams channel and it responds in that channel. If you omit this parameter or set it to <code>false</code>, the agent only sends one-way notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MSTeamsBidirectionalConfiguration) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> MSTeamsBidirectionalConfiguration:
    out: MSTeamsBidirectionalConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    return out
