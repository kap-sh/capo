"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeFilePath``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string


class CodeFilePath(TypedDict, closed=True):
    file_name: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The name of the file the code vulnerability was found in.</p>"""
    file_path: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The file path to the code that a vulnerability was found in.</p>"""
    start_line: "int"
    """<p>The line number of the first line of code that a vulnerability was found in.</p>"""
    end_line: "int"
    """<p>The line number of the last line of code that a vulnerability was found in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeFilePath) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    out["filePath"] = value["file_path"]
    out["startLine"] = value["start_line"]
    out["endLine"] = value["end_line"]
    return out


def deserialize_json(data: dict) -> CodeFilePath:
    out: CodeFilePath = {}  # type: ignore[typeddict-item]
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    if data.get("startLine") is not None:
        out["start_line"] = data["startLine"]
    else:
        out["start_line"] = 0
    if data.get("endLine") is not None:
        out["end_line"] = data["endLine"]
    else:
        out["end_line"] = 0
    return out
