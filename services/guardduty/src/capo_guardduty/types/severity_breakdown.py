"""Generated from Smithy shape ``com.amazonaws.guardduty#SeverityBreakdown``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer


class SeverityBreakdown(TypedDict, closed=True):
    critical: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings that have Critical severity.</p>"""
    high: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings that have High severity.</p>"""
    medium: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings that have Medium severity.</p>"""
    low: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings that have Low severity.</p>"""
    info: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings that have Info severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeverityBreakdown) -> dict:
    out: dict = {}
    if "critical" in value:
        out["critical"] = value["critical"]
    if "high" in value:
        out["high"] = value["high"]
    if "medium" in value:
        out["medium"] = value["medium"]
    if "low" in value:
        out["low"] = value["low"]
    if "info" in value:
        out["info"] = value["info"]
    return out


def deserialize_json(data: dict) -> SeverityBreakdown:
    out: SeverityBreakdown = {}  # type: ignore[typeddict-item]
    if data.get("critical") is not None:
        out["critical"] = data["critical"]
    if data.get("high") is not None:
        out["high"] = data["high"]
    if data.get("medium") is not None:
        out["medium"] = data["medium"]
    if data.get("low") is not None:
        out["low"] = data["low"]
    if data.get("info") is not None:
        out["info"] = data["info"]
    return out
