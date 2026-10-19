"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Roi``."""

from typing_extensions import NotRequired, TypedDict


class Roi(TypedDict, closed=True):
    estimate: NotRequired["str"]
    """<p>A short statistic or key metric. Optional when there is no quantifiable figure.</p>"""
    detail: "str"
    """<p>A sentence providing context for the estimate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Roi) -> dict:
    out: dict = {}
    if "estimate" in value:
        out["estimate"] = value["estimate"]
    out["detail"] = value["detail"]
    return out


def deserialize_json(data: dict) -> Roi:
    out: Roi = {}  # type: ignore[typeddict-item]
    if data.get("estimate") is not None:
        out["estimate"] = data["estimate"]
    if data.get("detail") is not None:
        out["detail"] = data["detail"]
    else:
        out["detail"] = ""
    return out
