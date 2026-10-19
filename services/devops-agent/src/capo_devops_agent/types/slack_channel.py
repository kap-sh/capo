"""Generated from Smithy shape ``com.amazonaws.devopsagent#SlackChannel``."""

from typing_extensions import NotRequired, TypedDict


class SlackChannel(TypedDict, closed=True):
    channel_name: NotRequired["str"]
    """<p>Slack channel name</p>"""
    channel_id: "str"
    """<p>Slack channel ID</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackChannel) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["channelName"] = value["channel_name"]
    out["channelId"] = value["channel_id"]
    return out


def deserialize_json(data: dict) -> SlackChannel:
    out: SlackChannel = {}  # type: ignore[typeddict-item]
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    if data.get("channelId") is not None:
        out["channel_id"] = data["channelId"]
    else:
        out["channel_id"] = ""
    return out
