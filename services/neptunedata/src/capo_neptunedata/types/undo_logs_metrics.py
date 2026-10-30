"""Generated from Smithy shape ``com.amazonaws.neptunedata#UndoLogsMetrics``."""

from typing_extensions import TypedDict


class UndoLogsMetrics(TypedDict, closed=True):
    size_in_bytes: "int"
    """<p>The total size of the undo logs in bytes.</p>"""
    list_size: "int"
    """<p>The number of entries in the undo log list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UndoLogsMetrics) -> dict:
    out: dict = {}
    out["sizeInBytes"] = value["size_in_bytes"]
    out["listSize"] = value["list_size"]
    return out


def deserialize_json(data: dict) -> UndoLogsMetrics:
    out: UndoLogsMetrics = {}  # type: ignore[typeddict-item]
    if data.get("sizeInBytes") is not None:
        out["size_in_bytes"] = data["sizeInBytes"]
    else:
        out["size_in_bytes"] = 0
    if data.get("listSize") is not None:
        out["list_size"] = data["listSize"]
    else:
        out["list_size"] = 0
    return out
