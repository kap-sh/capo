"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeLocation``."""

from typing_extensions import NotRequired, TypedDict


class CodeLocation(TypedDict, closed=True):
    file_path: "str"
    """<p>The absolute path to the file containing the code location.</p>"""
    line_start: NotRequired["int"]
    """<p>The starting line number of the code location.</p>"""
    line_end: NotRequired["int"]
    """<p>The ending line number of the code location.</p>"""
    label: NotRequired["str"]
    """<p>The role of this location in the vulnerability, such as source or sink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeLocation) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    if "line_start" in value:
        out["lineStart"] = value["line_start"]
    if "line_end" in value:
        out["lineEnd"] = value["line_end"]
    if "label" in value:
        out["label"] = value["label"]
    return out


def deserialize_json(data: dict) -> CodeLocation:
    out: CodeLocation = {}  # type: ignore[typeddict-item]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    if data.get("lineStart") is not None:
        out["line_start"] = data["lineStart"]
    if data.get("lineEnd") is not None:
        out["line_end"] = data["lineEnd"]
    if data.get("label") is not None:
        out["label"] = data["label"]
    return out
