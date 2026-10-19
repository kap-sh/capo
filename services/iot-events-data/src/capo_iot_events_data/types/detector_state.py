"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DetectorState``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.state_name
    import capo_iot_events_data.types.timers
    import capo_iot_events_data.types.variables


class DetectorState(TypedDict, closed=True):
    state_name: "capo_iot_events_data.types.state_name.StateName"
    """<p>The name of the state.</p>"""
    variables: "capo_iot_events_data.types.variables.Variables"
    """<p>The current values of the detector's variables.</p>"""
    timers: "capo_iot_events_data.types.timers.Timers"
    """<p>The current state of the detector's timers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorState) -> dict:
    out: dict = {}
    out["stateName"] = value["state_name"]
    import capo_iot_events_data.types.variables

    out["variables"] = capo_iot_events_data.types.variables.serialize_json(
        value["variables"]
    )
    import capo_iot_events_data.types.timers

    out["timers"] = capo_iot_events_data.types.timers.serialize_json(value["timers"])
    return out


def deserialize_json(data: dict) -> DetectorState:
    out: DetectorState = {}  # type: ignore[typeddict-item]
    if data.get("stateName") is not None:
        out["state_name"] = data["stateName"]
    else:
        out["state_name"] = ""
    if data.get("variables") is not None:
        import capo_iot_events_data.types.variables

        out["variables"] = capo_iot_events_data.types.variables.deserialize_json(
            data["variables"]
        )
    else:
        out["variables"] = []
    if data.get("timers") is not None:
        import capo_iot_events_data.types.timers

        out["timers"] = capo_iot_events_data.types.timers.deserialize_json(
            data["timers"]
        )
    else:
        out["timers"] = []
    return out
