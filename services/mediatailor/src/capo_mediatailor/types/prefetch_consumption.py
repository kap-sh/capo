"""Generated from Smithy shape ``com.amazonaws.mediatailor#PrefetchConsumption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of_avail_matching_criteria
    import capo_mediatailor.types.__timestamp_unix


class PrefetchConsumption(TypedDict, closed=True):
    avail_matching_criteria: NotRequired[
        "capo_mediatailor.types.__list_of_avail_matching_criteria.__listOfAvailMatchingCriteria"
    ]
    """<p>If you only want MediaTailor to insert prefetched ads into avails (ad breaks) that match specific dynamic variables, such as <code>scte.event_id</code>, set the avail matching criteria.</p>"""
    end_time: "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    """<p>The time when MediaTailor no longer considers the prefetched ads for use in an ad break. MediaTailor automatically deletes prefetch schedules no less than seven days after the end time. If you'd like to manually delete the prefetch schedule, you can call <code>DeletePrefetchSchedule</code>.</p>"""
    start_time: NotRequired["capo_mediatailor.types.__timestamp_unix.__timestampUnix"]
    """<p>The time when prefetched ads are considered for use in an ad break. If you don't specify <code>StartTime</code>, the prefetched ads are available after MediaTailor retrieves them from the ad decision server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrefetchConsumption) -> dict:
    out: dict = {}
    if "avail_matching_criteria" in value:
        import capo_mediatailor.types.__list_of_avail_matching_criteria

        out["AvailMatchingCriteria"] = (
            capo_mediatailor.types.__list_of_avail_matching_criteria.serialize_json(
                value["avail_matching_criteria"]
            )
        )
    import capo_mediatailor.types.__timestamp_unix

    out["EndTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
        value["end_time"]
    )
    if "start_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["StartTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
            value["start_time"]
        )
    return out


def deserialize_json(data: dict) -> PrefetchConsumption:
    out: PrefetchConsumption = {}  # type: ignore[typeddict-item]
    if data.get("AvailMatchingCriteria") is not None:
        import capo_mediatailor.types.__list_of_avail_matching_criteria

        out["avail_matching_criteria"] = (
            capo_mediatailor.types.__list_of_avail_matching_criteria.deserialize_json(
                data["AvailMatchingCriteria"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["end_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["EndTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("StartTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["start_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["StartTime"]
        )
    return out
