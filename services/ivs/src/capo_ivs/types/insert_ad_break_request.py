"""Generated from Smithy shape ``com.amazonaws.ivs#InsertAdBreakRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.ad_duration_seconds
    import capo_ivs.types.channel_arn


class InsertAdBreakRequest(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel into which the ad break is inserted.</p>"""
    duration_seconds: "capo_ivs.types.ad_duration_seconds.AdDurationSeconds"
    """<p>Duration of the ad break, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsertAdBreakRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["durationSeconds"] = value["duration_seconds"]
    return out


def deserialize_json(data: dict) -> InsertAdBreakRequest:
    out: InsertAdBreakRequest = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        out["channel_arn"] = ""
    if data.get("durationSeconds") is not None:
        out["duration_seconds"] = data["durationSeconds"]
    else:
        out["duration_seconds"] = 0
    return out
