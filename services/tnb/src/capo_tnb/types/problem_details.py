"""Generated from Smithy shape ``com.amazonaws.tnb#ProblemDetails``."""

from typing_extensions import NotRequired, TypedDict


class ProblemDetails(TypedDict, closed=True):
    detail: "str"
    """<p>A human-readable explanation specific to this occurrence of the problem.</p>"""
    title: NotRequired["str"]
    """<p>A human-readable title of the problem type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProblemDetails) -> dict:
    out: dict = {}
    out["detail"] = value["detail"]
    if "title" in value:
        out["title"] = value["title"]
    return out


def deserialize_json(data: dict) -> ProblemDetails:
    out: ProblemDetails = {}  # type: ignore[typeddict-item]
    if data.get("detail") is not None:
        out["detail"] = data["detail"]
    else:
        out["detail"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    return out
