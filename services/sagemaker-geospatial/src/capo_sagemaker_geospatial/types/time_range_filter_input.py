"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#TimeRangeFilterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class TimeRangeFilterInput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start time for the time-range filter.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time for the time-range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeFilterInput) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial.types._prelude.timestamp

    out["StartTime"] = (
        capo_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    )
    import capo_sagemaker_geospatial.types._prelude.timestamp

    out["EndTime"] = capo_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> TimeRangeFilterInput:
    out: TimeRangeFilterInput = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_sagemaker_geospatial.types._prelude.timestamp

        out["start_time"] = (
            capo_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_sagemaker_geospatial.types._prelude.timestamp

        out["end_time"] = (
            capo_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
