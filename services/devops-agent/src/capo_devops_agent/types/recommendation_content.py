"""Generated from Smithy shape ``com.amazonaws.devopsagent#RecommendationContent``."""

from typing_extensions import NotRequired, TypedDict


class RecommendationContent(TypedDict, closed=True):
    summary: "str"
    """<p>A brief summary of the recommendation.</p>"""
    spec: NotRequired["str"]
    """<p>Agent-ready specification with detailed implementation steps</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationContent) -> dict:
    out: dict = {}
    out["summary"] = value["summary"]
    if "spec" in value:
        out["spec"] = value["spec"]
    return out


def deserialize_json(data: dict) -> RecommendationContent:
    out: RecommendationContent = {}  # type: ignore[typeddict-item]
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    else:
        out["summary"] = ""
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    return out
