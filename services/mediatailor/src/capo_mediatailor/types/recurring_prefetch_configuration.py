"""Generated from Smithy shape ``com.amazonaws.mediatailor#RecurringPrefetchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.recurring_consumption
    import capo_mediatailor.types.recurring_retrieval


class RecurringPrefetchConfiguration(TypedDict, closed=True):
    start_time: NotRequired["capo_mediatailor.types.__timestamp_unix.__timestampUnix"]
    """<p>The start time for the window that MediaTailor prefetches and inserts ads in a live event. </p>"""
    end_time: "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    """<p>The end time for the window that MediaTailor prefetches and inserts ads in a live event. </p>"""
    recurring_consumption: (
        "capo_mediatailor.types.recurring_consumption.RecurringConsumption"
    )
    """<p>The settings that determine how and when MediaTailor places prefetched ads into upcoming ad breaks for recurring prefetch scedules.</p>"""
    recurring_retrieval: "capo_mediatailor.types.recurring_retrieval.RecurringRetrieval"
    """<p>The configuration for prefetch ad retrieval from the ADS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecurringPrefetchConfiguration) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["StartTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
            value["start_time"]
        )
    import capo_mediatailor.types.__timestamp_unix

    out["EndTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
        value["end_time"]
    )
    import capo_mediatailor.types.recurring_consumption

    out["RecurringConsumption"] = (
        capo_mediatailor.types.recurring_consumption.serialize_json(
            value["recurring_consumption"]
        )
    )
    import capo_mediatailor.types.recurring_retrieval

    out["RecurringRetrieval"] = (
        capo_mediatailor.types.recurring_retrieval.serialize_json(
            value["recurring_retrieval"]
        )
    )
    return out


def deserialize_json(data: dict) -> RecurringPrefetchConfiguration:
    out: RecurringPrefetchConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["start_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["end_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["EndTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("RecurringConsumption") is not None:
        import capo_mediatailor.types.recurring_consumption

        out["recurring_consumption"] = (
            capo_mediatailor.types.recurring_consumption.deserialize_json(
                data["RecurringConsumption"]
            )
        )
    else:
        raise DeserializationError(
            "RecurringPrefetchConfiguration.recurring_consumption required"
        )
    if data.get("RecurringRetrieval") is not None:
        import capo_mediatailor.types.recurring_retrieval

        out["recurring_retrieval"] = (
            capo_mediatailor.types.recurring_retrieval.deserialize_json(
                data["RecurringRetrieval"]
            )
        )
    else:
        raise DeserializationError(
            "RecurringPrefetchConfiguration.recurring_retrieval required"
        )
    return out
