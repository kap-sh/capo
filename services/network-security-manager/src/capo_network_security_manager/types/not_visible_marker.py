"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#NotVisibleMarker``."""

from typing_extensions import TypedDict


class NotVisibleMarker(TypedDict, closed=True):
    reason: "str"
    """<p>The reason the details are not visible.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotVisibleMarker) -> dict:
    out: dict = {}
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> NotVisibleMarker:
    out: NotVisibleMarker = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    return out
