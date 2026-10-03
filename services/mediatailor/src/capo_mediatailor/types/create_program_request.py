"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateProgramRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of_ad_break
    import capo_mediatailor.types.__list_of_audience_media
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.schedule_configuration


class CreateProgramRequest(TypedDict, closed=True):
    ad_breaks: NotRequired["capo_mediatailor.types.__list_of_ad_break.__listOfAdBreak"]
    """<p>The ad break configuration settings.</p>"""
    channel_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the channel for this Program.</p>"""
    live_source_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the LiveSource for this Program.</p>"""
    program_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the Program.</p>"""
    schedule_configuration: (
        "capo_mediatailor.types.schedule_configuration.ScheduleConfiguration"
    )
    """<p>The schedule configuration settings.</p>"""
    source_location_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the source location.</p>"""
    vod_source_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name that's used to refer to a VOD source.</p>"""
    audience_media: NotRequired[
        "capo_mediatailor.types.__list_of_audience_media.__listOfAudienceMedia"
    ]
    """<p>The list of AudienceMedia defined in program.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the program. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProgramRequest) -> dict:
    out: dict = {}
    if "ad_breaks" in value:
        import capo_mediatailor.types.__list_of_ad_break

        out["AdBreaks"] = capo_mediatailor.types.__list_of_ad_break.serialize_json(
            value["ad_breaks"]
        )
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    import capo_mediatailor.types.schedule_configuration

    out["ScheduleConfiguration"] = (
        capo_mediatailor.types.schedule_configuration.serialize_json(
            value["schedule_configuration"]
        )
    )
    out["SourceLocationName"] = value["source_location_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
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


def deserialize_json(data: dict) -> CreateProgramRequest:
    out: CreateProgramRequest = {}  # type: ignore[typeddict-item]
    if data.get("AdBreaks") is not None:
        import capo_mediatailor.types.__list_of_ad_break

        out["ad_breaks"] = capo_mediatailor.types.__list_of_ad_break.deserialize_json(
            data["AdBreaks"]
        )
    if data.get("LiveSourceName") is not None:
        out["live_source_name"] = data["LiveSourceName"]
    if data.get("ScheduleConfiguration") is not None:
        import capo_mediatailor.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_mediatailor.types.schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProgramRequest.schedule_configuration required"
        )
    if data.get("SourceLocationName") is not None:
        out["source_location_name"] = data["SourceLocationName"]
    else:
        raise DeserializationError("CreateProgramRequest.source_location_name required")
    if data.get("VodSourceName") is not None:
        out["vod_source_name"] = data["VodSourceName"]
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
