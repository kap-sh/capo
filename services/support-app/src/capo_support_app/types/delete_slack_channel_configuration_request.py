"""Generated from Smithy shape ``com.amazonaws.supportapp#DeleteSlackChannelConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support_app.types.channel_id
    import capo_support_app.types.team_id


class DeleteSlackChannelConfigurationRequest(TypedDict, closed=True):
    team_id: "capo_support_app.types.team_id.teamId"
    """<p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>"""
    channel_id: "capo_support_app.types.channel_id.channelId"
    """<p>The channel ID in Slack. This ID identifies a channel within a Slack workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlackChannelConfigurationRequest) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    out["channelId"] = value["channel_id"]
    return out


def deserialize_json(data: dict) -> DeleteSlackChannelConfigurationRequest:
    out: DeleteSlackChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("teamId") is not None:
        out["team_id"] = data["teamId"]
    else:
        out["team_id"] = ""
    if data.get("channelId") is not None:
        out["channel_id"] = data["channelId"]
    else:
        out["channel_id"] = ""
    return out
