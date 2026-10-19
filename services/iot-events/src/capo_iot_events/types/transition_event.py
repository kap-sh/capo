"""Generated from Smithy shape ``com.amazonaws.iotevents#TransitionEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.actions
    import capo_iot_events.types.condition
    import capo_iot_events.types.event_name
    import capo_iot_events.types.state_name


class TransitionEvent(TypedDict, closed=True):
    event_name: "capo_iot_events.types.event_name.EventName"
    """<p>The name of the transition event.</p>"""
    condition: "capo_iot_events.types.condition.Condition"
    """<p>Required. A Boolean expression that when TRUE causes the actions to be performed and the <code>nextState</code> to be entered.</p>"""
    actions: NotRequired["capo_iot_events.types.actions.Actions"]
    """<p>The actions to be performed.</p>"""
    next_state: "capo_iot_events.types.state_name.StateName"
    """<p>The next state to enter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransitionEvent) -> dict:
    out: dict = {}
    out["eventName"] = value["event_name"]
    out["condition"] = value["condition"]
    if "actions" in value:
        import capo_iot_events.types.actions

        out["actions"] = capo_iot_events.types.actions.serialize_json(value["actions"])
    out["nextState"] = value["next_state"]
    return out


def deserialize_json(data: dict) -> TransitionEvent:
    out: TransitionEvent = {}  # type: ignore[typeddict-item]
    if data.get("eventName") is not None:
        out["event_name"] = data["eventName"]
    else:
        out["event_name"] = ""
    if data.get("condition") is not None:
        out["condition"] = data["condition"]
    else:
        out["condition"] = ""
    if data.get("actions") is not None:
        import capo_iot_events.types.actions

        out["actions"] = capo_iot_events.types.actions.deserialize_json(data["actions"])
    if data.get("nextState") is not None:
        out["next_state"] = data["nextState"]
    else:
        out["next_state"] = ""
    return out
