"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.state_name
    import capo_iot_events.types.states


class DetectorModelDefinition(TypedDict, closed=True):
    states: "capo_iot_events.types.states.States"
    """<p>Information about the states of the detector.</p>"""
    initial_state_name: "capo_iot_events.types.state_name.StateName"
    """<p>The state that is entered at the creation of each detector (instance).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorModelDefinition) -> dict:
    out: dict = {}
    import capo_iot_events.types.states

    out["states"] = capo_iot_events.types.states.serialize_json(value["states"])
    out["initialStateName"] = value["initial_state_name"]
    return out


def deserialize_json(data: dict) -> DetectorModelDefinition:
    out: DetectorModelDefinition = {}  # type: ignore[typeddict-item]
    if data.get("states") is not None:
        import capo_iot_events.types.states

        out["states"] = capo_iot_events.types.states.deserialize_json(data["states"])
    else:
        out["states"] = []
    if data.get("initialStateName") is not None:
        out["initial_state_name"] = data["initialStateName"]
    else:
        out["initial_state_name"] = ""
    return out
