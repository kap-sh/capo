"""Generated from Smithy shape ``com.amazonaws.groundstation#ISO8601TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class ISO8601TimeRange(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>Start time in ISO 8601 format in Coordinated Universal Time (UTC).</p> <p>Example: <code>2026-11-15T10:28:48.000Z</code> </p>"""
    end_time: "datetime.datetime"
    """<p>End time in ISO 8601 format in Coordinated Universal Time (UTC).</p> <p>Example: <code>2024-01-15T12:00:00.000Z</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ISO8601TimeRange) -> dict:
    out: dict = {}
    import capo_groundstation._protocol.serialize

    out["startTime"] = capo_groundstation._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    import capo_groundstation._protocol.serialize

    out["endTime"] = capo_groundstation._protocol.serialize.fmt_date_time(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> ISO8601TimeRange:
    out: ISO8601TimeRange = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
