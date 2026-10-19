"""Generated from Smithy shape ``com.amazonaws.mediaconnect#WindowMaintenanceSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class WindowMaintenanceSchedule(TypedDict, closed=True):
    start: "datetime.datetime"
    """<p>The start time of the maintenance window.</p>"""
    end: "datetime.datetime"
    """<p>The end time of the maintenance window.</p>"""
    scheduled_time: "datetime.datetime"
    """<p>The date and time when the maintenance window is scheduled to occur.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WindowMaintenanceSchedule) -> dict:
    out: dict = {}
    import capo_mediaconnect._protocol.serialize

    out["start"] = capo_mediaconnect._protocol.serialize.fmt_date_time(value["start"])
    import capo_mediaconnect._protocol.serialize

    out["end"] = capo_mediaconnect._protocol.serialize.fmt_date_time(value["end"])
    import capo_mediaconnect._protocol.serialize

    out["scheduledTime"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["scheduled_time"]
    )
    return out


def deserialize_json(data: dict) -> WindowMaintenanceSchedule:
    out: WindowMaintenanceSchedule = {}  # type: ignore[typeddict-item]
    if data.get("start") is not None:
        import datetime

        out["start"] = datetime.datetime.fromisoformat(
            data["start"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["start"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("end") is not None:
        import datetime

        out["end"] = datetime.datetime.fromisoformat(data["end"].replace("Z", "+00:00"))
    else:
        import datetime

        out["end"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("scheduledTime") is not None:
        import datetime

        out["scheduled_time"] = datetime.datetime.fromisoformat(
            data["scheduledTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["scheduled_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
