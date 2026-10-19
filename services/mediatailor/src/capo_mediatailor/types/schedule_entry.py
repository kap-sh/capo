"""Generated from Smithy shape ``com.amazonaws.mediatailor#ScheduleEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of_schedule_ad_break
    import capo_mediatailor.types.__long
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.audiences
    import capo_mediatailor.types.schedule_entry_type


class ScheduleEntry(TypedDict, closed=True):
    approximate_duration_seconds: NotRequired["capo_mediatailor.types.__long.__long"]
    """<p>The approximate duration of this program, in seconds.</p>"""
    approximate_start_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The approximate time that the program will start playing.</p>"""
    arn: "capo_mediatailor.types.__string.__string"
    """<p>The ARN of the program.</p>"""
    channel_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the channel that uses this schedule.</p>"""
    live_source_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the live source used for the program.</p>"""
    program_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the program.</p>"""
    schedule_ad_breaks: NotRequired[
        "capo_mediatailor.types.__list_of_schedule_ad_break.__listOfScheduleAdBreak"
    ]
    """<p>The schedule's ad break properties.</p>"""
    schedule_entry_type: NotRequired[
        "capo_mediatailor.types.schedule_entry_type.ScheduleEntryType"
    ]
    """<p>The type of schedule entry.</p>"""
    source_location_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the source location.</p>"""
    vod_source_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the VOD source.</p>"""
    audiences: NotRequired["capo_mediatailor.types.audiences.Audiences"]
    """<p>The list of audiences defined in ScheduleEntry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleEntry) -> dict:
    out: dict = {}
    if "approximate_duration_seconds" in value:
        out["ApproximateDurationSeconds"] = value["approximate_duration_seconds"]
    if "approximate_start_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["ApproximateStartTime"] = (
            capo_mediatailor.types.__timestamp_unix.serialize_json(
                value["approximate_start_time"]
            )
        )
    out["Arn"] = value["arn"]
    out["ChannelName"] = value["channel_name"]
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    out["ProgramName"] = value["program_name"]
    if "schedule_ad_breaks" in value:
        import capo_mediatailor.types.__list_of_schedule_ad_break

        out["ScheduleAdBreaks"] = (
            capo_mediatailor.types.__list_of_schedule_ad_break.serialize_json(
                value["schedule_ad_breaks"]
            )
        )
    if "schedule_entry_type" in value:
        import capo_mediatailor.types.schedule_entry_type

        out["ScheduleEntryType"] = (
            capo_mediatailor.types.schedule_entry_type.serialize_json(
                value["schedule_entry_type"]
            )
        )
    out["SourceLocationName"] = value["source_location_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
    if "audiences" in value:
        import capo_mediatailor.types.audiences

        out["Audiences"] = capo_mediatailor.types.audiences.serialize_json(
            value["audiences"]
        )
    return out


def deserialize_json(data: dict) -> ScheduleEntry:
    out: ScheduleEntry = {}  # type: ignore[typeddict-item]
    if data.get("ApproximateDurationSeconds") is not None:
        out["approximate_duration_seconds"] = data["ApproximateDurationSeconds"]
    if data.get("ApproximateStartTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["approximate_start_time"] = (
            capo_mediatailor.types.__timestamp_unix.deserialize_json(
                data["ApproximateStartTime"]
            )
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        out["channel_name"] = ""
    if data.get("LiveSourceName") is not None:
        out["live_source_name"] = data["LiveSourceName"]
    if data.get("ProgramName") is not None:
        out["program_name"] = data["ProgramName"]
    else:
        out["program_name"] = ""
    if data.get("ScheduleAdBreaks") is not None:
        import capo_mediatailor.types.__list_of_schedule_ad_break

        out["schedule_ad_breaks"] = (
            capo_mediatailor.types.__list_of_schedule_ad_break.deserialize_json(
                data["ScheduleAdBreaks"]
            )
        )
    if data.get("ScheduleEntryType") is not None:
        import capo_mediatailor.types.schedule_entry_type

        out["schedule_entry_type"] = (
            capo_mediatailor.types.schedule_entry_type.deserialize_json(
                data["ScheduleEntryType"]
            )
        )
    if data.get("SourceLocationName") is not None:
        out["source_location_name"] = data["SourceLocationName"]
    else:
        out["source_location_name"] = ""
    if data.get("VodSourceName") is not None:
        out["vod_source_name"] = data["VodSourceName"]
    if data.get("Audiences") is not None:
        import capo_mediatailor.types.audiences

        out["audiences"] = capo_mediatailor.types.audiences.deserialize_json(
            data["Audiences"]
        )
    return out
