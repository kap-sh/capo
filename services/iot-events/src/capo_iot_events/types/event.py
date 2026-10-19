"""Generated from Smithy shape ``com.amazonaws.iotevents#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.actions
    import capo_iot_events.types.condition
    import capo_iot_events.types.event_name


class Event(TypedDict, closed=True):
    event_name: "capo_iot_events.types.event_name.EventName"
    """<p>The name of the event.</p>"""
    condition: NotRequired["capo_iot_events.types.condition.Condition"]
    """<p>Optional. The Boolean expression that, when TRUE, causes the <code>actions</code> to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).</p>"""
    actions: NotRequired["capo_iot_events.types.actions.Actions"]
    """<p>The actions to be performed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> dict:
    out: dict = {}
    out["eventName"] = value["event_name"]
    if "condition" in value:
        out["condition"] = value["condition"]
    if "actions" in value:
        import capo_iot_events.types.actions

        out["actions"] = capo_iot_events.types.actions.serialize_json(value["actions"])
    return out


def deserialize_json(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if data.get("eventName") is not None:
        out["event_name"] = data["eventName"]
    else:
        out["event_name"] = ""
    if data.get("condition") is not None:
        out["condition"] = data["condition"]
    if data.get("actions") is not None:
        import capo_iot_events.types.actions

        out["actions"] = capo_iot_events.types.actions.deserialize_json(data["actions"])
    return out
