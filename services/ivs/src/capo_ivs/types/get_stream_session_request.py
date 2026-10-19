"""Generated from Smithy shape ``com.amazonaws.ivs#GetStreamSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn
    import capo_ivs.types.stream_id


class GetStreamSessionRequest(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel resource</p>"""
    stream_id: NotRequired["capo_ivs.types.stream_id.StreamId"]
    """<p>Unique identifier for a live or previously live stream in the specified channel. If no <code>streamId</code> is provided, this returns the most recent stream session for the channel, if it exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamSessionRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    return out


def deserialize_json(data: dict) -> GetStreamSessionRequest:
    out: GetStreamSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        out["channel_arn"] = ""
    if data.get("streamId") is not None:
        out["stream_id"] = data["streamId"]
    return out
