"""Generated from Smithy shape ``com.amazonaws.iotevents#State``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.on_enter_lifecycle
    import capo_iot_events.types.on_exit_lifecycle
    import capo_iot_events.types.on_input_lifecycle
    import capo_iot_events.types.state_name


class State(TypedDict, closed=True):
    state_name: "capo_iot_events.types.state_name.StateName"
    """<p>The name of the state.</p>"""
    on_input: NotRequired["capo_iot_events.types.on_input_lifecycle.OnInputLifecycle"]
    """<p>When an input is received and the <code>condition</code> is TRUE, perform the specified <code>actions</code>.</p>"""
    on_enter: NotRequired["capo_iot_events.types.on_enter_lifecycle.OnEnterLifecycle"]
    """<p>When entering this state, perform these <code>actions</code> if the <code>condition</code> is TRUE.</p>"""
    on_exit: NotRequired["capo_iot_events.types.on_exit_lifecycle.OnExitLifecycle"]
    """<p>When exiting this state, perform these <code>actions</code> if the specified <code>condition</code> is <code>TRUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: State) -> dict:
    out: dict = {}
    out["stateName"] = value["state_name"]
    if "on_input" in value:
        import capo_iot_events.types.on_input_lifecycle

        out["onInput"] = capo_iot_events.types.on_input_lifecycle.serialize_json(
            value["on_input"]
        )
    if "on_enter" in value:
        import capo_iot_events.types.on_enter_lifecycle

        out["onEnter"] = capo_iot_events.types.on_enter_lifecycle.serialize_json(
            value["on_enter"]
        )
    if "on_exit" in value:
        import capo_iot_events.types.on_exit_lifecycle

        out["onExit"] = capo_iot_events.types.on_exit_lifecycle.serialize_json(
            value["on_exit"]
        )
    return out


def deserialize_json(data: dict) -> State:
    out: State = {}  # type: ignore[typeddict-item]
    if data.get("stateName") is not None:
        out["state_name"] = data["stateName"]
    else:
        out["state_name"] = ""
    if data.get("onInput") is not None:
        import capo_iot_events.types.on_input_lifecycle

        out["on_input"] = capo_iot_events.types.on_input_lifecycle.deserialize_json(
            data["onInput"]
        )
    if data.get("onEnter") is not None:
        import capo_iot_events.types.on_enter_lifecycle

        out["on_enter"] = capo_iot_events.types.on_enter_lifecycle.deserialize_json(
            data["onEnter"]
        )
    if data.get("onExit") is not None:
        import capo_iot_events.types.on_exit_lifecycle

        out["on_exit"] = capo_iot_events.types.on_exit_lifecycle.deserialize_json(
            data["onExit"]
        )
    return out
