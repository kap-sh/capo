"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookExportError``."""

from typing_extensions import TypedDict


class NotebookExportError(TypedDict, closed=True):
    message: "str"
    """<p>The error message. The maximum length is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotebookExportError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotebookExportError:
    out: NotebookExportError = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
