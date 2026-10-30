"""Generated from Smithy shape ``com.amazonaws.neptunedata#StorageMetrics``."""

from typing_extensions import TypedDict


class StorageMetrics(TypedDict, closed=True):
    size_in_bytes: "int"
    """<p>Storage size in bytes.</p>"""
    count: "int"
    """<p>The number of entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageMetrics) -> dict:
    out: dict = {}
    out["sizeInBytes"] = value["size_in_bytes"]
    out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> StorageMetrics:
    out: StorageMetrics = {}  # type: ignore[typeddict-item]
    if data.get("sizeInBytes") is not None:
        out["size_in_bytes"] = data["sizeInBytes"]
    else:
        out["size_in_bytes"] = 0
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
