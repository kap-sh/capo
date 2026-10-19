"""Generated from Smithy shape ``com.amazonaws.iot#MaintenanceWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.cron_expression
    import capo_iot.types.duration_in_minutes


class MaintenanceWindow(TypedDict, closed=True):
    start_time: "capo_iot.types.cron_expression.CronExpression"
    """<p>Displays the start time of the next maintenance window.</p>"""
    duration_in_minutes: "capo_iot.types.duration_in_minutes.DurationInMinutes"
    """<p>Displays the duration of the next maintenance window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceWindow) -> dict:
    out: dict = {}
    out["startTime"] = value["start_time"]
    out["durationInMinutes"] = value["duration_in_minutes"]
    return out


def deserialize_json(data: dict) -> MaintenanceWindow:
    out: MaintenanceWindow = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        out["start_time"] = data["startTime"]
    else:
        out["start_time"] = ""
    if data.get("durationInMinutes") is not None:
        out["duration_in_minutes"] = data["durationInMinutes"]
    else:
        out["duration_in_minutes"] = 0
    return out
