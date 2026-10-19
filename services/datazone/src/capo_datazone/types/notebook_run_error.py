"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookRunError``."""

from typing_extensions import TypedDict


class NotebookRunError(TypedDict, closed=True):
    message: "str"
    """<p>The error message. The maximum length is 1024 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotebookRunError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotebookRunError:
    out: NotebookRunError = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
