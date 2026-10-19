"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalContent``."""

from typing_extensions import TypedDict


class GoalContent(TypedDict, closed=True):
    description: "str"
    """<p>A detailed description of the goal.</p>"""
    objectives: "str"
    """<p>The objectives to be achieved for this goal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GoalContent) -> dict:
    out: dict = {}
    out["description"] = value["description"]
    out["objectives"] = value["objectives"]
    return out


def deserialize_json(data: dict) -> GoalContent:
    out: GoalContent = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("objectives") is not None:
        out["objectives"] = data["objectives"]
    else:
        out["objectives"] = ""
    return out
