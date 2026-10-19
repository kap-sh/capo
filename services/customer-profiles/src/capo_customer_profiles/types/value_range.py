"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ValueRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.value_range_end
    import capo_customer_profiles.types.value_range_start


class ValueRange(TypedDict, closed=True):
    start: "capo_customer_profiles.types.value_range_start.ValueRangeStart"
    """<p>The start time of when to include objects. Use positive numbers to indicate that the starting point is in the past, and negative numbers to indicate it is in the future.</p>"""
    end: "capo_customer_profiles.types.value_range_end.ValueRangeEnd"
    """<p>The end time of when to include objects. Use positive numbers to indicate that the starting point is in the past, and negative numbers to indicate it is in the future.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValueRange) -> dict:
    out: dict = {}
    out["Start"] = value["start"]
    out["End"] = value["end"]
    return out


def deserialize_json(data: dict) -> ValueRange:
    out: ValueRange = {}  # type: ignore[typeddict-item]
    if data.get("Start") is not None:
        out["start"] = data["Start"]
    else:
        out["start"] = 0
    if data.get("End") is not None:
        out["end"] = data["End"]
    else:
        out["end"] = 0
    return out
