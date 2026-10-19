"""Generated from Smithy shape ``com.amazonaws.iotevents#ClearTimerAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.timer_name


class ClearTimerAction(TypedDict, closed=True):
    timer_name: "capo_iot_events.types.timer_name.TimerName"
    """<p>The name of the timer to clear.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClearTimerAction) -> dict:
    out: dict = {}
    out["timerName"] = value["timer_name"]
    return out


def deserialize_json(data: dict) -> ClearTimerAction:
    out: ClearTimerAction = {}  # type: ignore[typeddict-item]
    if data.get("timerName") is not None:
        out["timer_name"] = data["timerName"]
    else:
        out["timer_name"] = ""
    return out
