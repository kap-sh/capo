"""Generated from Smithy shape ``com.amazonaws.braket#TimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class TimePeriod(TypedDict, closed=True):
    start_at: "datetime.datetime"
    """<p>The start date and time for the spending limit period, in epoch seconds.</p>"""
    end_at: "datetime.datetime"
    """<p>The end date and time for the spending limit period, in epoch seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimePeriod) -> dict:
    out: dict = {}
    out["startAt"] = value["start_at"].timestamp()
    out["endAt"] = value["end_at"].timestamp()
    return out


def deserialize_json(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if data.get("startAt") is not None:
        import datetime

        out["start_at"] = datetime.datetime.fromtimestamp(
            float(data["startAt"]), tz=datetime.timezone.utc
        )
    else:
        import datetime

        out["start_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endAt") is not None:
        import datetime

        out["end_at"] = datetime.datetime.fromtimestamp(
            float(data["endAt"]), tz=datetime.timezone.utc
        )
    else:
        import datetime

        out["end_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
