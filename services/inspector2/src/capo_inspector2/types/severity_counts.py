"""Generated from Smithy shape ``com.amazonaws.inspector2#SeverityCounts``."""

from typing_extensions import NotRequired, TypedDict


class SeverityCounts(TypedDict, closed=True):
    all: NotRequired["int"]
    """<p>The total count of findings from all severities.</p>"""
    medium: NotRequired["int"]
    """<p>The total count of medium severity findings.</p>"""
    high: NotRequired["int"]
    """<p>The total count of high severity findings.</p>"""
    critical: NotRequired["int"]
    """<p>The total count of critical severity findings.</p>"""
    low: NotRequired["int"]
    """<p>The total count of low severity findings.</p>"""
    informational: NotRequired["int"]
    """<p>The total count of informational severity findings.</p>"""
    untriaged: NotRequired["int"]
    """<p>The total count of untriaged findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeverityCounts) -> dict:
    out: dict = {}
    if "all" in value:
        out["all"] = value["all"]
    if "medium" in value:
        out["medium"] = value["medium"]
    if "high" in value:
        out["high"] = value["high"]
    if "critical" in value:
        out["critical"] = value["critical"]
    if "low" in value:
        out["low"] = value["low"]
    if "informational" in value:
        out["informational"] = value["informational"]
    if "untriaged" in value:
        out["untriaged"] = value["untriaged"]
    return out


def deserialize_json(data: dict) -> SeverityCounts:
    out: SeverityCounts = {}  # type: ignore[typeddict-item]
    if data.get("all") is not None:
        out["all"] = data["all"]
    if data.get("medium") is not None:
        out["medium"] = data["medium"]
    if data.get("high") is not None:
        out["high"] = data["high"]
    if data.get("critical") is not None:
        out["critical"] = data["critical"]
    if data.get("low") is not None:
        out["low"] = data["low"]
    if data.get("informational") is not None:
        out["informational"] = data["informational"]
    if data.get("untriaged") is not None:
        out["untriaged"] = data["untriaged"]
    return out
