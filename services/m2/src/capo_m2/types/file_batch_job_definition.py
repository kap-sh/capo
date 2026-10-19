"""Generated from Smithy shape ``com.amazonaws.m2#FileBatchJobDefinition``."""

from typing_extensions import NotRequired, TypedDict


class FileBatchJobDefinition(TypedDict, closed=True):
    file_name: "str"
    """<p>The name of the file containing the batch job definition.</p>"""
    folder_path: NotRequired["str"]
    """<p>The path to the file containing the batch job definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileBatchJobDefinition) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    if "folder_path" in value:
        out["folderPath"] = value["folder_path"]
    return out


def deserialize_json(data: dict) -> FileBatchJobDefinition:
    out: FileBatchJobDefinition = {}  # type: ignore[typeddict-item]
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    if data.get("folderPath") is not None:
        out["folder_path"] = data["folderPath"]
    return out
