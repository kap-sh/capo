"""Generated from Smithy shape ``com.amazonaws.repostspace#CreateChannelOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.channel_id


class CreateChannelOutput(TypedDict, closed=True):
    channel_id: "capo_repostspace.types.channel_id.ChannelId"
    """<p>The unique ID of the private re:Post channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelOutput) -> dict:
    out: dict = {}
    out["channelId"] = value["channel_id"]
    return out


def deserialize_json(data: dict) -> CreateChannelOutput:
    out: CreateChannelOutput = {}  # type: ignore[typeddict-item]
    if data.get("channelId") is not None:
        out["channel_id"] = data["channelId"]
    else:
        out["channel_id"] = ""
    return out
