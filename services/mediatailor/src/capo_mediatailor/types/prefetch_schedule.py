"""Generated from Smithy shape ``com.amazonaws.mediatailor#PrefetchSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.prefetch_consumption
    import capo_mediatailor.types.prefetch_retrieval
    import capo_mediatailor.types.prefetch_schedule_type
    import capo_mediatailor.types.recurring_prefetch_configuration


class PrefetchSchedule(TypedDict, closed=True):
    arn: "capo_mediatailor.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the prefetch schedule.</p>"""
    consumption: NotRequired[
        "capo_mediatailor.types.prefetch_consumption.PrefetchConsumption"
    ]
    """<p>Consumption settings determine how, and when, MediaTailor places the prefetched ads into ad breaks for single prefetch schedules. Ad consumption occurs within a span of time that you define, called a <i>consumption window</i>. You can designate which ad breaks that MediaTailor fills with prefetch ads by setting avail matching criteria.</p>"""
    name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.</p>"""
    playback_configuration_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the playback configuration to create the prefetch schedule for.</p>"""
    retrieval: NotRequired[
        "capo_mediatailor.types.prefetch_retrieval.PrefetchRetrieval"
    ]
    """<p>A complex type that contains settings for prefetch retrieval from the ad decision server (ADS).</p>"""
    schedule_type: NotRequired[
        "capo_mediatailor.types.prefetch_schedule_type.PrefetchScheduleType"
    ]
    """<p>The frequency that MediaTailor creates prefetch schedules. <code>SINGLE</code> indicates that this schedule applies to one ad break. <code>RECURRING</code> indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.</p> <p>For more information about the prefetch types and when you might use each, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Prefetching ads in Elemental MediaTailor.</a> </p>"""
    recurring_prefetch_configuration: NotRequired[
        "capo_mediatailor.types.recurring_prefetch_configuration.RecurringPrefetchConfiguration"
    ]
    """<p>The settings that determine how and when MediaTailor prefetches ads and inserts them into ad breaks.</p>"""
    stream_id: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>An optional stream identifier that you can specify in order to prefetch for multiple streams that use the same playback configuration.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags assigned to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrefetchSchedule) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "consumption" in value:
        import capo_mediatailor.types.prefetch_consumption

        out["Consumption"] = capo_mediatailor.types.prefetch_consumption.serialize_json(
            value["consumption"]
        )
    out["Name"] = value["name"]
    out["PlaybackConfigurationName"] = value["playback_configuration_name"]
    if "retrieval" in value:
        import capo_mediatailor.types.prefetch_retrieval

        out["Retrieval"] = capo_mediatailor.types.prefetch_retrieval.serialize_json(
            value["retrieval"]
        )
    if "schedule_type" in value:
        import capo_mediatailor.types.prefetch_schedule_type

        out["ScheduleType"] = (
            capo_mediatailor.types.prefetch_schedule_type.serialize_json(
                value["schedule_type"]
            )
        )
    if "recurring_prefetch_configuration" in value:
        import capo_mediatailor.types.recurring_prefetch_configuration

        out["RecurringPrefetchConfiguration"] = (
            capo_mediatailor.types.recurring_prefetch_configuration.serialize_json(
                value["recurring_prefetch_configuration"]
            )
        )
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> PrefetchSchedule:
    out: PrefetchSchedule = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("PrefetchSchedule.arn required")
    if data.get("Consumption") is not None:
        import capo_mediatailor.types.prefetch_consumption

        out["consumption"] = (
            capo_mediatailor.types.prefetch_consumption.deserialize_json(
                data["Consumption"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PrefetchSchedule.name required")
    if data.get("PlaybackConfigurationName") is not None:
        out["playback_configuration_name"] = data["PlaybackConfigurationName"]
    else:
        raise DeserializationError(
            "PrefetchSchedule.playback_configuration_name required"
        )
    if data.get("Retrieval") is not None:
        import capo_mediatailor.types.prefetch_retrieval

        out["retrieval"] = capo_mediatailor.types.prefetch_retrieval.deserialize_json(
            data["Retrieval"]
        )
    if data.get("ScheduleType") is not None:
        import capo_mediatailor.types.prefetch_schedule_type

        out["schedule_type"] = (
            capo_mediatailor.types.prefetch_schedule_type.deserialize_json(
                data["ScheduleType"]
            )
        )
    if data.get("RecurringPrefetchConfiguration") is not None:
        import capo_mediatailor.types.recurring_prefetch_configuration

        out["recurring_prefetch_configuration"] = (
            capo_mediatailor.types.recurring_prefetch_configuration.deserialize_json(
                data["RecurringPrefetchConfiguration"]
            )
        )
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
