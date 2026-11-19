"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PriorityCount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.priority


class PriorityCount(TypedDict, closed=True):
    priority: "capo_wellarchitected.types.priority.Priority"
    """<p>Priority this count is attributed to.</p>"""
    count: "int"
    """<p>Non-negative count of recommendations in the report that are attributed to this priority.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PriorityCount) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.priority

    out["priority"] = capo_wellarchitected.types.priority.serialize_json(
        value["priority"]
    )
    out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> PriorityCount:
    out: PriorityCount = {}  # type: ignore[typeddict-item]
    if data.get("priority") is not None:
        import capo_wellarchitected.types.priority

        out["priority"] = capo_wellarchitected.types.priority.deserialize_json(
            data["priority"]
        )
    else:
        import typing

        out["priority"] = typing.cast(
            "capo_wellarchitected.types.priority.Priority", ""
        )
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
