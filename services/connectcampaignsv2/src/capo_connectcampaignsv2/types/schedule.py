"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#Schedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.iso8601_duration
    import capo_connectcampaignsv2.types.time_stamp


class Schedule(TypedDict, closed=True):
    start_time: "capo_connectcampaignsv2.types.time_stamp.TimeStamp"
    end_time: "capo_connectcampaignsv2.types.time_stamp.TimeStamp"
    refresh_frequency: NotRequired[
        "capo_connectcampaignsv2.types.iso8601_duration.Iso8601Duration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Schedule) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.time_stamp

    out["startTime"] = capo_connectcampaignsv2.types.time_stamp.serialize_json(
        value["start_time"]
    )
    import capo_connectcampaignsv2.types.time_stamp

    out["endTime"] = capo_connectcampaignsv2.types.time_stamp.serialize_json(
        value["end_time"]
    )
    if "refresh_frequency" in value:
        out["refreshFrequency"] = value["refresh_frequency"]
    return out


def deserialize_json(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_connectcampaignsv2.types.time_stamp

        out["start_time"] = capo_connectcampaignsv2.types.time_stamp.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_connectcampaignsv2.types.time_stamp

        out["end_time"] = capo_connectcampaignsv2.types.time_stamp.deserialize_json(
            data["endTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("refreshFrequency") is not None:
        out["refresh_frequency"] = data["refreshFrequency"]
    return out
