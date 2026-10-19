"""Generated from Smithy shape ``com.amazonaws.appmesh#MatchRange``."""

from typing_extensions import TypedDict


class MatchRange(TypedDict, closed=True):
    start: "int"
    """<p>The start of the range.</p>"""
    end: "int"
    """<p>The end of the range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchRange) -> dict:
    out: dict = {}
    out["start"] = value["start"]
    out["end"] = value["end"]
    return out


def deserialize_json(data: dict) -> MatchRange:
    out: MatchRange = {}  # type: ignore[typeddict-item]
    if data.get("start") is not None:
        out["start"] = data["start"]
    else:
        out["start"] = 0
    if data.get("end") is not None:
        out["end"] = data["end"]
    else:
        out["end"] = 0
    return out
