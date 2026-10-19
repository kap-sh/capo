"""Generated from Smithy shape ``com.amazonaws.deadline#AcquiredLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.limit_id
    import capo_deadline.types.min_one_max_integer


class AcquiredLimit(TypedDict, closed=True):
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit.</p>"""
    count: "capo_deadline.types.min_one_max_integer.MinOneMaxInteger"
    """<p>The number of limit resources used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcquiredLimit) -> dict:
    out: dict = {}
    out["limitId"] = value["limit_id"]
    out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> AcquiredLimit:
    out: AcquiredLimit = {}  # type: ignore[typeddict-item]
    if data.get("limitId") is not None:
        out["limit_id"] = data["limitId"]
    else:
        out["limit_id"] = ""
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
