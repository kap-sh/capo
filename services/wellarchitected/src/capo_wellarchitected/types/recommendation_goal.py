"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationGoal``."""

from typing_extensions import TypedDict


class RecommendationGoal(TypedDict, closed=True):
    title: "str"
    """<p>The title of the goal associated with the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationGoal) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    return out


def deserialize_json(data: dict) -> RecommendationGoal:
    out: RecommendationGoal = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    return out
