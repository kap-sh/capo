"""Generated from Smithy shape ``com.amazonaws.m2#FileBatchJobIdentifier``."""

from typing_extensions import NotRequired, TypedDict


class FileBatchJobIdentifier(TypedDict, closed=True):
    file_name: "str"
    """<p>The file name for the batch job identifier.</p>"""
    folder_path: NotRequired["str"]
    """<p>The relative path to the file name for the batch job identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileBatchJobIdentifier) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    if "folder_path" in value:
        out["folderPath"] = value["folder_path"]
    return out


def deserialize_json(data: dict) -> FileBatchJobIdentifier:
    out: FileBatchJobIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    if data.get("folderPath") is not None:
        out["folder_path"] = data["folderPath"]
    return out
