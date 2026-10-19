"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Substring``."""

from typing_extensions import TypedDict


class Substring(TypedDict, closed=True):
    start: "int"
    """<p>The start index of the substring, starting from 0.</p>"""
    length: "int"
    """<p>The length of the substring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Substring) -> dict:
    out: dict = {}
    out["start"] = value["start"]
    out["length"] = value["length"]
    return out


def deserialize_json(data: dict) -> Substring:
    out: Substring = {}  # type: ignore[typeddict-item]
    if data.get("start") is not None:
        out["start"] = data["start"]
    else:
        out["start"] = 0
    if data.get("length") is not None:
        out["length"] = data["length"]
    else:
        out["length"] = 0
    return out
