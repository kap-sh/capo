"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#TimeRangeFilterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class TimeRangeFilterOutput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The starting time for the time range filter.</p>"""
    end_time: "datetime.datetime"
    """<p>The ending time for the time range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeFilterOutput) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial._protocol.serialize

    out["StartTime"] = capo_sagemaker_geospatial._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    import capo_sagemaker_geospatial._protocol.serialize

    out["EndTime"] = capo_sagemaker_geospatial._protocol.serialize.fmt_date_time(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> TimeRangeFilterOutput:
    out: TimeRangeFilterOutput = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["StartTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["EndTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
