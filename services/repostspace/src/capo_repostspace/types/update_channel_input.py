"""Generated from Smithy shape ``com.amazonaws.repostspace#UpdateChannelInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.channel_description
    import capo_repostspace.types.channel_id
    import capo_repostspace.types.channel_name
    import capo_repostspace.types.space_id


class UpdateChannelInput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    channel_id: "capo_repostspace.types.channel_id.ChannelId"
    """<p>The unique ID of the private re:Post channel.</p>"""
    channel_name: "capo_repostspace.types.channel_name.ChannelName"
    """<p>The name for the channel. This must be unique per private re:Post.</p>"""
    channel_description: NotRequired[
        "capo_repostspace.types.channel_description.ChannelDescription"
    ]
    """<p>A description for the channel. This is used only to help you identify this channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelInput) -> dict:
    out: dict = {}
    out["channelName"] = value["channel_name"]
    if "channel_description" in value:
        out["channelDescription"] = value["channel_description"]
    return out


def deserialize_json(data: dict) -> UpdateChannelInput:
    out: UpdateChannelInput = {}  # type: ignore[typeddict-item]
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    else:
        out["channel_name"] = ""
    if data.get("channelDescription") is not None:
        out["channel_description"] = data["channelDescription"]
    return out


def redact_sensitive(value: UpdateChannelInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_name" in value:
        out["channel_name"] = "*** Sensitive Data Redacted ***"
    if "channel_description" in value:
        out["channel_description"] = "*** Sensitive Data Redacted ***"
    return out
