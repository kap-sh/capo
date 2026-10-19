"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Position``."""

from typing_extensions import TypedDict


class Position(TypedDict, closed=True):
    line: "int"
    """<p>The line of the position, starting from 1.</p>"""
    column: "int"
    """<p>The column of the position, starting from 0.</p>"""
    offset: "int"
    """<p>The offset within the policy that corresponds to the position, starting from 0.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Position) -> dict:
    out: dict = {}
    out["line"] = value["line"]
    out["column"] = value["column"]
    out["offset"] = value["offset"]
    return out


def deserialize_json(data: dict) -> Position:
    out: Position = {}  # type: ignore[typeddict-item]
    if data.get("line") is not None:
        out["line"] = data["line"]
    else:
        out["line"] = 0
    if data.get("column") is not None:
        out["column"] = data["column"]
    else:
        out["column"] = 0
    if data.get("offset") is not None:
        out["offset"] = data["offset"]
    else:
        out["offset"] = 0
    return out
