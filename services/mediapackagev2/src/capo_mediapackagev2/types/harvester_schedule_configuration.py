"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvesterScheduleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class HarvesterScheduleConfiguration(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start time for the harvest job.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time for the harvest job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarvesterScheduleConfiguration) -> dict:
    out: dict = {}
    import capo_mediapackagev2.types._prelude.timestamp

    out["StartTime"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_mediapackagev2.types._prelude.timestamp

    out["EndTime"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> HarvesterScheduleConfiguration:
    out: HarvesterScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["start_time"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["end_time"] = capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
            data["EndTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
