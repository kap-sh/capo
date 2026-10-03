"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateProgramResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of_ad_break
    import capo_mediatailor.types.__list_of_audience_media
    import capo_mediatailor.types.__long
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.clip_range


class CreateProgramResponse(TypedDict, closed=True):
    ad_breaks: NotRequired["capo_mediatailor.types.__list_of_ad_break.__listOfAdBreak"]
    """<p>The ad break configuration settings.</p>"""
    arn: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The ARN to assign to the program.</p>"""
    channel_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name to assign to the channel for this program.</p>"""
    creation_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The time the program was created.</p>"""
    live_source_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the LiveSource for this Program.</p>"""
    program_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name to assign to this program.</p>"""
    scheduled_start_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The scheduled start time for this Program.</p>"""
    source_location_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name to assign to the source location for this program.</p>"""
    vod_source_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name that's used to refer to a VOD source.</p>"""
    clip_range: NotRequired["capo_mediatailor.types.clip_range.ClipRange"]
    """<p>The clip range configuration settings.</p>"""
    duration_millis: NotRequired["capo_mediatailor.types.__long.__long"]
    """<p>The duration of the live program in milliseconds.</p>"""
    audience_media: NotRequired[
        "capo_mediatailor.types.__list_of_audience_media.__listOfAudienceMedia"
    ]
    """<p>The list of AudienceMedia defined in program.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags assigned to the program. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProgramResponse) -> dict:
    out: dict = {}
    if "ad_breaks" in value:
        import capo_mediatailor.types.__list_of_ad_break

        out["AdBreaks"] = capo_mediatailor.types.__list_of_ad_break.serialize_json(
            value["ad_breaks"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "creation_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["CreationTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    if "program_name" in value:
        out["ProgramName"] = value["program_name"]
    if "scheduled_start_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["ScheduledStartTime"] = (
            capo_mediatailor.types.__timestamp_unix.serialize_json(
                value["scheduled_start_time"]
            )
        )
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
    if "clip_range" in value:
        import capo_mediatailor.types.clip_range

        out["ClipRange"] = capo_mediatailor.types.clip_range.serialize_json(
            value["clip_range"]
        )
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    if "audience_media" in value:
        import capo_mediatailor.types.__list_of_audience_media

        out["AudienceMedia"] = (
            capo_mediatailor.types.__list_of_audience_media.serialize_json(
                value["audience_media"]
            )
        )
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateProgramResponse:
    out: CreateProgramResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdBreaks") is not None:
        import capo_mediatailor.types.__list_of_ad_break

        out["ad_breaks"] = capo_mediatailor.types.__list_of_ad_break.deserialize_json(
            data["AdBreaks"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    if data.get("CreationTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["creation_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["CreationTime"]
        )
    if data.get("LiveSourceName") is not None:
        out["live_source_name"] = data["LiveSourceName"]
    if data.get("ProgramName") is not None:
        out["program_name"] = data["ProgramName"]
    if data.get("ScheduledStartTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["scheduled_start_time"] = (
            capo_mediatailor.types.__timestamp_unix.deserialize_json(
                data["ScheduledStartTime"]
            )
        )
    if data.get("SourceLocationName") is not None:
        out["source_location_name"] = data["SourceLocationName"]
    if data.get("VodSourceName") is not None:
        out["vod_source_name"] = data["VodSourceName"]
    if data.get("ClipRange") is not None:
        import capo_mediatailor.types.clip_range

        out["clip_range"] = capo_mediatailor.types.clip_range.deserialize_json(
            data["ClipRange"]
        )
    if data.get("DurationMillis") is not None:
        out["duration_millis"] = data["DurationMillis"]
    if data.get("AudienceMedia") is not None:
        import capo_mediatailor.types.__list_of_audience_media

        out["audience_media"] = (
            capo_mediatailor.types.__list_of_audience_media.deserialize_json(
                data["AudienceMedia"]
            )
        )
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
