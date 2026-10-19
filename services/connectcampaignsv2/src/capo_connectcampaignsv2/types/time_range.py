"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.iso8601_time


class TimeRange(TypedDict, closed=True):
    start_time: "capo_connectcampaignsv2.types.iso8601_time.Iso8601Time"
    end_time: "capo_connectcampaignsv2.types.iso8601_time.Iso8601Time"


# --- restJson1 ser/de ---
def serialize_json(value: TimeRange) -> dict:
    out: dict = {}
    out["startTime"] = value["start_time"]
    out["endTime"] = value["end_time"]
    return out


def deserialize_json(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        out["start_time"] = data["startTime"]
    else:
        out["start_time"] = ""
    if data.get("endTime") is not None:
        out["end_time"] = data["endTime"]
    else:
        out["end_time"] = ""
    return out
