"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterValueNumberRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.string_parameter_value


class CommandParameterValueNumberRange(TypedDict, closed=True):
    min: "capo_iot.types.string_parameter_value.StringParameterValue"
    """<p>The minimum value of a numerical range of a command parameter value.</p>"""
    max: "capo_iot.types.string_parameter_value.StringParameterValue"
    """<p>The maximum value of a numerical range of a command parameter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterValueNumberRange) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> CommandParameterValueNumberRange:
    out: CommandParameterValueNumberRange = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = data["min"]
    else:
        out["min"] = ""
    if data.get("max") is not None:
        out["max"] = data["max"]
    else:
        out["max"] = ""
    return out
