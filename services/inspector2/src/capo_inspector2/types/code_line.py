"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeLine``."""

from typing_extensions import TypedDict


class CodeLine(TypedDict, closed=True):
    content: "str"
    """<p>The content of a line of code</p>"""
    line_number: "int"
    """<p>The line number that a section of code is located at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeLine) -> dict:
    out: dict = {}
    out["content"] = value["content"]
    out["lineNumber"] = value["line_number"]
    return out


def deserialize_json(data: dict) -> CodeLine:
    out: CodeLine = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    if data.get("lineNumber") is not None:
        out["line_number"] = data["lineNumber"]
    else:
        out["line_number"] = 0
    return out
