"""Generated from Smithy shape ``com.amazonaws.ivs#GetStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn


class GetStreamRequest(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>Channel ARN for stream to be accessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    return out


def deserialize_json(data: dict) -> GetStreamRequest:
    out: GetStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        out["channel_arn"] = ""
    return out
