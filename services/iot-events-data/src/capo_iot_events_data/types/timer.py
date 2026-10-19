"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#Timer``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.timer_name
    import capo_iot_events_data.types.timestamp


class Timer(TypedDict, closed=True):
    name: "capo_iot_events_data.types.timer_name.TimerName"
    """<p>The name of the timer.</p>"""
    timestamp: "capo_iot_events_data.types.timestamp.Timestamp"
    """<p>The expiration time for the timer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Timer) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_iot_events_data.types.timestamp

    out["timestamp"] = capo_iot_events_data.types.timestamp.serialize_json(
        value["timestamp"]
    )
    return out


def deserialize_json(data: dict) -> Timer:
    out: Timer = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("timestamp") is not None:
        import capo_iot_events_data.types.timestamp

        out["timestamp"] = capo_iot_events_data.types.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
