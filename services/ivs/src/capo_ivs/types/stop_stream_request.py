"""Generated from Smithy shape ``com.amazonaws.ivs#StopStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn


class StopStreamRequest(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel for which the stream is to be stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopStreamRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    return out


def deserialize_json(data: dict) -> StopStreamRequest:
    out: StopStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        out["channel_arn"] = ""
    return out
