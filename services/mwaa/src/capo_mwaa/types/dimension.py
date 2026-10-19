"""Generated from Smithy shape ``com.amazonaws.mwaa#Dimension``."""

from typing_extensions import TypedDict


class Dimension(TypedDict, closed=True):
    name: "str"
    """<p> <b>Internal only</b>. The name of the dimension.</p>"""
    value: "str"
    """<p> <b>Internal only</b>. The value of the dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dimension) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
