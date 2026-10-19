"""Generated from Smithy shape ``com.amazonaws.iotevents#SetVariableAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.variable_name
    import capo_iot_events.types.variable_value


class SetVariableAction(TypedDict, closed=True):
    variable_name: "capo_iot_events.types.variable_name.VariableName"
    """<p>The name of the variable.</p>"""
    value: "capo_iot_events.types.variable_value.VariableValue"
    """<p>The new value of the variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetVariableAction) -> dict:
    out: dict = {}
    out["variableName"] = value["variable_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SetVariableAction:
    out: SetVariableAction = {}  # type: ignore[typeddict-item]
    if data.get("variableName") is not None:
        out["variable_name"] = data["variableName"]
    else:
        out["variable_name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
