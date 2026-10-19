"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookError``."""

from typing_extensions import TypedDict


class NotebookError(TypedDict, closed=True):
    message: "str"
    """<p>The error message. The maximum length is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotebookError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotebookError:
    out: NotebookError = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
