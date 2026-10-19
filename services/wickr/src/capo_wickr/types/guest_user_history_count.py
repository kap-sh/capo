"""Generated from Smithy shape ``com.amazonaws.wickr#GuestUserHistoryCount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class GuestUserHistoryCount(TypedDict, closed=True):
    month: "capo_wickr.types.generic_string.GenericString"
    """<p>The month and billing period in YYYY_MM format (e.g., '2024_01').</p>"""
    count: "capo_wickr.types.generic_string.GenericString"
    """<p>The number of guest users who have communicated with your Wickr network during this billing period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuestUserHistoryCount) -> dict:
    out: dict = {}
    out["month"] = value["month"]
    out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> GuestUserHistoryCount:
    out: GuestUserHistoryCount = {}  # type: ignore[typeddict-item]
    if data.get("month") is not None:
        out["month"] = data["month"]
    else:
        out["month"] = ""
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = ""
    return out
