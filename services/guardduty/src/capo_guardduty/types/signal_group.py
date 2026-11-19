"""Generated from Smithy shape ``com.amazonaws.guardduty#SignalGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.finding_type
    import capo_guardduty.types.severity_score


class SignalGroup(TypedDict, closed=True):
    finding_type: NotRequired["capo_guardduty.types.finding_type.FindingType"]
    """<p>The finding type of the group.</p>"""
    severity: NotRequired["capo_guardduty.types.severity_score.SeverityScore"]
    """<p>The severity score of the signals in the group, from 0 to 10.</p>"""
    count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of signals in the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignalGroup) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "severity" in value:
        out["severity"] = (
            "NaN"
            if value["severity"] != value["severity"]
            else "Infinity"
            if value["severity"] == float("inf")
            else "-Infinity"
            if value["severity"] == float("-inf")
            else value["severity"]
        )
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> SignalGroup:
    out: SignalGroup = {}  # type: ignore[typeddict-item]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("severity") is not None:
        out["severity"] = float(data["severity"])
    if data.get("count") is not None:
        out["count"] = data["count"]
    return out
