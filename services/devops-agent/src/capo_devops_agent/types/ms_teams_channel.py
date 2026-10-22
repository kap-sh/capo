"""Generated from Smithy shape ``com.amazonaws.devopsagent#MSTeamsChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.ms_teams_channel_id


class MSTeamsChannel(TypedDict, closed=True):
    channel_name: "str"
    """<p>The name of the Microsoft Teams channel.</p>"""
    channel_id: "capo_devops_agent.types.ms_teams_channel_id.MSTeamsChannelId"
    """<p>The unique identifier of the Microsoft Teams channel, for example 19:abc123def456@thread.tacv2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MSTeamsChannel) -> dict:
    out: dict = {}
    out["channelName"] = value["channel_name"]
    out["channelId"] = value["channel_id"]
    return out


def deserialize_json(data: dict) -> MSTeamsChannel:
    out: MSTeamsChannel = {}  # type: ignore[typeddict-item]
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    else:
        out["channel_name"] = ""
    if data.get("channelId") is not None:
        out["channel_id"] = data["channelId"]
    else:
        out["channel_id"] = ""
    return out
