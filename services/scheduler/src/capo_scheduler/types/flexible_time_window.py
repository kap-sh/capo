"""Generated from Smithy shape ``com.amazonaws.scheduler#FlexibleTimeWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.flexible_time_window_mode
    import capo_scheduler.types.maximum_window_in_minutes


class FlexibleTimeWindow(TypedDict, closed=True):
    mode: "capo_scheduler.types.flexible_time_window_mode.FlexibleTimeWindowMode"
    """<p>Determines whether the schedule is invoked within a flexible time window.</p>"""
    maximum_window_in_minutes: NotRequired[
        "capo_scheduler.types.maximum_window_in_minutes.MaximumWindowInMinutes"
    ]
    """<p>The maximum time window during which a schedule can be invoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlexibleTimeWindow) -> dict:
    out: dict = {}
    out["Mode"] = value["mode"]
    if "maximum_window_in_minutes" in value:
        out["MaximumWindowInMinutes"] = value["maximum_window_in_minutes"]
    return out


def deserialize_json(data: dict) -> FlexibleTimeWindow:
    out: FlexibleTimeWindow = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        out["mode"] = data["Mode"]
    else:
        out["mode"] = ""
    if data.get("MaximumWindowInMinutes") is not None:
        out["maximum_window_in_minutes"] = data["MaximumWindowInMinutes"]
    return out
