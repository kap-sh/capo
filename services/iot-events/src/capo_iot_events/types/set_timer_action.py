"""Generated from Smithy shape ``com.amazonaws.iotevents#SetTimerAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.seconds
    import capo_iot_events.types.timer_name
    import capo_iot_events.types.variable_value


class SetTimerAction(TypedDict, closed=True):
    timer_name: "capo_iot_events.types.timer_name.TimerName"
    """<p>The name of the timer.</p>"""
    seconds: NotRequired["capo_iot_events.types.seconds.Seconds"]
    """<p>The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds. </p>"""
    duration_expression: NotRequired[
        "capo_iot_events.types.variable_value.VariableValue"
    ]
    """<p>The duration of the timer, in seconds. You can use a string expression that includes numbers, variables (<code>$variable.<variable-name></code>), and input values (<code>$input.<input-name>.<path-to-datum></code>) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetTimerAction) -> dict:
    out: dict = {}
    out["timerName"] = value["timer_name"]
    if "seconds" in value:
        out["seconds"] = value["seconds"]
    if "duration_expression" in value:
        out["durationExpression"] = value["duration_expression"]
    return out


def deserialize_json(data: dict) -> SetTimerAction:
    out: SetTimerAction = {}  # type: ignore[typeddict-item]
    if data.get("timerName") is not None:
        out["timer_name"] = data["timerName"]
    else:
        out["timer_name"] = ""
    if data.get("seconds") is not None:
        out["seconds"] = data["seconds"]
    if data.get("durationExpression") is not None:
        out["duration_expression"] = data["durationExpression"]
    return out
