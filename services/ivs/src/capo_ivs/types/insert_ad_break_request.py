"""Generated from Smithy shape ``com.amazonaws.ivs#InsertAdBreakRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.ad_break_id
    import capo_ivs.types.ad_duration_seconds
    import capo_ivs.types.channel_arn
    import capo_ivs.types.time


class InsertAdBreakRequest(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel into which the ad break is inserted.</p>"""
    duration_seconds: "capo_ivs.types.ad_duration_seconds.AdDurationSeconds"
    """<p>Duration of the ad break, in seconds.</p>"""
    ad_break_id: NotRequired["capo_ivs.types.ad_break_id.AdBreakId"]
    """<p>Caller-specified unique identifier for the ad break to insert into the playlist.</p>"""
    target_start_at: NotRequired["capo_ivs.types.time.Time"]
    """<p>Target time at which the ad break starts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsertAdBreakRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["durationSeconds"] = value["duration_seconds"]
    if "ad_break_id" in value:
        out["adBreakId"] = value["ad_break_id"]
    if "target_start_at" in value:
        import capo_ivs.types.time

        out["targetStartAt"] = capo_ivs.types.time.serialize_json(
            value["target_start_at"]
        )
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
    if data.get("adBreakId") is not None:
        out["ad_break_id"] = data["adBreakId"]
    if data.get("targetStartAt") is not None:
        import capo_ivs.types.time

        out["target_start_at"] = capo_ivs.types.time.deserialize_json(
            data["targetStartAt"]
        )
    return out
