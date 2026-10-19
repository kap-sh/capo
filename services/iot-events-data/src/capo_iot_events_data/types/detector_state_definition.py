"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DetectorStateDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.state_name
    import capo_iot_events_data.types.timer_definitions
    import capo_iot_events_data.types.variable_definitions


class DetectorStateDefinition(TypedDict, closed=True):
    state_name: "capo_iot_events_data.types.state_name.StateName"
    """<p>The name of the new state of the detector (instance).</p>"""
    variables: "capo_iot_events_data.types.variable_definitions.VariableDefinitions"
    """<p>The new values of the detector's variables. Any variable whose value isn't specified is cleared.</p>"""
    timers: "capo_iot_events_data.types.timer_definitions.TimerDefinitions"
    """<p>The new values of the detector's timers. Any timer whose value isn't specified is cleared, and its timeout event won't occur.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorStateDefinition) -> dict:
    out: dict = {}
    out["stateName"] = value["state_name"]
    import capo_iot_events_data.types.variable_definitions

    out["variables"] = capo_iot_events_data.types.variable_definitions.serialize_json(
        value["variables"]
    )
    import capo_iot_events_data.types.timer_definitions

    out["timers"] = capo_iot_events_data.types.timer_definitions.serialize_json(
        value["timers"]
    )
    return out


def deserialize_json(data: dict) -> DetectorStateDefinition:
    out: DetectorStateDefinition = {}  # type: ignore[typeddict-item]
    if data.get("stateName") is not None:
        out["state_name"] = data["stateName"]
    else:
        out["state_name"] = ""
    if data.get("variables") is not None:
        import capo_iot_events_data.types.variable_definitions

        out["variables"] = (
            capo_iot_events_data.types.variable_definitions.deserialize_json(
                data["variables"]
            )
        )
    else:
        out["variables"] = []
    if data.get("timers") is not None:
        import capo_iot_events_data.types.timer_definitions

        out["timers"] = capo_iot_events_data.types.timer_definitions.deserialize_json(
            data["timers"]
        )
    else:
        out["timers"] = []
    return out
