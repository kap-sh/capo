"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CalendarInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.calendar_interval_duration
    import capo_application_signals.types.duration_unit


class CalendarInterval(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The date and time when you want the first interval to start. Be sure to choose a time that configures the intervals the way that you want. For example, if you want weekly intervals starting on Mondays at 6 a.m., be sure to specify a start time that is a Monday at 6 a.m.</p> <p>When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>As soon as one calendar interval ends, another automatically begins.</p>"""
    duration_unit: "capo_application_signals.types.duration_unit.DurationUnit"
    """<p>Specifies the calendar interval unit.</p>"""
    duration: "capo_application_signals.types.calendar_interval_duration.CalendarIntervalDuration"
    """<p>Specifies the duration of each calendar interval. For example, if <code>Duration</code> is <code>1</code> and <code>DurationUnit</code> is <code>MONTH</code>, each interval is one month, aligned with the calendar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalendarInterval) -> dict:
    out: dict = {}
    import capo_application_signals.types._prelude.timestamp

    out["StartTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_application_signals.types.duration_unit

    out["DurationUnit"] = capo_application_signals.types.duration_unit.serialize_json(
        value["duration_unit"]
    )
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> CalendarInterval:
    out: CalendarInterval = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["start_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("DurationUnit") is not None:
        import capo_application_signals.types.duration_unit

        out["duration_unit"] = (
            capo_application_signals.types.duration_unit.deserialize_json(
                data["DurationUnit"]
            )
        )
    else:
        import typing

        out["duration_unit"] = typing.cast(
            "capo_application_signals.types.duration_unit.DurationUnit", ""
        )
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    return out
