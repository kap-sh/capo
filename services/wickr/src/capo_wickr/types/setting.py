"""Generated from Smithy shape ``com.amazonaws.wickr#Setting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class Setting(TypedDict, closed=True):
    option_name: "capo_wickr.types.generic_string.GenericString"
    """<p>The name of the network setting (e.g., 'enableClientMetrics', 'dataRetention').</p>"""
    value: "capo_wickr.types.generic_string.GenericString"
    """<p>The current value of the setting as a string. Boolean values are represented as 'true' or 'false'.</p>"""
    type: "capo_wickr.types.generic_string.GenericString"
    """<p>The data type of the setting value (e.g., 'boolean', 'string', 'number').</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Setting) -> dict:
    out: dict = {}
    out["optionName"] = value["option_name"]
    out["value"] = value["value"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Setting:
    out: Setting = {}  # type: ignore[typeddict-item]
    if data.get("optionName") is not None:
        out["option_name"] = data["optionName"]
    else:
        out["option_name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
